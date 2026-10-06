"""Genera el README del perfil (español e inglés) y el sitio rxyxs.github.io desde perfil.json.

    python tools/build_profile.py                         # README.md y README.en.md
    python tools/build_profile.py --site ../Rxyxs.github.io   # además, el sitio

Los proyectos, sus resultados y sus etiquetas viven solo en ``tools/perfil.json``: el README y
el sitio se generan desde ahí para que nunca digan cosas distintas. Para agregar o corregir un
proyecto se edita el JSON y se vuelve a correr este script.
"""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
GH = "https://github.com/Rxyxs/"
PAGE = "https://rxyxs.github.io/"

D = json.loads((ROOT / "tools" / "perfil.json").read_text(encoding="utf-8"))
ES, EN = 0, 1


def t(L: int, es: str, en: str) -> str:
    return es if L == ES else en


def label(item: dict, L: int) -> str:
    return D["data_labels"][item["data"]][L]


def all_items() -> list[dict]:
    return [p for c in D["categories"] for p in c["items"]]


# ----------------------------------------------------------------------------- README

def badge(text: str, logo: str, style: str = "flat-square") -> str:
    url = f"https://img.shields.io/badge/{quote(text).replace('-', '--')}-0D1117?style={style}"
    if logo:
        url += f"&logo={logo}&logoColor=00FF66"
    return f'<img src="{url}" alt="{html.escape(text)}">'


def md_tags(tags) -> str:
    return " ".join(f"`{x}`" for x in tags)


def b_to_md(s: str) -> str:
    return re.sub(r"</?b>", "**", s)


def readme(L: int) -> str:
    p = D["profile"]
    switch = [f"**Español** · [English]({GH}Rxyxs/blob/main/README.en.md)",
              f"[Español]({GH[:-1]}) · **English**"][L]
    out = [switch, "", f"![{t(L, 'Portada', 'Banner')}](assets/banner.png)", "", '<div align="center">', "",
           f"# {p['name']}", "", f"**{p['role'][L]}**", "",
           f'<a href="{p["site"]}">{badge(t(L, "Portafolio", "Portfolio"), "githubpages", "for-the-badge")}</a>',
           f'<a href="{p["linkedin"]}">{badge("LinkedIn", "linkedin", "for-the-badge")}</a>',
           f'<a href="mailto:{p["email"]}">{badge("Email", "gmail", "for-the-badge")}</a>',
           "", "</div>", "", "---", "", "\n\n".join(p["intro"][L]), ""]

    # Destacados en tarjetas 2x2
    out += [f"## {t(L, 'Proyectos destacados', 'Featured projects')}", "", "<table>"]
    feats = D["featured"]
    for i in range(0, len(feats), 2):
        out.append("<tr>")
        for f in feats[i:i + 2]:
            extra = f' · <a href="{PAGE}{f["repo"]}/">{t(L, "página", "page")}</a>' if f["page"] else ""
            out += ['<td width="50%" valign="top">', f'<h3><a href="{GH}{f["repo"]}">{f["name"][L]}</a></h3>',
                    f"<sub>{label(f, L)}{extra}</sub>", f"<p>{f['res'][L]}</p>",
                    " ".join(f"<code>{x}</code>" for x in f["tags"]), "</td>"]
        out.append("</tr>")
    out += ["</table>", ""]

    lib = D["library"]
    out += [f"## {t(L, 'Herramienta abierta', 'Open-source tool')}", "",
            f"**[{lib['name'][L]}]({GH}{lib['repo']})**  ", lib["res"][L], "",
            "```python", lib["code"], "```", ""]

    w = D["work"]
    out += [f"## {t(L, 'Experiencia', 'Experience')}", "",
            f"**[{w['name'][L]}]({GH}{w['repo']})** · <sub>{label(w, L)}</sub>  ", w["res"][L] + "  ", md_tags(w["tags"]), ""]

    cats = D["categories"]
    out += [f"## {t(L, 'Proyectos por tipo de problema', 'Projects by kind of problem')}", "",
            t(L, f"{len(all_items())} proyectos en {len(cats)} tipos de problema; haz clic en una categoría para abrirla, "
                 f"o míralos todos en el [portafolio]({p['site']}).",
                 f"{len(all_items())} projects across {len(cats)} kinds of problem; click a category to open it, "
                 f"or see them all in the [portfolio]({p['site']}en/)."), ""]
    for i, c in enumerate(cats, 1):
        out += ["<details>", f"<summary><b>{i}. {c['name'][L]}</b> · {len(c['items'])} {t(L, 'proyectos', 'projects')}</summary>", "",
                f"| {t(L, 'Proyecto', 'Project')} | {t(L, 'Qué resuelve y qué encontró', 'What it solves and what it found')} | Stack |",
                "|---|---|---|"]
        for it in c["items"]:
            pg = f" · [{t(L, 'página', 'page')}]({PAGE}{it['repo']}/)" if it["page"] else ""
            out.append(f"| **[{it['name'][L]}]({GH}{it['repo']})**<br><sub>{label(it, L)}{pg}</sub> | {b_to_md(it['res'][L])} | {md_tags(it['tags'])} |")
        out += ["", "</details>", ""]

    out += [f"## {t(L, 'Herramientas', 'Tools')}", "", "<table>"]
    for g in D["tools"]:
        out.append(f"<tr><td><b>{g['group'][L]}</b></td><td>{' '.join(badge(x['label'], x['logo']) for x in g['items'])}</td></tr>")
    out += ["</table>", "", "---", "", '<div align="center">',
            f'<sub><a href="{p["site"]}">{t(L, "Portafolio", "Portfolio")}</a> · <a href="{p["linkedin"]}">LinkedIn</a> · '
            f'{p["email"]} · Santiago, Chile</sub>', "</div>", ""]
    return "\n".join(out)


