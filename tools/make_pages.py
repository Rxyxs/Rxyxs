"""Genera la GitHub Page de un repositorio a partir de su README y sus figuras.

    python tools/make_pages.py <ruta-al-repo> [--lang es|en] [--dry-run]

**Qué hace y qué no.** La página es un *índice visual*: toma el título, la
entradilla y cada figura del README con el párrafo que la explica, y las muestra
en un formato que se lee en diez segundos. Después enlaza al README para el resto.

No replica el README entero, y es deliberado: dos copias del mismo texto se
desincronizan, y la que nadie edita queda mintiendo. El README sigue siendo el
documento; la página es la portada.

El estilo es el mismo de las dos páginas hechas a mano (pensiones y Favorita),
así que los repos se ven como un conjunto y no como veinte sitios distintos.
"""
from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

FIG_RE = re.compile(r"^!\[(?P<alt>[^\]]*)\]\((?P<src>[^)\s]+)\)\s*$")
BADGE_RE = re.compile(r"^\[?!\[")
HEADING_RE = re.compile(r"^(#{1,3})\s+(.*)$")
LANG_TOGGLE_RE = re.compile(r"^\[\s*🇺🇸|^\[\s*🇨🇱")
PLACEHOLDER_TITLE_RE = re.compile(r"^\d*\.?\s*project title\s*$", re.I)


@dataclass
class Figure:
    src: str          # ruta tal como aparece en el README
    alt: str
    caption: str      # primer parrafo despues de la figura
    section: str      # encabezado bajo el que vive


@dataclass
class Page:
    title: str
    lede: str
    figures: list[Figure]


def _clean_inline(md: str) -> str:
    """Markdown en linea -> HTML, lo justo: negrita, codigo y enlaces."""
    s = html.escape(md.strip())
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', s)
    return s


def parse_readme(path: Path) -> Page:
    lines = path.read_text(encoding="utf-8").splitlines()

    title, lede = "", ""
    figures: list[Figure] = []
    section = ""
    i = 0

    # Titulo: el primer '# '. Tres READMEs del perfil arrastran un resto de
    # plantilla y su H1 dice literalmente "1. Project Title", con el titulo real
    # en el H2 siguiente. Cuando el H1 es ese marcador, se toma el H2.
    for idx, ln in enumerate(lines):
        m = HEADING_RE.match(ln)
        if m and len(m.group(1)) == 1:
            title = m.group(2).strip()
            i = idx + 1
            if PLACEHOLDER_TITLE_RE.match(title):
                for ln2 in lines[idx + 1: idx + 6]:
                    m2 = HEADING_RE.match(ln2)
                    if m2 and len(m2.group(1)) == 2:
                        title = m2.group(2).strip()
                        break
            break

    # Entradilla: el primer parrafo real despues del titulo, saltando badges,
    # el selector de idioma y las lineas vacias.
    while i < len(lines):
        ln = lines[i].strip()
        if not ln or BADGE_RE.match(ln) or LANG_TOGGLE_RE.match(ln) or HEADING_RE.match(ln):
            i += 1
            continue
        lede = ln
        break

    # Figuras, con la seccion donde viven y el parrafo que las sigue.
    for idx, ln in enumerate(lines):
        h = HEADING_RE.match(ln)
        if h:
            section = h.group(2).strip()
            continue
        m = FIG_RE.match(ln.strip())
        if not m:
            continue
        # Los badges (shields.io, el badge de CI) son imagenes remotas, no
        # figuras del proyecto. Sin este filtro la pagina intentaria copiar una
        # URL como si fuera un archivo local, que es lo que hacia la primera
        # version.
        if m.group("src").startswith(("http://", "https://")):
            continue
        caption = ""
        for nxt in lines[idx + 1: idx + 6]:
            t = nxt.strip()
            if not t or FIG_RE.match(t):
                continue
            if HEADING_RE.match(t) or t.startswith("|") or t.startswith("```"):
                break
            caption = t
            break
        figures.append(Figure(src=m.group("src"), alt=m.group("alt"),
                              caption=caption, section=section))

    return Page(title=title, lede=lede, figures=figures)


CSS = """
  :root { --bg:#FBFAF8; --surface:#FFF; --ink:#23201D; --muted:#6B645D; --line:#E3DED7; --accent:#B5553D; }
  @media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
    --bg:#171614; --surface:#201E1B; --ink:#EDE9E3; --muted:#A9A29A; --line:#322E2A; --accent:#D9765C; } }
  :root[data-theme="dark"] { --bg:#171614; --surface:#201E1B; --ink:#EDE9E3; --muted:#A9A29A; --line:#322E2A; --accent:#D9765C; }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--bg); color:var(--ink);
    font:16px/1.68 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
    -webkit-font-smoothing:antialiased; }
  .wrap { max-width:900px; margin:0 auto; padding:0 16px 88px; }
  header { padding:60px 0 32px; border-bottom:1px solid var(--line); margin-bottom:36px; }
  h1 { font-size:clamp(1.7rem,5vw,2.4rem); line-height:1.16; margin:0 0 18px; letter-spacing:-.02em; }
  .lede { font-size:clamp(1rem,2.3vw,1.1rem); color:var(--muted); margin:0 0 22px; max-width:62ch; }
  .lede strong { color:var(--ink); }
  .links a { display:inline-block; margin:0 9px 9px 0; padding:9px 15px; border:1px solid var(--line);
    border-radius:7px; text-decoration:none; color:var(--ink); background:var(--surface); font-size:.9rem;
    transition:border-color .15s; }
  .links a:hover { border-color:var(--accent); }
  h2 { font-size:1.3rem; margin:48px 0 8px; padding-top:12px; border-top:1px solid var(--line); letter-spacing:-.01em; }
  figure { margin:22px 0; }
  figure img { width:100%; height:auto; display:block; border:1px solid var(--line); border-radius:9px; background:#fff; }
  figcaption { font-size:.85rem; color:var(--muted); margin-top:9px; max-width:70ch; }
  p { margin:0 0 16px; max-width:70ch; }
  code { background:var(--surface); border:1px solid var(--line); border-radius:4px; padding:1px 5px; font-size:.86em;
    font-family:ui-monospace,SFMono-Regular,Consolas,monospace; }
  footer { margin-top:60px; padding-top:22px; border-top:1px solid var(--line); font-size:.86rem; color:var(--muted); }
  a { color:var(--accent); }
"""

