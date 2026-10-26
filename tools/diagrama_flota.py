"""Dibuja el mapa del trabajo en Buses Vule (assets/shots/bus-fleet-flow-{es,en}.svg).

    python tools/diagrama_flota.py ../Rxyxs.github.io

El cargo fue de analista de datos en abastecimiento y combustibles; el repositorio
bus-fleet-fuel-efficiency reproduce parte del flujo con datos ficticios. El diagrama junta lo
que cuenta el README del repositorio y lo que dice el CV: indicadores arriba, cinco etapas de
izquierda a derecha y, abajo, los problemas de datos que se encontraron y corrigieron.
"""
from __future__ import annotations

import sys
from html import escape
from pathlib import Path

TXT = {
    "es": {
        "title": "Buses Vule S.A. · Abastecimiento y combustibles",
        "sub": "Analista de Datos · Red Metropolitana de Movilidad · enero 2025 a abril 2026",
        "kpis": [("20", "terminales"), ("2.094", "buses en la app"), ("−70%", "tiempo de procesamiento"),
                 ("1.754", "cargas reales en la prueba"), ("13", "tests automatizados")],
        "stages": [
            ("Captura", "App en AppSheet",
             ["Reemplazó las planillas Excel y el papel", "Formularios de buses y camionetas con lógica condicional",
              "Lecturas por turno: pistolas, AdBlue y stock", "Validaciones sobre un modelo relacional"],
             ["Móvil y web", "KPIs automáticos"]),
            ("Integración", "ETL en Python",
             ["Consolida las planillas por terminal, día y mes", "Limpia horas, patentes y fechas digitadas a mano",
              "Automatiza cuadraturas semanales de inventario y reportes de compras"],
             ["pandas", "regex", "−70% tiempo"]),
            ("Control", "Rendimiento y estanques",
             ["km/L de cada bus contra su carga anterior, aunque sea en otro terminal",
              "Marca BR o CI según el rango de su modelo y norma", "Stock teórico contra el medido en cada estanque"],
             ["KMACC", "REV", "Stock teórico"]),
            ("Analítica", "Anomalías y forecast",
             ["Detección de anomalías: pérdidas y desviaciones de combustible",
              "Forecast de demanda para abastecer insumos críticos"],
             ["Anomalías", "Forecast"]),
            ("Reportes", "Power BI y ERP",
             ["Dashboards ejecutivos de indicadores de flota", "Excel con fórmulas vivas y colores por rango",
              "Sincronización con el ERP Softland"],
             ["Power BI", "Softland"]),
        ],
        "out": "Resultado",
        "qa": "Problemas de datos encontrados y corregidos",
        "fixes": ["Fechas ordenadas como texto: entre meses, los km se calculaban contra la lectura equivocada",
                  "La norma escrita de dos formas (Euro V / EURO V) dejaba buses sin rango y sin alerta",
                  "La primera carga de cada bus salía marcada como bajo rango",
                  "La app tomaba la lectura inicial de otro turno; se amarró por folio, terminal y fecha",
                  "Una planilla con el mes mal digitado producía 28 kilometrajes negativos"],
        "note": "El repositorio bus-fleet-fuel-efficiency reproduce la consolidación, el rendimiento y el control de estanques con datos ficticios.",
    },
    "en": {
        "title": "Buses Vule S.A. · Supply and fuel",
        "sub": "Data Analyst · Santiago's public bus network (Red) · January 2025 to April 2026",
        "kpis": [("20", "depots"), ("2,094", "buses in the app"), ("−70%", "processing time"),
                 ("1,754", "real loads in the test"), ("13", "automated tests")],
        "stages": [
            ("Capture", "AppSheet app",
             ["Replaced the Excel sheets and paper", "Bus and van forms with conditional logic",
              "Per-shift readings: pumps, AdBlue and stock", "Validations on a relational model"],
             ["Mobile and web", "Automatic KPIs"]),
            ("Integration", "Python ETL",
             ["Consolidates the sheets by depot, day and month", "Cleans hand-typed times, plates and dates",
              "Automates weekly inventory reconciliations and purchase reports"],
             ["pandas", "regex", "−70% time"]),
            ("Control", "Efficiency and tanks",
             ["Each bus's km/L against its previous load, even at another depot",
              "Flags BR or CI by its model and standard's range", "Theoretical stock against the measured stock per tank"],
             ["KMACC", "REV", "Theoretical stock"]),
            ("Analytics", "Anomalies and forecast",
             ["Anomaly detection: fuel losses and deviations", "Demand forecast to supply critical inputs"],
             ["Anomalies", "Forecast"]),
            ("Reporting", "Power BI and ERP",
             ["Executive dashboards of fleet indicators", "Excel with live formulas and range colours",
              "Sync with the Softland ERP"],
             ["Power BI", "Softland"]),
        ],
        "out": "Output",
        "qa": "Data problems found and fixed",
        "fixes": ["Dates sorted as text: across months, km were computed against the wrong reading",
                  "The standard written two ways (Euro V / EURO V) left buses with no range and no alert",
                  "Every bus's first load was flagged as below range",
                  "The app picked another shift's opening reading; now matched by folio, depot and date",
                  "A sheet with a mistyped month produced 28 negative mileages"],
        "note": "The bus-fleet-fuel-efficiency repository reproduces the consolidation, efficiency and tank control on fictitious data.",
    },
}