# ----------------------------------------------------------------------------- sitio

CSS = """
:root{--bg:#FBFAF8;--surface:#FFFFFF;--ink:#23201D;--muted:#6B645D;--line:#E3DED7;--accent:#1F5A96;--green:#1a7f37}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#171614;--surface:#201E1B;--ink:#EDE9E3;--muted:#A9A29A;--line:#322E2A;--accent:#6FA8DC;--green:#7FAE6B}}
:root[data-theme="dark"]{--bg:#171614;--surface:#201E1B;--ink:#EDE9E3;--muted:#A9A29A;--line:#322E2A;--accent:#6FA8DC;--green:#7FAE6B}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
.wrap{max-width:1040px;margin:0 auto;padding:0 16px 80px}
header{padding:56px 0 32px;border-bottom:1px solid var(--line);margin-bottom:8px}
.lang{float:right;font-size:.85rem;color:var(--muted)}
.lang a{color:var(--muted)}
h1{font-size:clamp(2rem,6vw,2.8rem);line-height:1.1;margin:0 0 6px;letter-spacing:-.02em}
.role{color:var(--muted);margin:0 0 22px;font-size:1.05rem}
.intro p{max-width:72ch;margin:0 0 14px}
.links a{display:inline-block;margin:6px 8px 0 0;padding:8px 14px;border:1px solid var(--line);border-radius:7px;text-decoration:none;color:var(--ink);background:var(--surface);font-size:.9rem}
.links a:hover{border-color:var(--accent)}
h2{font-size:1.35rem;margin:48px 0 6px;letter-spacing:-.01em}
.sub{color:var(--muted);margin:0 0 18px;font-size:.95rem}
nav.toc{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 0}
nav.toc a{font-size:.82rem;padding:4px 10px;border:1px solid var(--line);border-radius:999px;text-decoration:none;color:var(--muted);background:var(--surface)}
nav.toc a:hover{color:var(--ink);border-color:var(--accent)}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(min(300px,100%),1fr))}
.one{grid-template-columns:minmax(0,1fr)}
.feat{grid-template-columns:repeat(auto-fill,minmax(min(440px,100%),1fr))}
@media (max-width:520px){.feat,.grid{grid-template-columns:minmax(0,1fr)}.lang{float:none;margin-bottom:8px}}
.card{min-width:0;overflow-wrap:anywhere;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:16px 18px;display:flex;flex-direction:column}
.card img{width:100%;aspect-ratio:16/8;object-fit:cover;object-position:top;border-radius:6px;border:1px solid var(--line);background:#fff;margin-bottom:12px}
.card h3{font-size:1.02rem;margin:0 0 2px;line-height:1.3}
.card h3 a{color:var(--ink);text-decoration:none}
.card h3 a:hover{color:var(--accent)}
.data{font-size:.78rem;color:var(--muted);margin-bottom:8px}
.card p{margin:0 0 12px;font-size:.92rem;flex:1}
.tags{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:10px}
.tags code{font-size:.74rem;padding:2px 7px;border-radius:999px;background:rgba(31,90,150,.08);color:var(--accent);font-family:ui-monospace,SFMono-Regular,Consolas,monospace}
.actions{font-size:.85rem;display:flex;gap:14px}
.lib{border-left:3px solid var(--green)}
pre{background:var(--bg);border:1px solid var(--line);border-radius:7px;padding:12px 14px;overflow-x:auto;font-size:.85rem;margin:4px 0 12px}
h2.cat{font-size:1.12rem;margin:36px 0 12px;padding-top:12px;border-top:1px solid var(--line)}
h2.cat .n{color:var(--accent);margin-right:6px}
.tools{display:flex;flex-wrap:wrap;gap:6px}
.tools span{font-size:.82rem;padding:4px 10px;border:1px solid var(--line);border-radius:6px;background:var(--surface)}
.tools b{display:block;width:100%;font-size:.8rem;color:var(--muted);font-weight:600;margin:10px 0 2px}
footer{margin-top:56px;padding-top:20px;border-top:1px solid var(--line);color:var(--muted);font-size:.85rem}
"""


