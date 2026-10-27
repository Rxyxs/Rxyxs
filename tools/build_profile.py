"""Genera el README del perfil (español e inglés) y el sitio rxyxs.github.io desde perfil.json.

    python tools/build_profile.py                         # README.md y README.en.md
    python tools/build_profile.py --site ../Rxyxs.github.io   # además, el sitio
    python tools/galerias.py                              # antes, si cambiaron las figuras de un proyecto

Los proyectos, sus resultados y sus etiquetas viven solo en ``tools/perfil.json``: el README y
el sitio se generan desde ahí para que nunca digan cosas distintas. Para agregar o corregir un
proyecto se edita el JSON y se vuelve a correr este script.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
GH = "https://github.com/Rxyxs/"
PAGE = "https://rxyxs.github.io/"

D = json.loads((ROOT / "tools" / "perfil.json").read_text(encoding="utf-8"))
# Generados aparte para no reescribir perfil.json: la primera figura de la página de cada
# proyecto (miniaturas.json) y los sectores que alimentan los filtros del sitio (sectores.json).
THUMBS = json.loads((ROOT / "tools" / "miniaturas.json").read_text(encoding="utf-8"))
# Las figuras de la galería de cada tarjeta, con la miniatura primero (tools/galerias.py).
GAL = json.loads((ROOT / "tools" / "galerias.json").read_text(encoding="utf-8"))
# Qué repositorios tienen página de resultados, para las tarjetas que no lo declaran (Simulado vs. real).
PAGES = {p["repo"]: p.get("page") for p in [p for c in D["categories"] for p in c["items"]] + D["featured"]}
SECT = json.loads((ROOT / "tools" / "sectores.json").read_text(encoding="utf-8"))
SITE: Path | None = None  # carpeta del sitio, para versionar sus imágenes (main)
ICONS: set[str] = set()  # logos disponibles en <sitio>/assets/icons, se llena en main()
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
    out = [switch, "", f"![{t(L, 'Portada', 'Banner')}](assets/banner.gif)", "", '<div align="center">', "",
           f"# {p['name']}", "", f"**{p['role'][L]}**", "",
           f'<a href="{p["site"]}">{badge(t(L, "Portafolio", "Portfolio"), "githubpages", "for-the-badge")}</a>',
           f'<a href="{p["linkedin"]}">{badge("LinkedIn", "linkedin", "for-the-badge")}</a>',
           *([f'<a href="{PAGE}{p["cv"][L]}">{badge("CV", "adobeacrobatreader", "for-the-badge")}</a>']
             if p.get("cv") else []),
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

    rv = D["real_vs_sim"]
    out += [f"## {rv['title'][L]}", "", rv["intro"][L], "",
            "| " + " | ".join(rv["head"][L]) + " |", "|---|---|---|---|"]
    for r in rv["rows"]:
        out.append(f"| **[{r['name'][L]}]({GH}{r['repo']})**<br><sub>{r['data'][L]}</sub> | {r['metric'][L]} | "
                   f"{r['sim'][L]} → **{r['real'][L]}** | {r['why'][L]} |")
    out.append("")

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

    w = D["work"]
    out += [f"## {t(L, 'Experiencia', 'Experience')}", "",
            f"**[{w['name'][L]}]({GH}{w['repo']})** · <sub>{label(w, L)}</sub>  ", w["res"][L] + "  ", md_tags(w["tags"]), ""]

    lib = D["library"]
    out += [f"## {t(L, 'Herramienta pública', 'Open-source tool')}", "",
            f"**[{lib['name'][L]}]({GH}{lib['repo']})**  ", lib["res"][L], "",
            "```python", lib["code"], "```", ""]
    if lib.get("page"):
        out += [f"[{t(L, 'Ver el panel interactivo', 'Open the interactive dashboard')}]({PAGE}{lib['repo']}/)", ""]

    out += ["## Stack", "", "<table>"]
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
.gal{position:relative;margin:-6px -8px 14px;aspect-ratio:16/10;border-radius:8px;overflow:hidden;background:#fff;box-shadow:inset 0 0 0 1px var(--line)}
.feat .gal{aspect-ratio:16/9}
.two{grid-template-columns:repeat(auto-fit,minmax(min(380px,100%),1fr))}
.gal.pic{aspect-ratio:4/5;background:var(--bg2)}
.gal.oscura{background:#0d1117}.gal.oscura .frames img{padding:0}
.gal.pic .frames img{object-fit:cover;object-position:50% 45%;padding:0;transform:none}
.data.org{color:var(--muted);border-color:var(--line);background:var(--bg2)}
.facts{display:grid;grid-template-columns:auto minmax(0,1fr);gap:10px 14px;margin:0 0 14px;align-items:start}
.facts dt{font-size:.72rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding-top:5px;white-space:nowrap}
.facts dd{margin:0;display:flex;flex-wrap:wrap;gap:6px}
.facts dd span{display:inline-flex;align-items:center;gap:6px;font-size:.8rem;padding:3px 10px;border:1px solid var(--line);border-radius:999px;background:var(--bg2);color:var(--body)}
.facts dd.steps span b{display:grid;place-items:center;width:16px;height:16px;border-radius:50%;background:var(--accent);color:var(--accent-ink);font-size:.66rem}
.xps{display:grid;gap:16px}
.card.xp{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:28px;padding:18px 24px 18px 18px;align-items:stretch}
.xp .gal{margin:0;height:100%;min-height:300px;aspect-ratio:auto}
.card.xp.wide{grid-template-columns:minmax(0,1fr);padding:22px 24px}
.xp.wide .gal{height:auto;min-height:0;aspect-ratio:1200/684;margin:0 0 18px}
.xb{display:flex;flex-direction:column;min-width:0;padding-top:6px}
.xp p.kick{flex:none;margin:0 0 6px;font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--accent)}
.xp h3{font-size:1.18rem;margin:0 0 8px}
.meta{display:flex;flex-wrap:wrap;align-items:center;gap:4px 14px;margin-bottom:14px;font-size:.86rem;color:var(--muted)}
.meta b{color:var(--ink);font-weight:600}.meta .data{margin:0}
.meta span+span::before,.meta b+span::before{content:"·";margin-right:14px;color:var(--line)}
.meta .data::before{content:none}
.xp .xb>p{flex:none;margin:0 0 16px}
.xf{margin-top:auto;flex-wrap:wrap;align-items:center;gap:8px 18px}
.ig{display:inline-flex;align-items:center;gap:7px}.ig svg{width:16px;height:16px}
.xf .note{font-size:.8rem;color:var(--muted)}
.credit{font-size:.75rem;color:var(--muted);margin-left:auto}
@media (max-width:760px){.card.xp{grid-template-columns:minmax(0,1fr);gap:16px;padding:16px}
.xp .gal,.xp.wide .gal{height:auto;min-height:0;aspect-ratio:16/10}.xp .gal.pic{aspect-ratio:1/1}.credit{margin-left:0}}
.frames img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;padding:8px;opacity:0;transform:scale(1.015);transition:opacity .7s ease,transform 4s ease}
.frames img.on{opacity:1;transform:none}
.gal .open{position:absolute;inset:0;width:100%;border:0;padding:0;background:none;cursor:zoom-in}
.gal .open:focus-visible{outline:2px solid var(--accent);outline-offset:-2px;border-radius:8px}
.nav{position:absolute;top:50%;transform:translateY(-50%);width:32px;height:32px;border-radius:50%;border:0;padding:0;background:rgba(13,17,23,.62);color:#fff;cursor:pointer;display:grid;place-items:center;transition:opacity .2s,background .15s}
.nav:hover{background:rgba(13,17,23,.85)}.nav svg{width:16px;height:16px}
.gal .nav{opacity:0}.gal:hover .nav,.gal:focus-within .nav{opacity:1}
@media (hover:none){.gal .nav{display:none}}
.prev{left:8px}.next{right:8px}
.dots{position:absolute;left:0;right:0;bottom:8px;display:flex;justify-content:center;gap:5px;pointer-events:none}
.dots i{width:6px;height:6px;border-radius:3px;background:rgba(13,17,23,.22);transition:width .3s,background .3s}
.dots i.on{width:16px;background:rgba(13,17,23,.72)}
.bar{position:absolute;left:0;right:0;top:0;height:3px;pointer-events:none}
.bar i{display:block;height:100%;background:var(--accent);transform-origin:left;transform:scaleX(0);animation:fill 3.6s linear forwards paused}
@keyframes fill{to{transform:scaleX(1)}}
.gal.run .bar i{animation-play-state:running}
.gal.run:hover .bar i,.gal:focus-within .bar i,.lb-on .gal .bar i{animation-play-state:paused}
.gal .n{position:absolute;right:8px;top:10px;display:flex;align-items:center;gap:4px;font-size:.7rem;font-weight:600;padding:2px 8px;border-radius:999px;background:rgba(13,17,23,.62);color:#fff;pointer-events:none;font-variant-numeric:tabular-nums}
.gal .n svg{width:11px;height:11px}
.lb{border:0;padding:0;margin:auto;width:min(1120px,94vw);max-width:none;max-height:94vh;background:var(--surface);color:var(--ink);border-radius:14px;box-shadow:0 24px 70px rgba(0,0,0,.45);overflow:hidden}
.lb[open]{display:flex;flex-direction:column}
.lb::backdrop{background:rgba(1,4,9,.8);backdrop-filter:blur(3px)}
.lb-top{display:flex;align-items:center;gap:14px;padding:12px 14px 12px 18px;border-bottom:1px solid var(--line)}
.lb-top b{flex:1;min-width:0;font-size:1rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.lb-k{color:var(--muted);font-size:.82rem;font-variant-numeric:tabular-nums;white-space:nowrap}
.lb-top a{font-size:.86rem;font-weight:500;text-decoration:none;white-space:nowrap}.lb-top a:hover{text-decoration:underline}
.lb-x{background:none;border:1px solid var(--line);border-radius:6px;width:32px;height:30px;color:var(--muted);cursor:pointer;display:grid;place-items:center;padding:0}
.lb-x:hover{color:var(--ink);border-color:var(--accent)}.lb-x svg{width:15px;height:15px}
.lb-stage{position:relative;background:#fff;display:grid;place-items:center;min-height:0;touch-action:pan-y}
.lb-stage img{display:block;max-width:100%;height:calc(94vh - 210px);max-height:760px;object-fit:contain;padding:12px}
.lb-cap{margin:0;padding:12px 18px 10px;font-size:.92rem;color:var(--body);min-height:2.4em}
.lb-th{display:flex;gap:8px;padding:2px 18px 16px;overflow-x:auto;scrollbar-width:thin}
.lb-th button{flex:none;width:76px;height:48px;padding:2px;border:2px solid var(--line);border-radius:7px;background:#fff;cursor:pointer;opacity:.55;transition:opacity .15s,border-color .15s}
.lb-th button:hover{opacity:.9}.lb-th button[aria-current="true"]{opacity:1;border-color:var(--accent)}
.lb-th img{width:100%;height:100%;object-fit:contain}
.nav[hidden],.lb-th[hidden],.lb-top a[hidden]{display:none}
@media (max-width:640px){.lb{width:100vw;max-height:100vh;border-radius:0}.lb-stage img{height:auto;max-height:62vh;padding:6px}.lb-top a{display:none}}
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
.rvt{border:1px solid var(--line);border-radius:12px;background:var(--surface);overflow:hidden}
.rv-row{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.8fr) minmax(0,1fr) minmax(0,2fr);gap:16px;padding:14px 18px;border-top:1px solid var(--line);align-items:baseline}
.rv-h{border-top:0;font-size:.74rem;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);padding-top:12px;padding-bottom:10px}
.rv-p a{color:var(--ink);font-weight:600;text-decoration:none}.rv-p a:hover{color:var(--accent)}
.rv-p span{display:block;font-size:.78rem;color:var(--muted);margin-top:2px}
.rv-m{font-size:.85rem;color:var(--muted)}
.rv-v{font-variant-numeric:tabular-nums;display:flex;flex-wrap:wrap;column-gap:8px;row-gap:2px}.rv-v span,.rv-v b{white-space:nowrap}.rv-v .esp{color:var(--muted)}.rv-v .fl{color:var(--muted)}.rv-v b{color:var(--ink)}
.rv-w{color:var(--body);font-size:.92rem}
@media (max-width:760px){.rv-h{display:none}.rv-row{grid-template-columns:1fr;gap:4px}}
pre{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:12px 14px;overflow-x:auto;font-size:.85rem;margin:4px 0 12px;color:var(--body)}
h2.cat{font-size:1.1rem;margin:40px 0 14px;padding-top:16px;border-top:1px solid var(--line)}
h2.cat .n{color:var(--accent);margin-right:8px;font-variant-numeric:tabular-nums}
.tools{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(min(300px,100%),1fr))}
.tools div{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.tools b{display:block;font-size:.76rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600;margin:0 0 8px}
.tools span{display:inline-block;font-size:.82rem;padding:3px 9px;margin:0 5px 6px 0;border:1px solid var(--line);border-radius:6px;background:var(--bg2)}
footer{margin-top:64px;padding-top:22px;border-top:1px solid var(--line);color:var(--muted);font-size:.85rem;display:flex;flex-wrap:wrap;gap:8px 16px;justify-content:space-between}
footer a{color:var(--muted)}
.right{display:flex;align-items:center;gap:8px}
.theme{background:none;border:1px solid var(--line);border-radius:6px;width:30px;height:28px;color:var(--muted);cursor:pointer;display:grid;place-items:center;padding:0}
.theme:hover{color:var(--ink);border-color:var(--accent)}
.theme svg{width:15px;height:15px}
.hero-top{display:flex;align-items:center;gap:24px}
.photo{width:112px;height:112px;border-radius:50%;object-fit:cover;border:3px solid var(--surface);box-shadow:0 0 0 1px var(--line);flex:none}
@media (max-width:640px){.hero-top{flex-direction:column-reverse;align-items:flex-start;gap:16px}.photo{width:88px;height:88px}}
.filters{display:flex;flex-direction:column;gap:10px;margin:18px 0 6px;padding:14px 16px;background:var(--bg2);border:1px solid var(--line);border-radius:12px}
.frow{display:flex;flex-wrap:wrap;align-items:center;gap:6px}
.frow b{font-size:.76rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-right:6px;min-width:64px}
.chip{font:inherit;font-size:.82rem;padding:4px 11px;border:1px solid var(--line);border-radius:999px;background:var(--surface);color:var(--body);cursor:pointer}
.chip:hover{border-color:var(--accent)}
.chip[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.count{font-size:.85rem;color:var(--muted);margin:6px 0 0}
.card[hidden],.catwrap[hidden]{display:none}
.tools span{display:inline-flex;align-items:center;gap:6px}
.ic{width:14px;height:14px;background:currentColor;-webkit-mask:var(--i) center/contain no-repeat;mask:var(--i) center/contain no-repeat;flex:none;opacity:.85}
.reveal{opacity:0;transform:translateY(12px);transition:opacity .5s ease,transform .5s ease}
.reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}.card{transition:none}html{scroll-behavior:auto}
.frames img{transition:none;transform:none}.bar{display:none}}
"""