INK, BODY, MUTED, LINE, SOFT = "#1F2328", "#3D444D", "#6E7781", "#D0D7DE", "#F6F8FA"
ACC, ACC_SOFT, ACC_LINE = "#1A7F37", "#EEF8F0", "#9BD3AB"
GOLD, GOLD_INK = "#BF8700", "#9A6700"
W, X0 = 1280, 40
N, GAP = 5, 26
CW = (W - 2 * X0 - (N - 1) * GAP) / N
KY, SY, SH = 122, 232, 432          # indicadores, etapas y alto de cada etapa
QY = SY + SH + 30                    # franja de calidad
QH = 174
H = QY + QH + 52


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
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{extra}>{escape(s)}</text>')


def icon(k: int, x: float, y: float) -> str:
    """Íconos de 40 px con trazos: teléfono, embudo, indicador, gráfico de tendencia y tablero."""
    s = f'fill="none" stroke="{ACC}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
    if k == 0:
        return (f'<rect x="{x + 9}" y="{y}" width="22" height="38" rx="4" {s}/>'
                f'<path d="M{x + 16} {y + 5}h8M{x + 14} {y + 13}h12M{x + 14} {y + 19}h12M{x + 14} {y + 25}h8" {s}/>'
                f'<circle cx="{x + 20}" cy="{y + 33}" r="1.5" fill="{ACC}"/>')
    if k == 1:
        return (f'<path d="M{x} {y + 6}h40l-15 16v12l-10 5v-17z" {s}/>'
                f'<path d="M{x + 7} {y}v2M{x + 20} {y - 2}v4M{x + 33} {y}v2" {s}/>')
    if k == 2:
        return (f'<path d="M{x + 3} {y + 34}a17 17 0 1 1 34 0" {s}/>'
                f'<path d="M{x + 20} {y + 34}l8-11" {s}/><circle cx="{x + 20}" cy="{y + 34}" r="3" fill="{ACC}"/>')
    if k == 3:
        return (f'<path d="M{x + 2} {y + 36}h36M{x + 2} {y + 2}v34" {s}/>'
                f'<path d="M{x + 6} {y + 28}l9-9 7 6 13-15" {s}/>'
                f'<circle cx="{x + 22}" cy="{y + 25}" r="2.4" fill="#fff" stroke="#CF222E" stroke-width="2"/>')
    return (f'<rect x="{x}" y="{y + 2}" width="40" height="32" rx="4" {s}/>'
            f'<path d="M{x + 8} {y + 26}v-6M{x + 16} {y + 26}v-12M{x + 24} {y + 26}v-9M{x + 32} {y + 26}v-15" {s}/>')


def chips(x: float, y: float, labels: list[str], maxw: float) -> str:
    out, cx, cy = [], x, y
    for lab in labels:
        w = 16 + len(lab) * 6.4
        if cx + w > x + maxw:
            cx, cy = x, cy + 29
        out.append(f'<rect x="{cx:.1f}" y="{cy}" width="{w:.0f}" height="23" rx="11.5" fill="{ACC_SOFT}" stroke="{ACC_LINE}"/>'
                   + text(cx + w / 2, cy + 16, lab, 11.5, 600, ACC, "middle"))
        cx += w + 6
    return "".join(out)