def h(s: str) -> str:
    """Escapa texto pero conserva las negritas <b> de los resultados."""
    return html.escape(s).replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>")


def md_inline(s: str) -> str:
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", h(s))


def card(it: dict, L: int, cls: str = "", img: bool = False) -> str:
    acts = []
    if it.get("page"):
        acts.append(f'<a href="{PAGE}{it["repo"]}/">{t(L, "Ver página", "View page")}</a>')
    acts.append(f'<a href="{GH}{it["repo"]}">{t(L, "Código", "Code")}</a>')
    pic = (f'<img src="{PAGE}{it["repo"]}/{it["img"]}" alt="" loading="lazy">' if img and it.get("img") else "")
    tags = "".join(f"<code>{html.escape(x)}</code>" for x in it["tags"])
    return (f'<article class="card {cls}">{pic}<h3><a href="{GH}{it["repo"]}">{h(it["name"][L])}</a></h3>'
            f'<div class="data">{h(label(it, L))}</div><p>{h(it["res"][L])}</p>'
            f'<div class="tags">{tags}</div><div class="actions">{"".join(acts)}</div></article>')


def site(L: int) -> str:
    p, cats, lib, w = D["profile"], D["categories"], D["library"], D["work"]
    other = t(L, '<a href="en/">English</a>', '<a href="../">Español</a>')
    intro = "".join(f"<p>{md_inline(x)}</p>" for x in p["intro"][L])
    toc = "".join(f'<a href="#c{i}">{h(c["name"][L])}</a>' for i, c in enumerate(cats, 1))
    body = [f'<header><div class="lang">{other}</div><h1>{h(p["name"])}</h1><p class="role">{h(p["role"][L])}</p>',
            f'<div class="intro">{intro}</div><div class="links">',
            f'<a href="{p["github"]}">GitHub</a><a href="{p["linkedin"]}">LinkedIn</a>',
            f'<a href="mailto:{p["email"]}">{p["email"]}</a><a href="{GH}{lib["repo"]}">datoschile</a></div></header>',
            f'<h2>{t(L, "Proyectos destacados", "Featured projects")}</h2>',
            f'<p class="sub">{t(L, "Cuatro proyectos con datos reales y un hallazgo que no era el esperado.", "Four projects on real data with a finding that was not the expected one.")}</p>',
            '<div class="grid feat">' + "".join(card(f, L, img=True) for f in D["featured"]) + "</div>",
            f'<h2>{t(L, "Herramienta abierta", "Open-source tool")}</h2>',
            f'<article class="card lib"><h3><a href="{GH}{lib["repo"]}">{h(lib["name"][L])}</a></h3>'
            f'<p>{h(lib["res"][L])}</p><pre><code>{html.escape(lib["code"])}</code></pre>'
            f'<div class="tags">{"".join(f"<code>{x}</code>" for x in lib["tags"])}</div>'
            f'<div class="actions"><a href="{GH}{lib["repo"]}">{t(L, "Código e instalación", "Code and install")}</a></div></article>',
            f'<h2>{t(L, "Experiencia", "Experience")}</h2>',
            '<div class="grid one">' + card(w, L) + "</div>",
            f'<h2>{t(L, "Proyectos por tipo de problema", "Projects by kind of problem")}</h2>',
            f'<p class="sub">{t(L, f"{len(all_items())} proyectos. Cada uno indica si usa datos reales o simulados.", f"{len(all_items())} projects. Each states whether it uses real or simulated data.")}</p>',
            f'<nav class="toc">{toc}</nav>']
    for i, c in enumerate(cats, 1):
        body.append(f'<h2 class="cat" id="c{i}"><span class="n">{i}.</span>{h(c["name"][L])}</h2>')
        body.append('<div class="grid">' + "".join(card(it, L) for it in c["items"]) + "</div>")
    tools = "".join(f"<b>{h(g['group'][L])}</b>" + "".join(f"<span>{h(x['label'])}</span>" for x in g["items"]) for g in D["tools"])
    body += [f'<h2>{t(L, "Herramientas", "Tools")}</h2><div class="tools">{tools}</div>',
             f'<footer>{h(p["name"])} · {h(p["role"][L])} · <a href="{p["github"]}">GitHub</a> · '
             f'<a href="{p["linkedin"]}">LinkedIn</a></footer>']
    desc = t(L, "Portafolio de ciencia de datos de Pablo Reyes: proyectos ordenados por el tipo de problema que resuelven.",
             "Data science portfolio of Pablo Reyes: projects organized by the kind of problem they solve.")
    lang = t(L, "es", "en")
    return (f'<!doctype html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>Pablo Reyes · {t(L, "Ciencia de datos", "Data science")}</title>\n'
            f'<meta name="description" content="{desc}">\n'
            f'<link rel="alternate" hreflang="es" href="{PAGE}"><link rel="alternate" hreflang="en" href="{PAGE}en/">\n'
            f"<style>{CSS}</style>\n</head>\n<body>\n<div class=\"wrap\">\n" + "\n".join(body) + "\n</div>\n</body>\n</html>\n")



def escribir(ruta: Path, texto: str) -> None:
    """Siempre con saltos de línea LF, también en Windows."""
    ruta.write_text(texto, encoding="utf-8", newline="\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", type=Path, help="carpeta del repositorio Rxyxs.github.io")
    a = ap.parse_args()
    escribir(ROOT / "README.md", readme(ES))
    escribir(ROOT / "README.en.md", readme(EN))
    print(f"README.md, README.en.md: {len(all_items())} proyectos")
    if a.site:
        (a.site / "en").mkdir(parents=True, exist_ok=True)
        escribir(a.site / "index.html", site(ES))
        escribir(a.site / "en" / "index.html", site(EN))
        escribir(a.site / ".nojekyll", "")
        print(f"sitio -> {a.site}")


if __name__ == "__main__":
    main()