# Botón de tema, filtros y aparición suave de las tarjetas. Sin dependencias.
JS = """
(function(){
  var root=document.documentElement, btn=document.querySelector('.theme');
  function current(){return root.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}
  if(btn){btn.addEventListener('click',function(){var n=current()==='dark'?'light':'dark';root.dataset.theme=n;
    try{localStorage.setItem('tema',n)}catch(e){}});}
  var sel={sector:'',datos:''}, cards=[].slice.call(document.querySelectorAll('.catwrap .card')),
      count=document.querySelector('.count');
  function apply(){var n=0;
    cards.forEach(function(c){var ok=(!sel.sector||c.dataset.sector.split(' ').indexOf(sel.sector)>=0)&&(!sel.datos||c.dataset.kind===sel.datos);
      c.hidden=!ok; if(ok)n++;});
    [].forEach.call(document.querySelectorAll('.catwrap'),function(w){w.hidden=!w.querySelector('.card:not([hidden])')});
    if(count)count.textContent=count.dataset.tpl.replace('{n}',n);}
  [].forEach.call(document.querySelectorAll('.chip'),function(b){b.addEventListener('click',function(){
    var g=b.dataset.group; sel[g]=b.dataset.value;
    [].forEach.call(document.querySelectorAll('.chip[data-group="'+g+'"]'),function(o){o.setAttribute('aria-pressed',o===b)});
    apply();});});
  apply();
  if('IntersectionObserver' in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -40px 0px'});
    [].forEach.call(document.querySelectorAll(".card,.rv-row:not(.rv-h)"),function(c){c.classList.add('reveal');io.observe(c)});}
})();
// Galerías: las figuras avanzan solas mientras la tarjeta está a la vista (la barra de progreso
// marca el tiempo, así que pasar el mouse la pausa), con flechas, swipe y un visor al hacer clic.
(function(){
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches, root=document.documentElement;
  function load(im){if(im&&!im.getAttribute('src')&&im.dataset.src)im.src=im.dataset.src}
  function src(im){return im.getAttribute('src')||im.dataset.src}
  function swipe(el,fn){var x0=null;
    el.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});
    el.addEventListener('touchend',function(e){if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;x0=null;
      if(Math.abs(dx)>40)fn(dx<0?1:-1)},{passive:true});}
  var lb=document.querySelector('.lb'), cur=null;
  var gals=[].slice.call(document.querySelectorAll('.gal'));
  gals.forEach(function(g,gi){
    var ims=[].slice.call(g.querySelectorAll('.frames img')), n=ims.length, i=0,
        dots=[].slice.call(g.querySelectorAll('.dots i')), bar=g.querySelector('.bar i');
    function timing(){if(!bar)return;bar.style.animation='none';void bar.offsetWidth;bar.style.animation='';
      bar.style.animationDuration=(/\\.gif$/i.test(src(ims[i]))?7:3.6)+'s'}
    g.go=function(k){if(n<2)return;ims[i].classList.remove('on');if(dots[i])dots[i].classList.remove('on');
      i=(k+n)%n;load(ims[i]);ims[i].classList.add('on');if(dots[i])dots[i].classList.add('on');
      load(ims[(i+1)%n]);timing()};
    g.at=function(){return i};
    g.figs=function(){return ims.map(function(im){return {src:src(im),cap:im.alt}})};
    if(bar){bar.addEventListener('animationend',function(){g.go(i+1)});
      bar.style.animationDelay=(gi%3)*0.9+'s';}
    [].forEach.call(g.querySelectorAll('.nav'),function(b){b.addEventListener('click',function(){
      g.go(i+(b.classList.contains('next')?1:-1))})});
    g.querySelector('.open').addEventListener('click',function(){show(g,i)});
    swipe(g,function(d){g.go(i+d)});
  });
  if(!reduce&&'IntersectionObserver' in window){
    var vis=new IntersectionObserver(function(es){es.forEach(function(e){var g=e.target;
      g.classList.toggle('run',e.isIntersecting);
      if(e.isIntersecting){var ims=g.querySelectorAll('.frames img');load(ims[1])}})},{threshold:.55});
    gals.forEach(function(g){if(g.querySelector('.bar'))vis.observe(g)});}
  if(!lb||!lb.showModal)return;
  var img=lb.querySelector('.lb-stage img'), cap=lb.querySelector('.lb-cap'), k=lb.querySelector('.lb-k'),
      ttl=lb.querySelector('.lb-top b'), link=lb.querySelector('.lb-top a'), th=lb.querySelector('.lb-th'), figs=[], j=0;
  function paint(){var f=figs[j];img.src=f.src;img.alt=f.cap;cap.textContent=f.cap;
    k.textContent=(j+1)+' / '+figs.length;
    [].forEach.call(th.children,function(b,x){b.setAttribute('aria-current',x===j);if(x===j)b.scrollIntoView({block:'nearest',inline:'nearest'})});
    if(figs.length>1)new Image().src=figs[(j+1)%figs.length].src;}
  function step(d){if(figs.length<2)return;j=(j+d+figs.length)%figs.length;paint()}
  function show(g,i){cur=g;figs=g.figs();j=i;ttl.textContent=g.dataset.title;link.href=g.dataset.href;link.hidden=!g.dataset.href;link.textContent=g.dataset.go+' ↗';
    th.innerHTML='';th.hidden=figs.length<2;
    figs.forEach(function(f,x){var b=document.createElement('button');b.type='button';b.setAttribute('aria-label',f.cap);
      var t=document.createElement('img');t.src=f.src;t.alt='';t.loading='lazy';b.appendChild(t);
      b.addEventListener('click',function(){j=x;paint()});th.appendChild(b)});
    [].forEach.call(lb.querySelectorAll('.nav'),function(b){b.hidden=figs.length<2});
    root.classList.add('lb-on');lb.showModal();paint();}
  lb.querySelector('.prev').addEventListener('click',function(){step(-1)});
  lb.querySelector('.next').addEventListener('click',function(){step(1)});
  lb.querySelector('.lb-x').addEventListener('click',function(){lb.close()});
  lb.addEventListener('click',function(e){if(e.target===lb)lb.close()});
  lb.addEventListener('keydown',function(e){if(e.key==='ArrowRight')step(1);else if(e.key==='ArrowLeft')step(-1)});
  lb.addEventListener('close',function(){root.classList.remove('lb-on');
    if(cur){if(cur.at()!==j)cur.go(j);cur.querySelector('.open').focus({preventScroll:true})}});
  swipe(lb.querySelector('.lb-stage'),step);
})();
"""

