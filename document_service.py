from __future__ import annotations

from io import BytesIO
from pathlib import Path

from pypdf import PdfReader

TEXT_EXTENSIONS = {
    ".txt", ".log", ".cfg", ".conf", ".json", ".yaml", ".yml",
    ".py", ".md", ".csv", ".xml",
}


def extract_uploaded_text(uploaded_file, max_chars: int = 20000) -> str:
    if uploaded_file is None:
        return ""

    filename = uploaded_file.name
    suffix = Path(filename).suffix.lower()
    raw = uploaded_file.getvalue()

    if suffix in TEXT_EXTENSIONS:
        return raw.decode("utf-8", errors="replace")[:max_chars]

    if suffix == ".pdf":
        reader = PdfReader(BytesIO(raw))
        pages: list[str] = []

        for page in reader.pages:
            pages.append(page.extract_text() or "")

        return "\n\n".join(pages)[:max_chars]

    raise ValueError(
        f"Unsupported file type: {suffix or 'unknown'}. "
        "Supported types include PDF, TXT, LOG, CFG, JSON, YAML, PY, CSV, and XML."
    )
