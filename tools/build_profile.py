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
:root{--bg:#FFFFFF;--bg2:#F6F8FA;--surface:#FFFFFF;--surface2:#F1F4F7;--ink:#1A1D21;--body:#3D434B;--muted:#5F6670;
--line:#E4E7EB;--hover:#C9D1D9;--accent:#0F766E;--accent-hover:#0D5F59;--accent-ink:#FFFFFF;--tag:#3D434B;--nav:rgba(255,255,255,.9);--real:#1A7F37;--sim:#9A6700;--mix:#0969DA}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0D1117;--bg2:#0D1117;--surface:#161B22;--surface2:#21262D;--ink:#E6EDF3;--body:#C9D1D9;--muted:#8B949E;--line:#30363D;--hover:#484F58;--accent:#3FB950;--accent-hover:#56D364;--accent-ink:#0D1117;--tag:#C9D1D9;--nav:rgba(13,17,23,.9);--real:#3FB950;--sim:#D29922;--mix:#58A6FF}}
:root[data-theme="dark"]{--bg:#0D1117;--bg2:#0D1117;--surface:#161B22;--surface2:#21262D;--ink:#E6EDF3;--body:#C9D1D9;--muted:#8B949E;--line:#30363D;--hover:#484F58;--accent:#3FB950;--accent-hover:#56D364;--accent-ink:#0D1117;--tag:#C9D1D9;--nav:rgba(13,17,23,.9);--real:#3FB950;--sim:#D29922;--mix:#58A6FF}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:72px}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
.top{position:sticky;top:0;z-index:10;background:var(--nav);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.top .in{max-width:1080px;margin:0 auto;padding:0 16px;height:56px;display:flex;align-items:center;gap:24px}
.brand{font-weight:700;color:var(--ink);text-decoration:none;letter-spacing:-.01em;white-space:nowrap}
.top nav{display:flex;gap:20px;overflow-x:auto;flex:1;scrollbar-width:none}
.top nav a{color:var(--muted);text-decoration:none;font-size:.88rem;white-space:nowrap}
.top nav a:hover{color:var(--ink)}
.lang a{font-size:.82rem;color:var(--muted);border:1px solid var(--line);border-radius:6px;padding:4px 10px;text-decoration:none}
.lang a:hover{color:var(--ink);border-color:var(--accent)}
.wrap{max-width:1080px;margin:0 auto;padding:0 16px 80px}
.hero{padding:64px 0 44px;border-bottom:1px solid var(--line)}
.eyebrow{font-size:.78rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin:0 0 10px}
h1{font-size:clamp(2.2rem,6vw,3.2rem);line-height:1.08;margin:0 0 8px;letter-spacing:-.025em}
.role{color:var(--muted);margin:0 0 24px;font-size:1.08rem}
.intro p{max-width:70ch;margin:0 0 14px;color:var(--body)}
.intro strong{color:var(--ink)}
.links{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
.links a{padding:10px 16px;border:1px solid var(--line);border-radius:8px;text-decoration:none;color:var(--ink);background:var(--surface);font-size:.9rem;font-weight:500;transition:border-color .15s,background .15s}
.links a:hover{border-color:var(--accent)}
.links a.primary{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.links a.primary:hover{background:var(--accent-hover);border-color:var(--accent-hover)}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-top:36px}
.stat{background:var(--bg2);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.stat b{display:block;font-size:1.7rem;line-height:1.15;font-variant-numeric:tabular-nums;letter-spacing:-.02em}
.stat span{font-size:.82rem;color:var(--muted)}
h2{font-size:1.45rem;margin:56px 0 6px;letter-spacing:-.015em}
.sub{color:var(--muted);margin:0 0 20px;font-size:.95rem}
nav.toc{display:flex;flex-wrap:wrap;gap:6px}
nav.toc a{font-size:.82rem;padding:5px 11px;border:1px solid var(--line);border-radius:999px;text-decoration:none;color:var(--muted);background:var(--surface)}
nav.toc a:hover{color:var(--ink);border-color:var(--accent)}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(min(300px,100%),1fr))}
.one{grid-template-columns:minmax(0,1fr)}
.feat{grid-template-columns:repeat(auto-fill,minmax(min(460px,100%),1fr))}
@media (max-width:640px){.feat,.grid{grid-template-columns:minmax(0,1fr)}.top nav{display:none}.top .in{justify-content:space-between}}
.card{min-width:0;overflow-wrap:anywhere;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:18px 20px;display:flex;flex-direction:column;transition:border-color .15s,transform .15s}
.card:hover{border-color:var(--hover);transform:translateY(-2px)}
.card img{width:100%;aspect-ratio:16/8;object-fit:cover;object-position:top;border-radius:8px;background:#fff;margin-bottom:14px}
.card img.contain{object-fit:contain}
.card h3{font-size:1.04rem;margin:0 0 8px;line-height:1.3}
.card h3 a{color:var(--ink);text-decoration:none}
.card h3 a:hover{color:var(--accent)}
.data{align-self:flex-start;font-size:.72rem;font-weight:600;padding:2px 9px;border-radius:999px;margin-bottom:10px;border:1px solid}
.data.real{color:var(--real);border-color:color-mix(in srgb,var(--real) 40%,transparent);background:color-mix(in srgb,var(--real) 8%,transparent)}
.data.sim{color:var(--sim);border-color:color-mix(in srgb,var(--sim) 40%,transparent);background:color-mix(in srgb,var(--sim) 8%,transparent)}
.data.mix{color:var(--mix);border-color:color-mix(in srgb,var(--mix) 40%,transparent);background:color-mix(in srgb,var(--mix) 8%,transparent)}
.card p{margin:0 0 14px;font-size:.92rem;color:var(--body);flex:1}
.card p b{color:var(--ink)}
.tags{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:12px}
.tags code{font-size:.72rem;padding:2px 8px;border-radius:5px;background:var(--surface2);color:var(--tag);font-family:ui-monospace,SFMono-Regular,Consolas,monospace}
.actions{font-size:.86rem;display:flex;gap:16px;padding-top:12px;border-top:1px solid var(--line)}
.actions a{text-decoration:none;font-weight:500}
.actions a:hover{text-decoration:underline}
.lib{border-left:3px solid var(--real)}
pre{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:12px 14px;overflow-x:auto;font-size:.85rem;margin:4px 0 12px;color:var(--body)}
h2.cat{font-size:1.1rem;margin:40px 0 14px;padding-top:16px;border-top:1px solid var(--line)}
h2.cat .n{color:var(--accent);margin-right:8px;font-variant-numeric:tabular-nums}
.tools{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(min(300px,100%),1fr))}
.tools div{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.tools b{display:block;font-size:.76rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600;margin:0 0 8px}
.tools span{display:inline-block;font-size:.82rem;padding:3px 9px;margin:0 5px 6px 0;border:1px solid var(--line);border-radius:6px;background:var(--bg2)}
footer{margin-top:64px;padding-top:22px;border-top:1px solid var(--line);color:var(--muted);font-size:.85rem;display:flex;flex-wrap:wrap;gap:8px 16px;justify-content:space-between}
footer a{color:var(--muted)}
"""


def h(s: str) -> str:
    """Escapa texto pero conserva las negritas <b> de los resultados."""
    return html.escape(s).replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>")


def md_inline(s: str) -> str:
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", h(s))


def kind(it: dict) -> str:
    """Color de la etiqueta de datos: real, simulado o mezcla de ambos."""
    if it["data"] in ("real", "coco"):
        return "real"
    if it["data"] in ("sim", "mc", "model"):
        return "sim"
    return "mix"


def card(it: dict, L: int, cls: str = "", img: bool = False) -> str:
    acts = []
    if it.get("page"):
        acts.append(f'<a href="{PAGE}{it["repo"]}/">{t(L, "Ver página", "View page")}</a>')
    acts.append(f'<a href="{GH}{it["repo"]}">{t(L, "Código", "Code")}</a>')
    # "img_fit": "contain" muestra el gráfico entero en vez de recortarlo al formato de la tarjeta.
    fit = ' class="contain"' if it.get("img_fit") == "contain" else ""
    pic = (f'<img src="{PAGE}{it["repo"]}/{it["img"]}" alt="" loading="lazy"{fit}>' if img and it.get("img") else "")
    tags = "".join(f"<code>{html.escape(x)}</code>" for x in it["tags"])
    return (f'<article class="card {cls}">{pic}<h3><a href="{GH}{it["repo"]}">{h(it["name"][L])}</a></h3>'
            f'<div class="data {kind(it)}">{h(label(it, L))}</div><p>{h(it["res"][L])}</p>'
            f'<div class="tags">{tags}</div><div class="actions">{"".join(acts)}</div></article>')


def site(L: int) -> str:
    p, cats, lib, w = D["profile"], D["categories"], D["library"], D["work"]
    other = t(L, '<a href="en/">English</a>', '<a href="../">Español</a>')
    intro = "".join(f"<p>{md_inline(x)}</p>" for x in p["intro"][L])
    toc = "".join(f'<a href="#c{i}">{h(c["name"][L])}</a>' for i, c in enumerate(cats, 1))
    items = all_items()
    stats = [(len(items), t(L, "proyectos publicados", "published projects")),
             (len(cats), t(L, "tipos de problema", "kinds of problem")),
             (sum(kind(it) == "real" for it in items), t(L, "con datos reales", "on real data")),
             (sum(bool(it.get("page")) for it in items), t(L, "con página de resultados", "with a results page"))]
    menu = [("destacados", t(L, "Destacados", "Featured")), ("herramienta", t(L, "Herramienta", "Tool")),
            ("experiencia", t(L, "Experiencia", "Experience")), ("proyectos", t(L, "Proyectos", "Projects")),
            ("stack", "Stack")]
    body = ['<div class="top"><div class="in">'
            f'<a class="brand" href="#">{h(p["name"])}</a>'
            '<nav>' + "".join(f'<a href="#{k}">{v}</a>' for k, v in menu) + '</nav>'
            f'<div class="lang">{other}</div></div></div><div class="wrap">',
            f'<header class="hero"><p class="eyebrow">Data Scientist</p><h1>{h(p["name"])}</h1>'
            f'<p class="role">{h(p["role"][L])}</p>',
            f'<div class="intro">{intro}</div><div class="links">',
            f'<a class="primary" href="{p["github"]}">GitHub</a><a href="{p["linkedin"]}">LinkedIn</a>',
            f'<a href="mailto:{p["email"]}">{p["email"]}</a><a href="{GH}{lib["repo"]}">datoschile</a></div>',
            '<div class="stats">' + "".join(f'<div class="stat"><b>{n}</b><span>{s}</span></div>' for n, s in stats)
            + "</div></header>",
            f'<h2 id="destacados">{t(L, "Proyectos destacados", "Featured projects")}</h2>',
            f'<p class="sub">{t(L, "Cuatro proyectos con datos reales y un hallazgo que no era el esperado.", "Four projects on real data with a finding that was not the expected one.")}</p>',
            '<div class="grid feat">' + "".join(card(f, L, img=True) for f in D["featured"]) + "</div>",
            f'<h2 id="herramienta">{t(L, "Herramienta abierta", "Open-source tool")}</h2>',
            f'<article class="card lib"><h3><a href="{GH}{lib["repo"]}">{h(lib["name"][L])}</a></h3>'
            f'<p>{h(lib["res"][L])}</p><pre><code>{html.escape(lib["code"])}</code></pre>'
            f'<div class="tags">{"".join(f"<code>{x}</code>" for x in lib["tags"])}</div>'
            f'<div class="actions"><a href="{GH}{lib["repo"]}">{t(L, "Código e instalación", "Code and install")}</a></div></article>',
            f'<h2 id="experiencia">{t(L, "Experiencia", "Experience")}</h2>',
            '<div class="grid one">' + card(w, L) + "</div>",
            f'<h2 id="proyectos">{t(L, "Proyectos por tipo de problema", "Projects by kind of problem")}</h2>',
            f'<p class="sub">{t(L, f"{len(items)} proyectos. Cada uno indica si usa datos reales o simulados.", f"{len(items)} projects. Each states whether it uses real or simulated data.")}</p>',
            f'<nav class="toc">{toc}</nav>']
    for i, c in enumerate(cats, 1):
        body.append(f'<h2 class="cat" id="c{i}"><span class="n">{i}.</span>{h(c["name"][L])}</h2>')
        body.append('<div class="grid">' + "".join(card(it, L) for it in c["items"]) + "</div>")
    tools = "".join(f"<div><b>{h(g['group'][L])}</b>" + "".join(f"<span>{h(x['label'])}</span>" for x in g["items"])
                    + "</div>" for g in D["tools"])
    body += [f'<h2 id="stack">{t(L, "Herramientas", "Tools")}</h2><div class="tools">{tools}</div>',
             f'<footer><span>{h(p["name"])} · {h(p["role"][L])}</span><span><a href="{p["github"]}">GitHub</a> · '
             f'<a href="{p["linkedin"]}">LinkedIn</a> · <a href="mailto:{p["email"]}">{p["email"]}</a></span></footer>']
    desc = t(L, "Portafolio de ciencia de datos de Pablo Reyes: proyectos ordenados por el tipo de problema que resuelven.",
             "Data science portfolio of Pablo Reyes: projects organized by the kind of problem they solve.")
    lang = t(L, "es", "en")
    return (f'<!doctype html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>Pablo Reyes · {t(L, "Ciencia de datos", "Data science")}</title>\n'
            f'<meta name="description" content="{desc}">\n'
            f'<link rel="alternate" hreflang="es" href="{PAGE}"><link rel="alternate" hreflang="en" href="{PAGE}en/">\n'
            '<meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)">'
            '<meta name="theme-color" content="#0D1117" media="(prefers-color-scheme: dark)">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
            f"<style>{CSS}</style>\n</head>\n<body>\n" + "\n".join(body) + "\n</div>\n</body>\n</html>\n")



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
