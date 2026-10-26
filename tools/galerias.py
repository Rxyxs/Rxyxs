"""Arma tools/galerias.json: las figuras que se muestran en la galería de cada tarjeta del sitio.

    python tools/galerias.py

Lee la página publicada de cada proyecto (rxyxs.github.io/<repo>/) y toma sus figuras en el
orden en que aparecen, con el texto alternativo como título. Si el proyecto no tiene página, o
la página no tiene figuras, busca imágenes en el árbol del repositorio y las sirve por jsDelivr.
La figura de miniaturas.json va primero; si existe una versión animada (``*_animated.gif``) de
una figura, se usa en lugar del PNG. Las URL quedan absolutas para que build_profile.py solo
tenga que copiarlas.
"""
from __future__ import annotations

import html
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = "https://rxyxs.github.io/"
CDN = "https://cdn.jsdelivr.net/gh/Rxyxs/"
MAX = 8
IMG = re.compile(r"\.(png|gif|svg|jpe?g|webp)$", re.I)
# Imágenes de los README que no son figuras de resultados.
SKIP = re.compile(r"badge|favicon|(^|/)(icons?|logos?)/", re.I)


def get(url: str) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": "rxyxs-galerias"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError:
        return None


def attr(tag: str, name: str) -> str:
    m = re.search(rf'\b{name}="([^"]*)"', tag)
    return html.unescape(m.group(1)).strip() if m else ""


def first_sentence(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    m = re.match(r"(.+?[.!?])(\s|$)", s)
    return (m.group(1) if m else s).rstrip(".")


def humanize(path: str) -> str:
    stem = Path(path).stem.replace("_animated", "")
    stem = re.sub(r"^(figura)?\d+[_-]", "", stem)
    return stem.replace("_", " ").replace("-", " ").strip().capitalize()


def from_page(repo: str, text: str) -> list[dict]:
    """Figuras de la página publicada, en orden. Las páginas que eligen la carpeta del idioma
    con JavaScript (``<img data-fig>``) se resuelven a figures/es y figures/en."""
    base = f"{PAGE}{repo}/"
    i18n = {L: dict(re.findall(r'\b(f_\w+):\s*"([^"]+)"', block))
            for L, block in zip(("es", "en"), re.split(r"\n\s*en\s*:\s*\{", text, maxsplit=1))}
    out = []
    for m in re.finditer(r"<img\b[^>]*>(?:\s*<figcaption[^>]*data-i18n=\"(\w+)\")?", text):
        tag, key = m.group(0), m.group(1)
        src, fig = attr(tag, "src"), attr(tag, "data-fig")
        if fig:
            caps = [first_sentence(i18n.get(L, {}).get(key, "")) or humanize(fig) for L in ("es", "en")]
            out.append({"src": [f"{base}figures/es/{fig}", f"{base}figures/en/{fig}"], "cap": caps})
        elif src and not src.startswith(("http:", "https:", "data:", "//")) and IMG.search(src):
            cap = attr(tag, "alt") or humanize(src)
            out.append({"src": [base + src] * 2, "cap": [cap, cap]})
    return out


def from_repo(repo: str) -> list[dict]:
    """Sin página: las figuras que citan el README de la raíz y el de cada carpeta de primer
    nivel (los módulos de un laboratorio), que son las vigentes; el árbol completo arrastra
    figuras de versiones anteriores. Se alterna entre README para que un laboratorio con varios
    módulos no muestre solo el primero."""
    tree = json.loads(get(f"https://api.github.com/repos/Rxyxs/{repo}/git/trees/HEAD?recursive=1") or "{}")
    paths = {t["path"] for t in tree.get("tree", [])}
    readmes = sorted((p for p in paths if re.fullmatch(r"([^/]+/)?README\.md", p)), key=lambda p: (p.count("/"), p))
    groups = []
    for rd in readmes:
        text = get(f"https://raw.githubusercontent.com/Rxyxs/{repo}/HEAD/{rd}") or ""
        folder = rd[: -len("README.md")]
        # ![texto](ruta) en markdown o <img src alt> en HTML; el texto alternativo es el título.
        refs = [(a, r) for a, r in re.findall(r"!\[([^\]]*)\]\(([^)\s]+)", text)]
        refs += [(attr(t, "alt"), attr(t, "src")) for t in re.findall(r"<img\b[^>]*>", text)]
        groups.append([(folder + r.removeprefix("./"), a) for a, r in refs
                       if IMG.search(r) and not r.startswith("http") and not SKIP.search(r)])
    order: dict[str, str] = {}
    while any(groups):
        for g in groups:
            if g:
                p, alt = g.pop(0)
                if p in paths and p not in order:
                    order[p] = alt
    return [{"src": [f"{CDN}{repo}@HEAD/{p}"] * 2, "cap": [a or humanize(p)] * 2} for p, a in order.items()]


def curate(figs: list[dict], cover: str | None) -> list[dict]:
    seen, uniq = set(), []
    for f in figs:
        if f["src"][0] not in seen:
            seen.add(f["src"][0])
            uniq.append(f)
    srcs = {f["src"][0] for f in uniq}
    # El PNG estático sobra cuando la página también tiene su versión animada.
    uniq = [f for f in uniq if not (f["src"][0].endswith(".png")
                                    and f["src"][0][:-4] + "_animated.gif" in srcs)]
    if cover:
        anim = re.sub(r"\.png$", "_animated.gif", cover)
        key = next((f for f in uniq if f["src"][0].endswith("/" + anim)), None) or \
              next((f for f in uniq if f["src"][0].endswith("/" + cover)), None)
        if key:
            uniq.remove(key)
            uniq.insert(0, key)
    return uniq[:MAX]


def main() -> None:
    D = json.loads((ROOT / "tools" / "perfil.json").read_text(encoding="utf-8"))
    thumbs = json.loads((ROOT / "tools" / "miniaturas.json").read_text(encoding="utf-8"))
    extra = json.loads((ROOT / "tools" / "galerias_extra.json").read_text(encoding="utf-8"))
    items = [p for c in D["categories"] for p in c["items"]] + D["featured"]
    covers = {f["repo"]: f.get("img") for f in D["featured"]}
    out = {}
    for repo in dict.fromkeys(it["repo"] for it in items):
        text = get(f"{PAGE}{repo}/")
        figs = from_page(repo, text) if text else []
        source = "página"
        if not figs:
            figs, source = from_repo(repo), "repositorio"
        # Capturas propias del sitio (por ejemplo, de un tablero interactivo sin figuras).
        figs = [{"src": [PAGE + e["src"]] * 2, "cap": e["cap"]} for e in extra.get(repo, [])] + figs
        out[repo] = curate(figs, covers.get(repo) or thumbs.get(repo))
        print(f"{repo:45s} {len(out[repo]):2d} figuras ({source})")
    (ROOT / "tools" / "galerias.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
