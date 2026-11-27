"""Công cụ của bài toán — phần Tùng phụ trách (CP2).

Mỗi công cụ có @tool và docstring ghi đủ 4 ý theo spec.md §4:
    tên · input · output · có tác động ra ngoài không.
Chỉ dùng thư viện chuẩn của Python.
"""
import os
import re

from tracing import tool, TOOLS  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABS_DIR = os.path.join(ROOT, "data", "labs")

_RE_HEADING = re.compile(r"^\s*##\s+(.+?)\s*$")
_RE_TITLE = re.compile(r"^\s*#\s+(.+?)\s*$")
_RE_ITEM = re.compile(r"^\s*[-*]\s*\[([^\]]+)\]\s*(.+?)\s*$")
_RE_CP = re.compile(r"\b(?:CP|CHECKPOINT)\s*(\d+)\b", re.IGNORECASE)
_RE_SAFE_ID = re.compile(r"^[A-Za-z0-9_-]+$")


def _normalize_cp(text: str) -> str:
    m = _RE_CP.search(text or "")
    return ("CP" + m.group(1)) if m else ""


def _classify_section(section: str, cp: str) -> str:
    low = section.lower()
    if low.startswith("0.") or "quy định chung" in low or "yêu cầu chung" in low:
        return "general"
    if "nộp bài" in low or "submission" in low:
        return "submit"
    if cp:
        return "checkpoint"
    return "other"


@tool
def list_labs() -> list:
    """list_labs · Input: không · Output: danh sách mã đề lab (list[str]) hiện có trong data/labs/ · Không tác động ra ngoài."""
    if not os.path.isdir(LABS_DIR):
        return []
    labs = []
    for name in os.listdir(LABS_DIR):
        if name.lower().endswith(".md"):
            labs.append(os.path.splitext(name)[0].upper())
    return sorted(set(labs))


@tool
def read_lab(lab_id: str) -> dict:
    """read_lab · Input: mã lab (str, vd 'LAB1') · Output: dict gồm found, lab_id, title, checkpoints, items (code/section/section_type/checkpoint/text), raw · Không tác động ra ngoài."""
    clean_id = (lab_id or "").strip().upper()
    if not clean_id or not _RE_SAFE_ID.match(clean_id) or not os.path.isdir(LABS_DIR):
        return {
            "found": False,
            "lab_id": clean_id,
            "title": "",
            "checkpoints": [],
            "items": [],
            "raw": "",
        }

    target_path = None
    for name in os.listdir(LABS_DIR):
        if name.lower() == (clean_id.lower() + ".md"):
            target_path = os.path.join(LABS_DIR, name)
            break

    if not target_path or not os.path.isfile(target_path):
        return {
            "found": False,
            "lab_id": clean_id,
            "title": "",
            "checkpoints": [],
            "items": [],
            "raw": "",
        }

    with open(target_path, encoding="utf-8-sig") as f:
        raw = f.read()

    title = ""
    current_section = ""
    current_cp = ""
    current_type = "other"
    checkpoints = []
    items = []

    for line in raw.splitlines():
        if not title:
            m_title = _RE_TITLE.match(line)
            if m_title:
                title = m_title.group(1).strip()
                continue

        m_head = _RE_HEADING.match(line)
        if m_head:
            current_section = m_head.group(1).strip()
            current_cp = _normalize_cp(current_section)
            current_type = _classify_section(current_section, current_cp)
            if current_cp and current_cp not in checkpoints:
                checkpoints.append(current_cp)
            continue

        m_item = _RE_ITEM.match(line)
        if m_item:
            code = m_item.group(1).strip()
            content = m_item.group(2).strip()
            items.append({
                "code": code,
                "section": current_section,
                "section_type": current_type,
                "checkpoint": current_cp,
                "text": content,
            })

    return {
        "found": True,
        "lab_id": clean_id,
        "title": title,
        "checkpoints": checkpoints,
        "items": items,
        "raw": raw,
    }