ARROW_L = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>'
ARROW_R = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg>'
EXPAND = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true">'
          '<path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>')
CLOSE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg>'

# Se ejecuta antes de pintar la página para no mostrar un destello del tema equivocado.
THEME_BOOT = "try{var t=localStorage.getItem('tema');if(t)document.documentElement.dataset.theme=t}catch(e){}"

SUN_MOON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
            '<path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9z"/></svg>')


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


def bust(src: str) -> str:
    """Agrega ?v=<hash> a las imágenes que viven en el sitio: GitHub Pages las cachea 10 minutos
    y el navegador seguía mostrando el diagrama anterior después de publicar uno nuevo."""
    rel = src.removeprefix(PAGE).removeprefix("../")
    if SITE is None or "://" in rel or not rel.startswith("assets/") or not (SITE / rel).is_file():
        return src
    return f"{src}?v={hashlib.sha1((SITE / rel).read_bytes()).hexdigest()[:8]}"


def gallery(it: dict, L: int, figs: list | None = None, cls: str = "") -> str:
    """Figuras del proyecto que rotan solas; la primera se carga con la página y el resto
    (data-src) recién cuando la tarjeta aparece en pantalla. Un clic abre el visor.
    Sin ``figs`` usa las del repositorio del ítem (galerias.json)."""
    figs = GAL.get(it.get("repo", ""), []) if figs is None else figs
    if not figs:
        return ""
    name = html.escape(re.sub(r"</?b>", "", it["name"][L]))
    page = it.get("page", PAGES.get(it.get("repo")))
    href = (f'{PAGE}{it["repo"]}/' if page else f'{GH}{it["repo"]}') if it.get("repo") else it.get("href", "")
    go = it.get("go") or (t(L, "Ver página", "View page") if page else t(L, "Ver código", "View code"))
    imgs = "".join(
        f'<img {"src" if k == 0 else "data-src"}="{html.escape(bust(f["src"][L]))}" alt="{html.escape(f["cap"][L])}"'
        + (' class="on" loading="lazy"' if k == 0 else "") + ">"
        for k, f in enumerate(figs))
    n = len(figs)
    lbl = t(L, f"Ver las {n} figuras de {name}" if n > 1 else f"Ampliar la figura de {name}",
            f"View the {n} figures of {name}" if n > 1 else f"Enlarge the figure of {name}")
    ctrl = ""
    if n > 1:
        ctrl = (f'<button type="button" class="nav prev" aria-label="{t(L, "Figura anterior", "Previous figure")}">{ARROW_L}</button>'
                f'<button type="button" class="nav next" aria-label="{t(L, "Figura siguiente", "Next figure")}">{ARROW_R}</button>'
                '<div class="dots" aria-hidden="true">' + '<i class="on"></i>' + "<i></i>" * (n - 1) + "</div>"
                '<div class="bar" aria-hidden="true"><i></i></div>')
    return (f'<div class="gal{cls}" data-title="{name}" data-href="{href}" data-go="{go}"><div class="frames">{imgs}</div>'
            f'<button type="button" class="open" aria-label="{lbl}"></button>{ctrl}'
            f'<span class="n" aria-hidden="true">{EXPAND}{n if n > 1 else ""}</span></div>')


