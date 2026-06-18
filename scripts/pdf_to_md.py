#!/usr/bin/env python3
"""Convert PDF files to Markdown preserving content and structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import fitz
from markdownify import markdownify as html_to_md


def slugify(name: str) -> str:
    slug = name.lower()
    slug = re.sub(r"\.pdf$", "", slug, flags=re.IGNORECASE)
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def span_style(span: dict) -> dict:
    flags = span.get("flags", 0)
    return {
        "bold": bool(flags & 2**4),
        "italic": bool(flags & 2**1),
        "size": round(span.get("size", 0), 1),
    }


def format_span_text(text: str, bold: bool, italic: bool) -> str:
    if not text:
        return ""
    if bold and italic:
        return f"***{text}***"
    if bold:
        return f"**{text}**"
    if italic:
        return f"*{text}*"
    return text


def line_to_markdown(line: dict) -> str:
    parts: list[str] = []
    for span in line.get("spans", []):
        text = span.get("text", "")
        style = span_style(span)
        parts.append(format_span_text(text, style["bold"], style["italic"]))
    return "".join(parts).rstrip()


def max_line_size(line: dict) -> float:
    sizes = [span.get("size", 0) for span in line.get("spans", []) if span.get("text", "").strip()]
    return max(sizes) if sizes else 0


def classify_heading(size: float, body_size: float) -> int | None:
    if size >= body_size + 6:
        return 1
    if size >= body_size + 3:
        return 2
    if size >= body_size + 1.5:
        return 3
    return None


def detect_body_size(blocks: list[dict]) -> float:
    sizes: list[float] = []
    for block in blocks:
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            text = line_to_markdown(line).strip()
            if not text or text in {"•", "○"}:
                continue
            size = max_line_size(line)
            if 8 <= size <= 13:
                sizes.append(size)
    if not sizes:
        return 10.6
    sizes.sort()
    return sizes[len(sizes) // 2]


def extract_images_for_page(page: fitz.Page, image_dir: Path, page_num: int) -> dict[int, str]:
    image_dir.mkdir(parents=True, exist_ok=True)
    mapping: dict[int, str] = {}
    seen_xrefs: dict[int, str] = {}

    for img_index, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        if xref in seen_xrefs:
            mapping[img_index] = seen_xrefs[xref]
            continue
        try:
            base_image = page.parent.extract_image(xref)
        except Exception:
            continue
        ext = base_image.get("ext", "png")
        image_bytes = base_image["image"]
        filename = f"page-{page_num:03d}-img-{img_index + 1:03d}.{ext}"
        image_path = image_dir / filename
        image_path.write_bytes(image_bytes)
        rel_from_md = f"images/{image_dir.name}/{filename}"
        seen_xrefs[xref] = rel_from_md
        mapping[img_index] = rel_from_md

    return mapping


def blocks_to_markdown(blocks: list[dict], body_size: float, image_refs: dict[int, str]) -> str:
    lines_out: list[str] = []
    pending_bullet = False
    image_counter = 0

    for block in blocks:
        if block.get("type") == 1:
            ref = image_refs.get(image_counter)
            image_counter += 1
            if ref:
                lines_out.append(f"![image]({ref})")
            continue

        if block.get("type") != 0:
            continue

        for line in block.get("lines", []):
            text = line_to_markdown(line).strip()
            if not text:
                continue

            if text in {"•", "○"}:
                pending_bullet = True
                continue

            if pending_bullet:
                lines_out.append(f"- {text}")
                pending_bullet = False
                continue

            size = max_line_size(line)
            heading_level = classify_heading(size, body_size)

            numbered = re.match(r"^(\d+)\.$", text)
            if numbered:
                lines_out.append(f"{numbered.group(1)}.")
                continue

            if heading_level == 1:
                lines_out.append(f"# {text}")
            elif heading_level == 2:
                lines_out.append(f"## {text}")
            elif heading_level == 3:
                lines_out.append(f"### {text}")
            else:
                lines_out.append(text)

    return "\n\n".join(lines_out)


def convert_page(page: fitz.Page, page_num: int, image_dir: Path) -> str:
    blocks = page.get_text("dict")["blocks"]
    body_size = detect_body_size(blocks)
    image_refs = extract_images_for_page(page, image_dir, page_num)
    page_md = blocks_to_markdown(blocks, body_size, image_refs)

    if not page_md and image_refs:
        page_md = "\n\n".join(f"![image]({ref})" for ref in image_refs.values())

    return page_md.strip()


def convert_pdf(pdf_path: Path, md_dir: Path) -> Path:
    doc = fitz.open(pdf_path)
    slug = slugify(pdf_path.name)
    output_path = md_dir / f"{slug}.md"
    image_dir = md_dir / "images" / slug

    parts: list[str] = []
    for page_index, page in enumerate(doc):
        page_md = convert_page(page, page_index + 1, image_dir)
        if page_md:
            parts.append(page_md)

    doc.close()

    content = "\n\n---\n\n".join(parts)
    output_path.write_text(content + "\n", encoding="utf-8")
    return output_path


def main(argv: list[str]) -> int:
    workspace = Path("/workspace")
    md_dir = workspace / "md"
    md_dir.mkdir(exist_ok=True)

    pdf_names = ["Acronimi.pdf", "OC BASE.pdf", "tutorials.pdf"]
    created: list[Path] = []

    for name in pdf_names:
        pdf_path = workspace / name
        if not pdf_path.exists():
            print(f"Missing: {pdf_path}", file=sys.stderr)
            return 1
        out = convert_pdf(pdf_path, md_dir)
        created.append(out)
        print(f"Created {out} ({out.stat().st_size} bytes)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
