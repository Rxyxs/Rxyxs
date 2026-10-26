"""Dibuja el diagrama del proyecto de la flota de buses (assets/shots/bus-fleet-flow-{es,en}.svg).

    python tools/diagrama_flota.py ../Rxyxs.github.io

El proyecto es de trabajo y su repositorio usa datos de ejemplo, así que la tarjeta muestra el
proceso en cuatro etapas en vez de un gráfico de resultados.
"""
from __future__ import annotations

import sys
from html import escape
from pathlib import Path

TXT = {
    "es": {
        "title": "Control de combustible de una flota de buses",
        "sub": "De 17 planillas sueltas a una base consolidada y una app de registro en terreno",
        "stages": [
            ("Fuente", "17 planillas Excel", ["Una planilla por terminal", "Cada terminal registraba sus cargas por separado"],
             ["17 terminales"]),
            ("Integración", "Consolidación en Python", ["Une las 17 planillas en una sola base", "Comprime los registros y los consolida"],
             ["Por terminal", "Por día", "Por mes"]),
            ("Validación", "Control de rendimiento", ["km/L de cada bus contra su carga anterior", "Marca las cargas fuera del rango de su modelo"],
             ["km/L", "Rango por modelo"]),
            ("Operación", "App en AppSheet", ["El operador registra cargas, pistolas y estanques desde el celular", "Reemplazó las planillas"],
             ["Consumo por pistola", "Stock teórico", "AdBlue"]),
        ],
        "out": "Resultado",
        "qa": "Control de calidad: errores corregidos al revisar el código",
        "fixes": ["Fechas mal ordenadas entre meses", "Buses sin rango por cómo estaba escrita la norma",
                  "Primera carga de cada bus marcada por error"],
        "note": "Diagrama del proceso. El repositorio usa datos de ejemplo ficticios.",
    },
    "en": {
        "title": "Fuel control for a bus fleet",
        "sub": "From 17 separate spreadsheets to one consolidated base and an app for field records",
        "stages": [
            ("Source", "17 Excel sheets", ["One sheet per depot", "Each depot recorded its loads separately"],
             ["17 depots"]),
            ("Integration", "Consolidation in Python", ["Merges the 17 sheets into one base", "Compresses the records and consolidates them"],
             ["By depot", "By day", "By month"]),
            ("Validation", "Efficiency check", ["Each bus's km/L against its previous load", "Flags loads outside its model's range"],
             ["km/L", "Range per model"]),
            ("Operation", "AppSheet app", ["Operators record loads, pumps and tanks from their phone", "Replaced the spreadsheets"],
             ["Per-pump consumption", "Theoretical stock", "AdBlue"]),
        ],
        "out": "Output",
        "qa": "Quality control: bugs fixed while reviewing the code",
        "fixes": ["Dates sorted wrongly across months", "Buses left without a range by how the standard was written",
                  "Every bus's first load flagged by mistake"],
        "note": "Process diagram. The repository uses fictitious example data.",
    },
}

INK, BODY, MUTED, LINE, SOFT = "#1F2328", "#3D444D", "#6E7781", "#D0D7DE", "#F6F8FA"
ACC, ACC_SOFT, ACC_LINE = "#1A7F37", "#EEF8F0", "#9BD3AB"
W, H = 1200, 684
CW, GAP, X0, Y0, CH = 252, 40, 40, 128, 344


def wrap(s: str, n: int) -> list[str]:
    lines, cur = [], ""
    for w in s.split():
        if cur and len(cur) + 1 + len(w) > n:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    return lines + [cur]


def text(x, y, s, size=14, weight=400, fill=BODY, anchor="start", extra="") -> str:
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{extra}>{escape(s)}</text>')


def icon(k: int, x: float, y: float) -> str:
    """Íconos de 44 px dibujados con trazos: planillas, embudo, indicador y teléfono."""
    s = f'fill="none" stroke="{ACC}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
    if k == 0:
        return (f'<rect x="{x + 8}" y="{y}" width="30" height="36" rx="3" {s} opacity=".45"/>'
                f'<rect x="{x + 2}" y="{y + 6}" width="30" height="36" rx="3" fill="#fff" stroke="{ACC}" stroke-width="2"/>'
                f'<path d="M{x + 2} {y + 18}h30M{x + 2} {y + 30}h30M{x + 14} {y + 6}v36" {s}/>')
    if k == 1:
        return (f'<path d="M{x} {y + 6}h44l-16 18v14l-12 6v-20z" {s}/>'
                f'<path d="M{x + 8} {y}v2M{x + 22} {y - 2}v4M{x + 36} {y}v2" {s}/>')
    if k == 2:
        return (f'<path d="M{x + 4} {y + 32}a18 18 0 1 1 36 0" {s}/>'
                f'<path d="M{x + 22} {y + 32}l9-12" {s}/><circle cx="{x + 22}" cy="{y + 32}" r="3" fill="{ACC}"/>')
    return (f'<rect x="{x + 10}" y="{y}" width="24" height="42" rx="4" {s}/>'
            f'<path d="M{x + 18} {y + 5}h8M{x + 15} {y + 14}h14M{x + 15} {y + 21}h14M{x + 15} {y + 28}h9" {s}/>'
            f'<circle cx="{x + 22}" cy="{y + 36}" r="1.6" fill="{ACC}"/>')