def lightbox(L: int) -> str:
    return ('<dialog class="lb" aria-label="' + t(L, "Figuras del proyecto", "Project figures") + '">'
            '<div class="lb-top"><b></b><span class="lb-k"></span>'
            f'<a href="#">{t(L, "Ver página", "View page")} ↗</a>'
            f'<button type="button" class="lb-x" aria-label="{t(L, "Cerrar", "Close")}">{CLOSE}</button></div>'
            '<div class="lb-stage"><img alt="">'
            f'<button type="button" class="nav prev" aria-label="{t(L, "Figura anterior", "Previous figure")}">{ARROW_L}</button>'
            f'<button type="button" class="nav next" aria-label="{t(L, "Figura siguiente", "Next figure")}">{ARROW_R}</button></div>'
            '<p class="lb-cap" aria-live="polite"></p><div class="lb-th"></div></dialog>')


def card(it: dict, L: int, cls: str = "") -> str:
    acts = []
    if it.get("page"):
        acts.append(f'<a href="{PAGE}{it["repo"]}/">{t(L, "Ver página", "View page")}</a>')
    acts.append(f'<a href="{GH}{it["repo"]}">{t(L, "Código", "Code")}</a>')
    pic = gallery(it, L)
    tags = "".join(f"<code>{html.escape(x)}</code>" for x in it["tags"])
    attrs = f' data-kind="{kind(it)}" data-sector="{" ".join(SECT.get(it.get("repo", ""), []))}"'
    return (f'<article class="card {cls}"{attrs}>{pic}<h3><a href="{GH}{it["repo"]}">{h(it["name"][L])}</a></h3>'
            f'<div class="data {kind(it)}">{h(label(it, L))}</div><p>{h(it["res"][L])}</p>'
            f'<div class="tags">{tags}</div><div class="actions">{"".join(acts)}</div></article>')


