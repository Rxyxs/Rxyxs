"""Genera la GitHub Page de un repositorio a partir de su README y sus figuras.

    python tools/make_pages.py <ruta-al-repo> [--lang es|en] [--dry-run] [--repair]

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
LANG_TOGGLE_RE = re.compile(r"^\[+\s*(🇺🇸|🇨🇱|English|Español)")
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
    """Markdown en linea -> HTML, lo justo: negrita, cursiva, codigo y enlaces.

    Los enlaces relativos (a un archivo del repo) apuntan a una ruta que en la
    pagina no existe, asi que se deja solo su texto.
    """
    s = html.escape(md.strip())
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![*\w])\*([^*]+)\*(?![*\w])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\[([^\]]+)\]\([^)\s]+\)", r"\1", s)
    return s


def _is_block(t: str) -> bool:
    return bool(HEADING_RE.match(t) or FIG_RE.match(t) or t.startswith(("|", "```", "<", "---")))


def _paragraph(lines: list[str], start: int) -> str:
    """El parrafo que empieza en `start`, con todas sus lineas.

    Los READMEs cortan los parrafos a ~80 columnas. La primera version de este
    script tomaba solo la primera linea, y cada leyenda quedaba cortada a mitad
    de frase.
    """
    out = []
    for ln in lines[start:]:
        t = ln.strip()
        if not t or _is_block(t):
            break
        out.append(t)
    return " ".join(out)


def _trim_sentences(s: str, limit: int = 600) -> str:
    """Una leyenda larguisima no se lee en una pagina de figuras: se corta en la
    ultima frase completa antes de `limit` (el resto sigue en el README)."""
    if len(s) <= limit:
        return s
    cut = s.rfind(". ", 0, limit)
    return s[:cut + 1] if cut > 0 else s


def _unwrap_italics(s: str) -> str:
    """Las leyendas suelen ir enteras en cursiva (*...*); en la pagina ya lo parecen."""
    s = s.strip()
    if len(s) > 2 and s[0] == s[-1] and s[0] in "*_" and s[1] != s[0]:
        return s[1:-1].strip()
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
        if (not ln or BADGE_RE.match(ln) or LANG_TOGGLE_RE.match(ln) or _is_block(ln)
                or ln.startswith(("🌐", ">")) or "](README" in ln):
            i += 1
            continue
        lede = _paragraph(lines, i)
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
        for j in range(idx + 1, min(idx + 6, len(lines))):
            t = lines[j].strip()
            if not t or FIG_RE.match(t):
                continue
            if not _is_block(t):
                caption = _trim_sentences(_unwrap_italics(_paragraph(lines, j)))
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
        f'<meta name="description" content="{html.escape(re.sub(r"[*_`]", "", page.lede)[:180])}">',
        f'<meta name="generator" content="{GENERATOR}">',
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


GENERATOR = "Rxyxs/tools/make_pages.py"


def made_by_this_script(index: Path) -> bool:
    """Una pagina generada lleva la marca, o (las de antes de la marca) la frase de entrada."""
    s = index.read_text(encoding="utf-8")
    return GENERATOR in s or any(t["intro"] in s for t in TEXT.values())


def _readme(repo_dir: Path, lang: str) -> Path | None:
    readme = repo_dir / ("README.md" if lang == "en" else "README.es.md")
    if not readme.exists():
        readme = repo_dir / "README.md"
    return readme if readme.exists() else None


FIGURE_HTML_RE = re.compile(
    r'(?P<img><img src="figures/(?P<name>[^"]+)"[^>]*>)(?P<cap>\s*<figcaption>.*?</figcaption>)?', re.S)


def repair(repo_dir: Path, lang: str, dry_run: bool = False) -> bool:
    """Arregla una pagina generada sin rehacerla.

    Varias paginas generadas se completaron despues a mano (tablas y secciones
    con los resultados sobre datos reales), asi que regenerarlas borraria ese
    trabajo. Esto solo reemplaza cada leyenda por el parrafo completo que el
    README pone bajo la misma figura, rehace la meta descripcion desde la
    entradilla visible y actualiza las copias de las figuras que la pagina
    muestra. Lo demas queda como esta.
    """
    index = repo_dir / "docs" / "index.html"
    readme = _readme(repo_dir, lang)
    if not index.exists() or readme is None or not made_by_this_script(index):
        print(f"  [saltado] {repo_dir.name}: sin pagina generada o sin README")
        return False
    page = parse_readme(readme)
    captions = {Path(f.src).name: f.caption for f in page.figures if f.caption}
    sources = {Path(f.src).name: repo_dir / f.src for f in page.figures}

    def fix(m: re.Match) -> str:
        cap = captions.get(m.group("name"))
        if not cap:
            return m.group(0)
        return f'{m.group("img")}\n<figcaption>{_clean_inline(cap)}</figcaption>'

    before = index.read_text(encoding="utf-8")
    after = FIGURE_HTML_RE.sub(fix, before)
    lede = re.search(r'<p class="lede">(.*?)</p>', after, re.S)
    if lede:
        text = html.unescape(re.sub(r"<[^>]+>", "", lede.group(1))).strip()
        after = re.sub(r'<meta name="description" content="[^"]*">',
                       lambda _: f'<meta name="description" content="{html.escape(text[:180])}">', after, count=1)

    stale = []
    for name in sorted(set(re.findall(r'<img src="figures/([^"]+)"', after))):
        src, dst = sources.get(name), repo_dir / "docs" / "figures" / name
        if src is None or not src.exists() or src.resolve() == dst.resolve():
            continue
        if not dst.exists() or src.read_bytes() != dst.read_bytes():
            stale.append(name)
            if not dry_run:
                shutil.copy2(src, dst)
    if after != before and not dry_run:
        index.write_text(after, encoding="utf-8", newline="\n")
    print(f"  [{'cambia' if after != before or stale else 'igual'}] {repo_dir.name}: "
          f"{len(captions)} leyendas, {len(stale)} figuras actualizadas")
    return after != before or bool(stale)


def build(repo_dir: Path, lang: str, dry_run: bool = False) -> bool:
    readme = _readme(repo_dir, lang)
    if readme is None:
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
    # existe (para arreglar una pagina generada, ver `repair`).
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
    ap.add_argument("--repair", action="store_true",
                    help="arreglar leyendas y figuras de paginas ya generadas, sin rehacerlas")
    args = ap.parse_args()

    built = 0
    for r in args.repos:
        done = repair(r, args.lang, args.dry_run) if args.repair else build(r, args.lang, args.dry_run)
        if done:
            built += 1
    print(f"\n{built} de {len(args.repos)} repositorios")
    return 0


if __name__ == "__main__":
    sys.exit(main())
