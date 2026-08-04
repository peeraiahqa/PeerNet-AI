create extension if not exists pgcrypto;

create table if not exists public.profiles (
    id uuid primary key references auth.users(id) on delete cascade,
    email text not null,
    full_name text not null default '',
    username text not null default '',
    bio text not null default '',
    role text not null default 'member'
        check (role in ('member', 'admin')),
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create unique index if not exists profiles_username_unique
on public.profiles (lower(username))
where username <> '';

create table if not exists public.conversations (
    id uuid primary key default gen_random_uuid(),
    user_id uuid not null references auth.users(id) on delete cascade,
    title text not null default 'New conversation',
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create index if not exists conversations_user_id_idx
on public.conversations(user_id);

create table if not exists public.messages (
    id uuid primary key default gen_random_uuid(),
    conversation_id uuid not null
        references public.conversations(id) on delete cascade,
    user_id uuid not null references auth.users(id) on delete cascade,
    role text not null check (role in ('user', 'assistant')),
    content text not null,
    created_at timestamptz not null default now()
);

create index if not exists messages_conversation_id_idx
on public.messages(conversation_id);

create index if not exists messages_user_id_idx
on public.messages(user_id);

create table if not exists public.favorites (
    id uuid primary key default gen_random_uuid(),
    user_id uuid not null references auth.users(id) on delete cascade,
    title text not null,
    content text not null,
    created_at timestamptz not null default now()
);

create index if not exists favorites_user_id_idx
on public.favorites(user_id);

alter table public.profiles enable row level security;
alter table public.conversations enable row level security;
alter table public.messages enable row level security;
alter table public.favorites enable row level security;

drop policy if exists "profiles_select_own" on public.profiles;
create policy "profiles_select_own"
on public.profiles
for select
to authenticated
using ((select auth.uid()) = id);

drop policy if exists "profiles_update_own" on public.profiles;
create policy "profiles_update_own"
on public.profiles
for update
to authenticated
using ((select auth.uid()) = id)
with check ((select auth.uid()) = id);

drop policy if exists "conversations_all_own" on public.conversations;
create policy "conversations_all_own"
on public.conversations
for all
to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

drop policy if exists "messages_all_own" on public.messages;
create policy "messages_all_own"
on public.messages
for all
to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

drop policy if exists "favorites_all_own" on public.favorites;
create policy "favorites_all_own"
on public.favorites
for all
to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

grant select, update on public.profiles to authenticated;
grant select, insert, update, delete on public.conversations to authenticated;
grant select, insert, update, delete on public.messages to authenticated;
grant select, insert, update, delete on public.favorites to authenticated;

create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
    insert into public.profiles (
        id,
        email,
        full_name,
        username
    )
    values (
        new.id,
        coalesce(new.email, ''),
        coalesce(new.raw_user_meta_data ->> 'full_name', ''),
        coalesce(new.raw_user_meta_data ->> 'username', '')
    )
    on conflict (id) do nothing;

    return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;

create trigger on_auth_user_created
after insert on auth.users
for each row
execute procedure public.handle_new_user();

-- After registering your own account:
-- update public.profiles
-- set role = 'admin'
-- where email = 'your-email@example.com';


create table if not exists public.usage_events (
    id uuid primary key default gen_random_uuid(),
    user_id uuid not null references auth.users(id) on delete cascade,
    mode text not null,
    model text not null,
    created_at timestamptz not null default now()
);

create index if not exists usage_events_user_id_idx
on public.usage_events(user_id);

create table if not exists public.message_feedback (
    id uuid primary key default gen_random_uuid(),
    user_id uuid not null references auth.users(id) on delete cascade,
    conversation_id uuid references public.conversations(id) on delete set null,
    message_content text not null,
    rating text not null check (rating in ('helpful', 'not_helpful')),
    created_at timestamptz not null default now()
);

create index if not exists message_feedback_user_id_idx
on public.message_feedback(user_id);

alter table public.usage_events enable row level security;
alter table public.message_feedback enable row level security;

drop policy if exists "usage_events_own" on public.usage_events;
create policy "usage_events_own"
on public.usage_events
for all
to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

drop policy if exists "message_feedback_own" on public.message_feedback;
create policy "message_feedback_own"
on public.message_feedback
for all
to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

grant select, insert on public.usage_events to authenticated;
grant select, insert on public.message_feedback to authenticated;