def rvs_section(L: int) -> str:
    """Expectativa (datos simulados) contra comportamiento observado (datos reales): una fila
    por proyecto con la métrica esperada, la observada y la lectura de la diferencia."""
    rv = D["real_vs_sim"]
    hd = rv["head"][L]
    rows = "".join(
        f'<div class="rv-row" role="row"><div class="rv-p" role="cell"><a href="{GH}{r["repo"]}">{h(r["name"][L])}</a>'
        f'<span>{h(r["data"][L])}</span></div>'
        f'<div class="rv-m" role="cell">{h(r["metric"][L])}</div>'
        f'<div class="rv-v" role="cell"><span class="esp">{h(r["sim"][L])}</span><span class="fl" aria-hidden="true">→</span>'
        f'<b>{h(r["real"][L])}</b></div>'
        f'<div class="rv-w" role="cell">{h(r["why"][L])}</div></div>'
        for r in rv["rows"])
    head = "".join(f'<div role="columnheader">{h(x)}</div>' for x in hd)
    return (f'<h2 id="real">{h(rv["title"][L])}</h2><p class="sub">{h(rv["intro"][L])}</p>'
            f'<div class="rvt" role="table"><div class="rv-row rv-h" role="row">{head}</div>{rows}</div>')


INSTAGRAM = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
             '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/>'
             '<circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>')