TEXT = {
    "es": {
        "code": "Código y metodología",
        "readme": "README completo",
        "intro": ("Esta página muestra los resultados del proyecto. El detalle de la metodología, "
                  "las decisiones de diseño y las limitaciones están en el README del repositorio."),
        "foot": ("Cada figura de esta página la produce el pipeline del repositorio. "
                 "Para el método completo y las limitaciones, ver el README."),
    },
    "en": {
        "code": "Code and method",
        "readme": "Full README",
        "intro": ("This page shows the project's results. The methodology, the design decisions "
                  "and the limitations are documented in the repository's README."),
        "foot": ("Every figure on this page is produced by the repository's pipeline. "
                 "For the full method and its limitations, see the README."),
    },
}


def render(page: Page, repo: str, lang: str) -> str:
    t = TEXT[lang]
    url = f"https://github.com/Rxyxs/{repo}"
    parts = [
        "<!doctype html>", f'<html lang="{lang}">', "<head>", '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{html.escape(page.title)}</title>",
        f'<meta name="description" content="{html.escape(page.lede[:180])}">',
        f"<style>{CSS}</style>", "</head>", "<body>", '<div class="wrap">',
        "<header>", f"<h1>{html.escape(page.title)}</h1>",
        f'<p class="lede">{_clean_inline(page.lede)}</p>',
        '<div class="links">',
        f'<a href="{url}">{t["code"]}</a>',
        f'<a href="{url}#readme">{t["readme"]}</a>',
        "</div></header>",
        f"<p>{t['intro']}</p>",
    ]

    last_section = None
    for f in page.figures:
        if f.section and f.section != last_section:
            parts.append(f"<h2>{html.escape(f.section)}</h2>")
            last_section = f.section
        name = Path(f.src).name
        parts.append("<figure>")
        parts.append(f'<img src="figures/{name}" alt="{html.escape(f.alt)}" loading="lazy">')
        if f.caption:
            parts.append(f"<figcaption>{_clean_inline(f.caption)}</figcaption>")
        parts.append("</figure>")

    parts += [
        "<footer>", f'Pablo Reyes · <a href="{url}">github.com/Rxyxs/{repo}</a> · MIT<br><br>',
        t["foot"], "</footer>", "</div></body></html>", "",
    ]
    return "\n".join(parts)


def build(repo_dir: Path, lang: str, dry_run: bool = False) -> bool:
    readme = repo_dir / ("README.md" if lang == "en" else "README.es.md")
    if not readme.exists():
        readme = repo_dir / "README.md"
    if not readme.exists():
        print(f"  [saltado] {repo_dir.name}: sin README")
        return False

    page = parse_readme(readme)
    if len(page.figures) < 3:
        print(f"  [saltado] {repo_dir.name}: solo {len(page.figures)} figuras referenciadas")
        return False

    docs = repo_dir / "docs"
    figs = docs / "figures"

    # NUNCA pisar una pagina existente. Varios repos tienen un docs/index.html
    # escrito a mano, mas largo y mejor que lo que este generador produce, y la
    # primera corrida de este script reemplazo tres de ellos por versiones
    # generadas mas pobres. Un generador por lotes solo deberia crear lo que no
    # existe.
    if (docs / "index.html").exists():
        print(f"  [saltado] {repo_dir.name}: ya tiene docs/index.html, no se toca")
        return False
    missing = []
    for f in page.figures:
        src = repo_dir / f.src
        if not src.exists():
            missing.append(f.src)
    if missing:
        print(f"  [saltado] {repo_dir.name}: figuras referenciadas que no existen: {missing[:2]}")
        return False

    if dry_run:
        print(f"  [ok] {repo_dir.name}: {len(page.figures)} figuras · \"{page.title[:48]}\"")
        return True

    figs.mkdir(parents=True, exist_ok=True)
    for f in page.figures:
        src = (repo_dir / f.src).resolve()
        dst = (figs / Path(f.src).name).resolve()
        # Algun repo ya guarda sus figuras dentro de docs/figures/, en cuyo caso
        # origen y destino son el mismo archivo y copy2 falla.
        if src != dst:
            shutil.copy2(src, dst)
    (docs / "index.html").write_text(render(page, repo_dir.name, lang), encoding="utf-8")
    # .nojekyll le dice a Pages que sirva los archivos tal cual en vez de pasarlos
    # por Jekyll. Para HTML estatico no aporta nada procesarlos, y Jekyll ignora
    # por defecto cualquier ruta que empiece con guion bajo, que es una forma
    # silenciosa de que falte una figura.
    (docs / ".nojekyll").write_text("", encoding="utf-8")
    print(f"  [hecho] {repo_dir.name}: {len(page.figures)} figuras -> docs/index.html")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("repos", nargs="+", type=Path)
    ap.add_argument("--lang", choices=("es", "en"), default="en")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    built = 0
    for r in args.repos:
        if build(r, args.lang, args.dry_run):
            built += 1
    print(f"\n{built} de {len(args.repos)} repositorios")
    return 0


if __name__ == "__main__":
    sys.exit(main())
