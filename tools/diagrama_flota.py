"""Dibuja el diagrama del proyecto de la flota de buses (assets/shots/bus-fleet-flow-{es,en}.svg).

    python tools/diagrama_flota.py ../Rxyxs.github.io

El proyecto es de trabajo y su repositorio usa datos de ejemplo, así que la tarjeta muestra el flujo que
describe su texto en perfil.json en vez de un gráfico de resultados.
"""
from __future__ import annotations

import sys
from html import escape
from pathlib import Path

TXT = {
    "es": {
        "a": ("17 planillas Excel", "una por terminal"),
        "b": ("Script en Python", "une las planillas · km/L contra", "la carga anterior · marca lo que", "sale del rango de su modelo"),
        "c": ("App en AppSheet", "el operador registra cargas,", "pistolas y estanques", "desde el celular"),
        "out": ("Consumo por pistola", "Stock teórico", "AdBlue"),
        "fix": "Errores corregidos al revisar el código",
        "fixes": ("fechas mal ordenadas entre meses", "buses sin rango por cómo estaba escrita la norma",
                  "la primera carga de cada bus marcada por error"),
        "s1": "1", "s2": "2",
    },
    "en": {
        "a": ("17 Excel sheets", "one per depot"),
        "b": ("Python script", "merges the sheets · km/L against", "the previous load · flags what", "falls outside its model's range"),
        "c": ("AppSheet app", "operators record loads,", "pump readings and tanks", "from their phone"),
        "out": ("Per-pump consumption", "Theoretical stock", "AdBlue"),
        "fix": "Bugs fixed while reviewing the code",
        "fixes": ("dates sorted wrongly across months", "buses left without a range by how the standard was written",
                  "every bus's first load flagged by mistake"),
        "s1": "1", "s2": "2",
    },
}

INK, MUTED, LINE, ACC, ACC_BG = "#1F2328", "#59636E", "#D1D9E0", "#1A7F37", "#DAFBE1"


def box(x, y, w, h, lines, step=None, fill="#FFFFFF", stroke=LINE) -> str:
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>']
    ty = y + 34
    for k, s in enumerate(lines):
        size, weight, col = (17, 700, INK) if k == 0 else (13.5, 400, MUTED)
        out.append(f'<text x="{x + w / 2}" y="{ty}" text-anchor="middle" font-size="{size}" '
                   f'font-weight="{weight}" fill="{col}">{escape(s)}</text>')
        ty += 26 if k == 0 else 20
    if step:
        out.append(f'<circle cx="{x + 18}" cy="{y + 18}" r="11" fill="{ACC}"/>'
                   f'<text x="{x + 18}" y="{y + 22.5}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{step}</text>')
    return "".join(out)


def arrow(x1, y1, x2, y2) -> str:
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{MUTED}" stroke-width="2" marker-end="url(#a)"/>'


def svg(L: str) -> str:
    T = TXT[L]
    p = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 450" font-family="Inter,Segoe UI,Arial,sans-serif">',
         f'<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         f'<path d="M0 0L10 5L0 10z" fill="{MUTED}"/></marker></defs>',
         '<rect width="960" height="450" fill="#FFFFFF"/>']
    # Las 17 planillas: una pila de hojas.
    for k in range(4, -1, -1):
        p.append(f'<rect x="{40 + k * 6}" y="{40 + k * 6}" width="190" height="120" rx="10" fill="#fff" stroke="{LINE}" stroke-width="1.5"/>')
    for r in range(4):
        p.append(f'<line x1="56" y1="{68 + r * 18}" x2="214" y2="{68 + r * 18}" stroke="{LINE}" stroke-width="1"/>')
    p.append(f'<text x="135" y="206" text-anchor="middle" font-size="17" font-weight="700" fill="{INK}">{escape(T["a"][0])}</text>'
             f'<text x="135" y="228" text-anchor="middle" font-size="13.5" fill="{MUTED}">{escape(T["a"][1])}</text>')
    p.append(arrow(262, 110, 300, 110))
    p.append(box(305, 40, 270, 140, T["b"], step=T["s1"]))
    p.append(arrow(580, 110, 618, 110))
    p.append(box(623, 40, 297, 140, T["c"], step=T["s2"], fill=ACC_BG, stroke=ACC))
    # Lo que calcula la app.
    for k, s in enumerate(T["out"]):
        x = 623 + k * 101
        p.append(f'<rect x="{x}" y="222" width="95" height="56" rx="9" fill="#F6F8FA" stroke="{LINE}"/>')
        words = s.split(" ", 1) if len(s) > 12 else [s]
        for j, w in enumerate(words):
            p.append(f'<text x="{x + 47.5}" y="{247 + j * 17 - (len(words) - 1) * 8}" text-anchor="middle" '
                     f'font-size="12.5" font-weight="600" fill="{INK}">{escape(w)}</text>')
    p.append(arrow(771, 183, 771, 218))
    # Los tres errores corregidos.
    p.append(f'<rect x="40" y="318" width="880" height="96" rx="12" fill="#FFF8C5" stroke="#D4A72C" stroke-width="1.2"/>'
             f'<text x="62" y="348" font-size="14.5" font-weight="700" fill="{INK}">{escape(T["fix"])}</text>')
    xs = (62, 340, 660)
    for k, s in enumerate(T["fixes"]):
        words, lines, cur = s.split(), [], ""
        for w in words:
            if len(cur) + len(w) > 34:
                lines.append(cur.strip()); cur = ""
            cur += w + " "
        lines.append(cur.strip())
        for j, ln in enumerate(lines):
            p.append(f'<text x="{xs[k] + 16}" y="{376 + j * 19}" font-size="13.5" fill="{INK}">{escape(ln)}</text>')
        p.append(f'<circle cx="{xs[k] + 5}" cy="{371}" r="3.5" fill="#9A6700"/>')
    p.append("</svg>")
    return "".join(p)


if __name__ == "__main__":
    site = Path(sys.argv[1])
    for L in ("es", "en"):
        out = site / "assets" / "shots" / f"bus-fleet-flow-{L}.svg"
        out.write_text(svg(L) + "\n", encoding="utf-8", newline="\n")
        print(out)
