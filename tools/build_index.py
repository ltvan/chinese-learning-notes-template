#!/usr/bin/env python3
"""Sinh lại index/ từ frontmatter của chars/, words/, radicals/ và kiểm tra vault.

Chạy:  python3 tools/build_index.py
Exit 1 nếu có cảnh báo (trùng tên file, thành phần/bộ thủ chưa có note).

Frontmatter phải phẳng: `key: value` hoặc `key: [a, b]`. Giá trị có ": " thì đặt trong ngoặc kép.
"""
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTE_DIRS = ["chars", "words", "radicals"]
SKIP_DIRS = {"index", "templates", "docs", "tools"}
INDEX = ROOT / "index"
HEADER = "<!-- Sinh tự động bởi tools/build_index.py — đừng sửa tay -->\n\n"


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data = {}
    for line in text[4:end].splitlines():
        line = line.split(" #")[0]
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            value = [v.strip().strip("\"'") for v in value[1:-1].split(",") if v.strip()]
        else:
            value = value.strip("\"'")
        data[key.strip()] = value
    return data


def as_list(value):
    if not value:
        return []
    return value if isinstance(value, list) else [value]


def strip_marks(s):
    s = s.lower().replace("đ", "d")
    return "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c))


def load_notes():
    notes = {}
    for d in NOTE_DIRS:
        for path in sorted((ROOT / d).glob("*.md")):
            stem = unicodedata.normalize("NFC", path.stem)
            notes[stem] = {"name": stem, "dir": d, **parse_frontmatter(path)}
    return notes


def check(notes):
    problems = []
    stems = defaultdict(list)
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if rel.parts[0].startswith(".") or rel.parts[0] in SKIP_DIRS:
            continue
        stems[unicodedata.normalize("NFC", path.stem)].append(str(rel))
    for stem, paths in stems.items():
        if len(paths) > 1:
            problems.append(f"Trùng tên file '{stem}': {', '.join(paths)}")
    for n in notes.values():
        refs = as_list(n.get("components")) + as_list(n.get("radical")) + as_list(n.get("chars")) + as_list(n.get("variant_of"))
        for ref in refs:
            if ref not in notes:
                problems.append(f"{n['dir']}/{n['name']}.md nhắc tới '{ref}' nhưng chưa có note")
    return problems


def row(n):
    radical = f"[[{n['radical']}]]" if n.get("radical") else ""
    return f"| [[{n['name']}]] | {n.get('pinyin', '')} | {n.get('hanviet', '')} | {n.get('meaning', '')} | {radical} | {n.get('hsk', '')} |"


TABLE_HEAD = "| Chữ/Từ | Pinyin | Hán Việt | Nghĩa | Bộ | HSK |\n|---|---|---|---|---|---|\n"


def write(name, title, body):
    INDEX.mkdir(exist_ok=True)
    (INDEX / f"{name}.md").write_text(f"{HEADER}# {title}\n\n{body}", encoding="utf-8")


def grouped_tables(groups, order):
    out = []
    for key in order:
        out.append(f"## {key}\n\n{TABLE_HEAD}" + "\n".join(row(n) for n in groups[key]) + "\n")
    return "\n".join(out)


def build(notes):
    learned = [n for n in notes.values() if n.get("learned")]

    groups = defaultdict(list)
    for n in sorted(learned, key=lambda n: (n.get("pinyin_plain", ""), n["name"])):
        groups[(n.get("pinyin_plain") or "?")[0].upper()].append(n)
    write("by-pinyin", "Tra theo pinyin", grouped_tables(groups, sorted(groups)))

    groups = defaultdict(list)
    for n in sorted(learned, key=lambda n: (strip_marks(n.get("hanviet", "")), n.get("hanviet", ""))):
        if n.get("hanviet"):
            groups[strip_marks(n["hanviet"])[0].upper()].append(n)
    write("by-hanviet", "Tra theo âm Hán Việt", grouped_tables(groups, sorted(groups)))

    groups = defaultdict(list)
    for n in sorted(learned, key=lambda n: n["name"]):
        groups[str(n["learned"])].append(n)
    write("by-date", "Tra theo ngày học", grouped_tables(groups, sorted(groups, reverse=True)))

    # Gom biến thể (亻) về bộ gốc (人), sắp theo số thứ tự Khang Hy
    groups = defaultdict(list)
    for n in learned:
        if n.get("radical"):
            rad = notes.get(n["radical"], {})
            groups[rad.get("variant_of") or n["radical"]].append(n)

    def kangxi(root):
        try:
            return int(notes.get(root, {}).get("kangxi", 999))
        except ValueError:
            return 999

    out = []
    for root in sorted(groups, key=lambda r: (kangxi(r), r)):
        r = notes.get(root, {})
        out.append(f"## [[{root}]] {r.get('hanviet', '')} — {r.get('meaning', '')} (#{r.get('kangxi', '?')})\n\n{TABLE_HEAD}"
                   + "\n".join(row(n) for n in sorted(groups[root], key=lambda n: n.get("pinyin_plain", ""))) + "\n")
    write("by-radical", "Tra theo bộ thủ", "\n".join(out))

    pairs = [n for n in learned if n.get("traditional") and n["traditional"] != n.get("simplified", n["name"])]
    body = "| Phồn thể | Giản thể | Pinyin | Hán Việt | Nghĩa |\n|---|---|---|---|---|\n" + "\n".join(
        f"| {n['traditional']} | [[{n['name']}]] | {n.get('pinyin', '')} | {n.get('hanviet', '')} | {n.get('meaning', '')} |"
        for n in sorted(pairs, key=lambda n: n.get("pinyin_plain", ""))) + "\n"
    write("traditional", "Tra ngược từ phồn thể", body)
    return len(learned)


def main():
    notes = load_notes()
    count = build(notes)
    problems = check(notes)
    print(f"Đã sinh index: {count} note đã học / {len(notes)} note (kể cả stub).")
    for p in problems:
        print(f"CẢNH BÁO: {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