def chips(x: float, y: float, labels: list[str], maxw: float) -> str:
    out, cx, cy = [], x, y
    for lab in labels:
        w = 18 + len(lab) * 6.6
        if cx + w > x + maxw:
            cx, cy = x, cy + 30
        out.append(f'<rect x="{cx}" y="{cy}" width="{w:.0f}" height="24" rx="12" fill="{ACC_SOFT}" stroke="{ACC_LINE}"/>'
                   + text(cx + w / 2, cy + 16.5, lab, 12, 600, ACC, "middle"))
        cx += w + 6
    return "".join(out)


def svg(L: str) -> str:
    T = TXT[L]
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         'font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif">',
         f'<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto">'
         f'<path d="M0 1L9 5L0 9z" fill="{MUTED}"/></marker></defs>',
         f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
         text(X0, 64, T["title"], 26, 700, INK), text(X0, 94, T["sub"], 15.5, 400, MUTED)]
    for k, (phase, title, bullets, out) in enumerate(T["stages"]):
        x = X0 + k * (CW + GAP)
        last = k == len(T["stages"]) - 1
        p.append(f'<rect x="{x}" y="{Y0}" width="{CW}" height="{CH}" rx="14" fill="#fff" '
                 f'stroke="{ACC if last else LINE}" stroke-width="{2 if last else 1.4}"/>')
        p.append(text(x + 22, Y0 + 38, f"{k + 1:02d}  {phase.upper()}", 11.5, 700, ACC, extra=' letter-spacing="1.4"'))
        p.append(icon(k, x + 22, Y0 + 56))
        p.append(text(x + 22, Y0 + 132, title, 17.5, 700, INK))
        y = Y0 + 162
        for b in bullets:
            for j, ln in enumerate(wrap(b, 31)):
                if j == 0:
                    p.append(f'<circle cx="{x + 26}" cy="{y - 4.5}" r="2.6" fill="{MUTED}"/>')
                p.append(text(x + 36, y, ln, 13.5, 400, BODY))
                y += 19
            y += 7
        p.append(f'<line x1="{x + 22}" y1="{Y0 + 244}" x2="{x + CW - 22}" y2="{Y0 + 244}" stroke="{LINE}"/>')
        p.append(text(x + 22, Y0 + 266, T["out"].upper(), 11, 700, MUTED, extra=' letter-spacing="1.2"'))
        p.append(chips(x + 22, Y0 + 278, out, CW - 44))
        if not last:
            ax = x + CW + 6
            p.append(f'<line x1="{ax}" y1="{Y0 + CH / 2}" x2="{ax + GAP - 14}" y2="{Y0 + CH / 2}" '
                     f'stroke="{MUTED}" stroke-width="2" marker-end="url(#a)"/>')
    # Control de calidad, debajo del flujo.
    qy = Y0 + CH + 32
    p.append(f'<rect x="{X0}" y="{qy}" width="{W - 2 * X0}" height="118" rx="14" fill="{SOFT}" stroke="{LINE}"/>')
    p.append(f'<path d="M{X0} {qy + 14}v90" stroke="#BF8700" stroke-width="5" stroke-linecap="round"/>')
    p.append(text(X0 + 28, qy + 34, T["qa"], 15.5, 700, INK))
    colw = (W - 2 * X0 - 56) / 3
    for k, s in enumerate(T["fixes"]):
        cx = X0 + 28 + k * colw
        p.append(f'<circle cx="{cx + 12}" cy="{qy + 66}" r="12" fill="#fff" stroke="#BF8700" stroke-width="1.6"/>'
                 + text(cx + 12, qy + 70.5, str(k + 1), 12.5, 700, "#9A6700", "middle"))
        for j, ln in enumerate(wrap(s, 36)):
            p.append(text(cx + 34, qy + 71 + j * 19, ln, 14, 400, BODY))
    p.append(text(X0, H - 26, T["note"], 12.5, 400, MUTED))
    p.append("</svg>")
    return "".join(p)


if __name__ == "__main__":
    site = Path(sys.argv[1])
    for L in ("es", "en"):
        out = site / "assets" / "shots" / f"bus-fleet-flow-{L}.svg"
        out.write_text(svg(L) + "\n", encoding="utf-8", newline="\n")
        print(out)