def svg(L: str) -> str:
    T = TXT[L]
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         'font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif">',
         f'<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         f'<path d="M0 1L9 5L0 9z" fill="{MUTED}"/></marker></defs>',
         f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
         text(X0, 62, T["title"], 26, 700, INK), text(X0, 92, T["sub"], 15.5, 400, MUTED)]
    # Indicadores.
    kw = (W - 2 * X0 - 4 * 14) / 5
    for k, (v, lab) in enumerate(T["kpis"]):
        x = X0 + k * (kw + 14)
        p.append(f'<rect x="{x:.1f}" y="{KY}" width="{kw:.1f}" height="78" rx="12" fill="{SOFT}" stroke="{LINE}"/>'
                 + text(x + 18, KY + 40, v, 26, 700, ACC if k == 2 else INK)
                 + text(x + 18, KY + 63, lab, 13, 400, MUTED))
    # Etapas.
    for k, (phase, title, bullets, out) in enumerate(T["stages"]):
        x = X0 + k * (CW + GAP)
        p.append(f'<rect x="{x:.1f}" y="{SY}" width="{CW:.1f}" height="{SH}" rx="14" fill="#fff" stroke="{LINE}" stroke-width="1.4"/>')
        p.append(text(x + 18, SY + 34, f"{k + 1:02d}  {phase.upper()}", 11, 700, ACC, extra=' letter-spacing="1.3"'))
        p.append(icon(k, x + 18, SY + 52))
        p.append(text(x + 18, SY + 122, title, 15.5, 700, INK))
        y = SY + 152
        for b in bullets:
            for j, ln in enumerate(wrap(b, 27)):
                if j == 0:
                    p.append(f'<circle cx="{x + 22}" cy="{y - 4.5}" r="2.4" fill="{MUTED}"/>')
                p.append(text(x + 31, y, ln, 13, 400, BODY))
                y += 18
            y += 8
        p.append(f'<line x1="{x + 18}" y1="{SY + SH - 92}" x2="{x + CW - 18}" y2="{SY + SH - 92}" stroke="{LINE}"/>')
        p.append(text(x + 18, SY + SH - 70, T["out"].upper(), 10.5, 700, MUTED, extra=' letter-spacing="1.2"'))
        p.append(chips(x + 18, SY + SH - 58, out, CW - 36))
        if k < N - 1:
            ax = x + CW + 3
            p.append(f'<line x1="{ax:.1f}" y1="{SY + SH / 2}" x2="{ax + GAP - 8:.1f}" y2="{SY + SH / 2}" '
                     f'stroke="{MUTED}" stroke-width="2" marker-end="url(#a)"/>')
    # Problemas de datos, en tres columnas.
    p.append(f'<rect x="{X0}" y="{QY}" width="{W - 2 * X0}" height="{QH}" rx="14" fill="#FFFBEA" stroke="#EAD39C"/>')
    p.append(f'<path d="M{X0} {QY + 16}v{QH - 32}" stroke="{GOLD}" stroke-width="5" stroke-linecap="round"/>')
    p.append(text(X0 + 28, QY + 36, T["qa"], 15.5, 700, INK))
    colw = (W - 2 * X0 - 56) / 3
    for k, s in enumerate(T["fixes"]):
        cx, cy = X0 + 28 + (k % 3) * colw, QY + 70 + (k // 3) * 60
        p.append(f'<circle cx="{cx + 11:.1f}" cy="{cy - 4}" r="11" fill="#fff" stroke="{GOLD}" stroke-width="1.6"/>'
                 + text(cx + 11, cy + 0.5, str(k + 1), 12, 700, GOLD_INK, "middle"))
        for j, ln in enumerate(wrap(s, 50)):
            p.append(text(cx + 32, cy + j * 18, ln, 13.5, 400, BODY))
    p.append(text(X0, H - 22, T["note"], 12.5, 400, MUTED))
    p.append("</svg>")
    return "".join(p)


if __name__ == "__main__":
    site = Path(sys.argv[1])
    for L in ("es", "en"):
        out = site / "assets" / "shots" / f"bus-fleet-flow-{L}.svg"
        out.write_text(svg(L) + "\n", encoding="utf-8", newline="\n")
        print(out)