def experience(L: int, R: str) -> str:
    """Experiencia como filas de CV: imagen a la izquierda, rol y detalle a la derecha. La fila
    de "outside" (perfil.json) es la docencia de enduro y solo existe en el sitio."""
    w = D["work"]
    acts = f'<a href="{GH}{w["repo"]}">{t(L, "Código del flujo", "Code of the pipeline")}</a>'
    # El cargo va como caso: empresa y período arriba, el texto y el mapa del trabajo a todo el
    # ancho, donde se lee. El repositorio reproduce parte del flujo con datos ficticios.
    meta = "".join(f"<span>{h(x)}</span>" for x in (w["network"][L], w["period"][L])) if w.get("company") else ""
    rows = [f'<article class="card xp wide"><div class="xb">'
            f'<p class="kick">{t(L, "Experiencia laboral", "Work experience")}</p>'
            f'<h3>{h(w.get("role", w["name"])[L])}</h3>'
            f'<div class="meta"><b>{h(w.get("company", ""))}</b>{meta}</div>'
            f'<p>{h(w["res"][L])}</p>{gallery(w, L)}<div class="tags">{"".join(f"<code>{html.escape(x)}</code>" for x in w["tags"])}</div>'
            f'<div class="actions xf">{acts}<span class="data {kind(w)}">{h(label(w, L))}</span></div></div></article>']
    o = D.get("outside")
    if o:
        years = date.today().year - o["since"]
        cap = f'{o["name"][L]} · {o["org"]}'
        link = (o.get("links") or [{}])[0]
        pic = gallery({"name": [cap, cap], "href": link.get("url", ""), "go": link.get("label", ["", ""])[L]}, L,
                      [{"src": [R + o["photo"]] * 2, "cap": [f'{cap}. {o["credit"][0]}', f'{cap}. {o["credit"][1]}']}], " pic")
        # Los grupos como etiquetas y el ciclo del mes como pasos numerados.
        facts = "".join(
            f'<dt>{h(f["label"][L])}</dt><dd class="{"steps" if f.get("steps") else ""}">'
            + "".join(f'<span>{f"<b>{k}</b>" if f.get("steps") else ""}{h(x[L])}</span>'
                      for k, x in enumerate(f["items"], 1)) + "</dd>"
            for f in o.get("facts", []))
        links = "".join(f'<a class="ig" href="{x["url"]}" rel="noopener">{INSTAGRAM}{h(x["handle"])}</a>'
                        for x in o.get("links", []))
        note = f'<span class="note">{h(o["note"][L])}</span>' if o.get("note") else ""
        rows.append(
            f'<article class="card xp">{pic}<div class="xb">'
            f'<p class="kick">{h(o["kicker"][L])}</p><h3>{h(o["name"][L])}</h3>'
            f'<div class="meta"><b>{h(o["org"])}</b><span>{h(o["place"][L])}</span>'
            f'<span>{t(L, "desde", "since")} {o["since"]}</span></div>'
            f'<p>{h(o["res"][L].replace("{n}", str(years)))}</p>'
            + (f'<dl class="facts">{facts}</dl>' if facts else "") +
            f'<div class="actions xf">{links}{note}<span class="credit">{h(o["credit"][L])}</span></div></div></article>')
    return '<div class="xps">' + "".join(rows) + "</div>"


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
    # Orden de lectura: quién soy, proyectos, experiencia, herramienta pública y stack.
    menu = [("inicio", t(L, "Quién soy", "About")), ("destacados", t(L, "Proyectos", "Projects")),
            ("experiencia", t(L, "Experiencia", "Experience")), ("herramienta", t(L, "Herramienta pública", "Open-source tool")),
            ("stack", "Stack")]
    R = t(L, "", "../")  # la versión en inglés vive en /en/
    # Foto y CV son opcionales: aparecen solo si perfil.json los declara (rutas dentro del sitio).
    photo = (f'<img class="photo" src="{R}{p["photo"]}" alt="{h(p["name"])}" width="112" height="112">'
             if p.get("photo") else "")
    cv = (f'<a href="{R}{p["cv"][L]}" download>{t(L, "Descargar CV", "Download CV")}</a>' if p.get("cv") else "")
    theme_lbl = t(L, "Cambiar entre modo claro y oscuro", "Toggle light and dark mode")
    body = ['<div class="top"><div class="in">'
            f'<a class="brand" href="#">{h(p["name"])}</a>'
            '<nav>' + "".join(f'<a href="#{k}">{v}</a>' for k, v in menu) + '</nav>'
            f'<div class="right"><button class="theme" type="button" aria-label="{theme_lbl}" title="{theme_lbl}">{SUN_MOON}</button>'
            f'<div class="lang">{other}</div></div></div></div><div class="wrap">',
            f'<header class="hero" id="inicio"><div class="hero-top"><div><p class="eyebrow">Data Scientist</p><h1>{h(p["name"])}</h1>'
            f'<p class="role">{h(p["role"][L])}</p></div>{photo}</div>',
            f'<div class="intro">{intro}</div><div class="links">',
            f'<a class="primary" href="{p["github"]}">GitHub</a><a href="{p["linkedin"]}">LinkedIn</a>{cv}',
            f'<a href="mailto:{p["email"]}">{p["email"]}</a><a href="{GH}{lib["repo"]}">datoschile</a></div>',
            '<div class="stats">' + "".join(f'<div class="stat"><b>{n}</b><span>{s}</span></div>' for n, s in stats)
            + "</div></header>",
            f'<h2 id="destacados">{t(L, "Proyectos destacados", "Featured projects")}</h2>',
            f'<p class="sub">{t(L, "Cuatro proyectos con datos reales y un hallazgo que no era el esperado.", "Four projects on real data with a finding that was not the expected one.")}</p>',
            '<div class="grid feat">' + "".join(card(f, L) for f in D["featured"]) + "</div>",
            rvs_section(L),
            f'<h2 id="proyectos">{t(L, "Proyectos por tipo de problema", "Projects by kind of problem")}</h2>',
            f'<p class="sub">{t(L, f"{len(items)} proyectos. Cada uno indica si usa datos reales o simulados.", f"{len(items)} projects. Each states whether it uses real or simulated data.")}</p>',
            f'<nav class="toc">{toc}</nav>']
    # Filtros: solo se ofrecen los sectores que tienen al menos un proyecto.
    used = {s for it in items for s in SECT.get(it["repo"], [])}
    def chips(group: str, opts: list[tuple[str, str]]) -> str:
        return "".join(f'<button type="button" class="chip" data-group="{group}" data-value="{v}" '
                       f'aria-pressed="{"true" if v == "" else "false"}">{h(lbl)}</button>' for v, lbl in opts)
    sect_opts = [("", t(L, "Todos", "All"))] + [(k, v[L]) for k, v in SECT["_sectores"].items() if k in used]
    data_opts = [("", t(L, "Todos", "All")), ("real", t(L, "Reales", "Real")),
                 ("mix", t(L, "Real + simulado", "Real + simulated")), ("sim", t(L, "Simulados", "Simulated"))]
    tpl = t(L, "Mostrando {n} proyectos", "Showing {n} projects")
    body.append(f'<div class="filters"><div class="frow"><b>{t(L, "Sector", "Sector")}</b>{chips("sector", sect_opts)}</div>'
                f'<div class="frow"><b>{t(L, "Datos", "Data")}</b>{chips("datos", data_opts)}</div></div>'
                f'<p class="count" data-tpl="{tpl}" aria-live="polite">{tpl.replace("{n}", str(len(items)))}</p>')
    for i, c in enumerate(cats, 1):
        body.append(f'<section class="catwrap"><h2 class="cat" id="c{i}"><span class="n">{i}.</span>{h(c["name"][L])}</h2>')
        body.append('<div class="grid">' + "".join(card(it, L) for it in c["items"]) + "</div></section>")
    def tool(x: dict) -> str:
        ic = (f'<i class="ic" style="--i:url({R}assets/icons/{x["logo"]}.svg)" aria-hidden="true"></i>'
              if x.get("logo") in ICONS else "")
        return f"<span>{ic}{h(x['label'])}</span>"
    tools = "".join(f"<div><b>{h(g['group'][L])}</b>" + "".join(tool(x) for x in g["items"]) + "</div>" for g in D["tools"])
    body += [f'<h2 id="experiencia">{t(L, "Experiencia", "Experience")}</h2>',
             experience(L, R),
             (f'<h2 id="herramienta">{t(L, "Herramienta pública", "Open-source tool")}</h2>'
            f'<article class="card lib">{gallery(lib, L, cls=" oscura" if lib.get("dark") else "")}<h3><a href="{GH}{lib["repo"]}">{h(lib["name"][L])}</a></h3>'
            f'<p>{h(lib["res"][L])}</p><pre><code>{html.escape(lib["code"])}</code></pre>'
            f'<div class="tags">{"".join(f"<code>{x}</code>" for x in lib["tags"])}</div>'
            '<div class="actions">' + (f'<a href="{PAGE}{lib["repo"]}/">{t(L, "Ver panel", "View dashboard")}</a>' if lib.get("page") else "")
            + f'<a href="{GH}{lib["repo"]}">{t(L, "Código e instalación", "Code and install")}</a></div></article>'),
             f'<h2 id="stack">Stack</h2><div class="tools">{tools}</div>',
             f'<footer><span>{h(p["name"])} · {h(p["role"][L])}</span><span><a href="{p["github"]}">GitHub</a> · '
             f'<a href="{p["linkedin"]}">LinkedIn</a> · <a href="mailto:{p["email"]}">{p["email"]}</a></span></footer>']
    desc = t(L, "Portafolio de ciencia de datos de Pablo Reyes: proyectos ordenados por el tipo de problema que resuelven.",
             "Data science portfolio of Pablo Reyes: projects organized by the kind of problem they solve.")
    lang = t(L, "es", "en")
    title = f'Pablo Reyes · {t(L, "Ciencia de datos", "Data science")}'
    url = PAGE + t(L, "", "en/")
    og = (f'<meta property="og:type" content="website"><meta property="og:title" content="{title}">'
          f'<meta property="og:description" content="{desc}"><meta property="og:url" content="{url}">'
          f'<meta property="og:image" content="{PAGE}assets/og-{lang}.png"><meta property="og:image:width" content="1200">'
          f'<meta property="og:image:height" content="630"><meta property="og:locale" content="{t(L, "es_CL", "en_US")}">'
          f'<meta name="twitter:card" content="summary_large_image">\n'
          f'<link rel="icon" href="{R}favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{R}assets/icon-180.png">\n')
    return (f'<!doctype html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{title}</title>\n'
            f'<meta name="description" content="{desc}">\n' + og +
            f'<script>{THEME_BOOT}</script>\n'
            f'<link rel="alternate" hreflang="es" href="{PAGE}"><link rel="alternate" hreflang="en" href="{PAGE}en/">\n'
            '<meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)">'
            '<meta name="theme-color" content="#0D1117" media="(prefers-color-scheme: dark)">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
            f"<style>{CSS}</style>\n</head>\n<body>\n" + "\n".join(body) + "\n</div>\n" + lightbox(L) +
            f"\n<script>{JS}</script>\n</body>\n</html>\n")



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
        global SITE
        SITE = a.site
        ICONS.update(f.stem for f in (a.site / "assets" / "icons").glob("*.svg"))
        (a.site / "en").mkdir(parents=True, exist_ok=True)
        escribir(a.site / "index.html", site(ES))
        escribir(a.site / "en" / "index.html", site(EN))
        escribir(a.site / ".nojekyll", "")
        print(f"sitio -> {a.site}")


if __name__ == "__main__":
    main()
