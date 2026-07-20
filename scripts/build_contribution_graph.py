from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "images" / "breakout-dark.svg"
LEVELS = {
    "#151B23": 0,
    "#033A16": 1,
    "#196C2E": 2,
    "#2EA043": 3,
    "#56D364": 4,
}


def read_grid():
    root = ET.parse(SOURCE).getroot()
    cells = [
        node
        for node in root.iter()
        if node.tag.endswith("rect")
        and node.get("width") == "12"
        and node.get("height") == "12"
        and int(node.get("y", "999")) <= 105
    ]
    xs = sorted({int(node.get("x")) for node in cells})
    ys = sorted({int(node.get("y")) for node in cells})
    assert len(xs) == 53 and len(ys) == 7
    lookup = {
        (xs.index(int(node.get("x"))), ys.index(int(node.get("y")))): LEVELS[node.get("fill")]
        for node in cells
    }
    return [[lookup.get((week, day)) for day in range(7)] for week in range(53)]


def render(theme, grid):
    dark = theme == "dark"
    colors = (
        ["#111827", "#123F3A", "#0F766E", "#14B8A6", "#5EEAD4"]
        if dark
        else ["#E7EDF2", "#BFE8E3", "#70D3C8", "#22B8A7", "#087E75"]
    )
    bg = ("#030712", "#07111F", "#0B1324") if dark else ("#FFFFFF", "#F7FAFC", "#EEF4F7")
    text = "#F8FAFC" if dark else "#0F172A"
    muted = "#94A3B8" if dark else "#475569"
    border = "#FFFFFF" if dark else "#0F172A"
    x0, y0, step, size = 88, 101, 18.6, 13
    active = sum(level and level > 0 for week in grid for level in week if level is not None)

    cells = []
    for week, days in enumerate(grid):
        for day, level in enumerate(days):
            if level is None:
                continue
            x, y = x0 + week * step, y0 + day * 16.5
            pulse = ""
            if level:
                begin = -((week * 7 + day) % 37) / 3
                pulse = (
                    f'<animate attributeName="opacity" values=".72;1;.72" '
                    f'dur="{3 + level * .45:.2f}s" begin="{begin:.2f}s" repeatCount="indefinite"/>'
                )
            cells.append(
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{size}" height="{size}" rx="3.2" '
                f'fill="{colors[level]}" opacity="{.78 if level == 0 else 1}">{pulse}</rect>'
            )

    weekly = [sum(level or 0 for level in days) for days in grid]
    peak = max(weekly) or 1
    points = [
        (x0 + week * step + size / 2, 261 - value / peak * 20)
        for week, value in enumerate(weekly)
    ]
    trace = " ".join(
        ("M" if index == 0 else "L") + f"{x:.1f} {y:.1f}"
        for index, (x, y) in enumerate(points)
    )
    cell_markup = "".join(cells)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="300" viewBox="0 0 1180 300" preserveAspectRatio="xMidYMid meet" role="img" aria-labelledby="title desc">
  <title id="title">Phan Thanh Tu — GitHub contribution signal</title>
  <desc id="desc">Animated 53-week contribution heatmap generated from the same GitHub data as the Breakout game.</desc>
  <defs>
    <clipPath id="canvas"><rect width="1180" height="300" rx="26"/></clipPath>
    <clipPath id="grid"><rect x="82" y="95" width="1000" height="124" rx="12"/></clipPath>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{bg[0]}"/>
      <stop offset=".55" stop-color="{bg[1]}"/>
      <stop offset="1" stop-color="{bg[2]}"/>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#7C3AED"/>
      <stop offset=".52" stop-color="#06B6D4"/>
      <stop offset="1" stop-color="#10B981"/>
      <animate attributeName="x1" values="-.3;.35;-.3" dur="7s" repeatCount="indefinite"/>
      <animate attributeName="x2" values=".7;1.35;.7" dur="7s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="scan" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#22D3EE" stop-opacity="0"/>
      <stop offset=".5" stop-color="#22D3EE" stop-opacity=".24"/>
      <stop offset="1" stop-color="#22D3EE" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="glow">
      <stop offset="0" stop-color="#06B6D4" stop-opacity="{'.13' if dark else '.07'}"/>
      <stop offset="1" stop-color="#06B6D4" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="noise">
      <feTurbulence type="fractalNoise" baseFrequency=".74" numOctaves="2" seed="9">
        <animate attributeName="baseFrequency" values=".72;.78;.72" dur="9s" repeatCount="indefinite"/>
      </feTurbulence>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
  </defs>
  <g clip-path="url(#canvas)">
    <rect width="1180" height="300" fill="url(#bg)"/>
    <ellipse cx="940" cy="22" rx="330" ry="170" fill="url(#glow)">
      <animateTransform attributeName="transform" type="translate" values="0 0;-70 22;0 0" dur="13s" repeatCount="indefinite"/>
    </ellipse>
    <rect x="28" y="26" width="1124" height="248" rx="22" fill="{border}" fill-opacity="{'.025' if dark else '.2'}" stroke="{border}" stroke-opacity="{'.08' if dark else '.07'}"/>
    <circle cx="52" cy="53" r="4" fill="#34D399" filter="url(#soft)">
      <animate attributeName="opacity" values="1;.35;1" dur="2.2s" repeatCount="indefinite"/>
    </circle>
    <text x="66" y="58" fill="{text}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="13" font-weight="700" letter-spacing="1.8">CONTRIBUTION SIGNAL</text>
    <text x="66" y="79" fill="{muted}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="10.5" letter-spacing=".8">53-WEEK ACTIVITY · GENERATED FROM GITHUB</text>
    <text x="1117" y="57" text-anchor="end" fill="{text}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="12">{active:02d} ACTIVE DAYS</text>
    <text x="1117" y="78" text-anchor="end" fill="{muted}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="10">@mudotet / LIVE DATA</text>

    <g clip-path="url(#grid)">{cell_markup}
      <rect x="-40" y="95" width="110" height="124" fill="url(#scan)">
        <animate attributeName="x" values="-80;1110" dur="5.8s" repeatCount="indefinite"/>
      </rect>
    </g>
    <text x="66" y="111" text-anchor="end" fill="{muted}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="9">M</text>
    <text x="66" y="160" text-anchor="end" fill="{muted}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="9">W</text>
    <text x="66" y="210" text-anchor="end" fill="{muted}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="9">F</text>

    <path d="{trace}" fill="none" stroke="url(#accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" pathLength="100" stroke-dasharray="100" filter="url(#soft)">
      <animate attributeName="stroke-dashoffset" values="100;0;0" keyTimes="0;.28;1" dur="8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values=".45;1;.45" dur="4.5s" repeatCount="indefinite"/>
    </path>
    <text x="66" y="262" fill="{muted}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="9" letter-spacing="1">WEEKLY INTENSITY</text>
    <g transform="translate(1008 248)" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="9" fill="{muted}">
      <text x="-45" y="11">LESS</text>
      {''.join(f'<rect x="{i * 17}" width="12" height="12" rx="3" fill="{color}"/>' for i, color in enumerate(colors))}
      <text x="91" y="11">MORE</text>
    </g>
    <rect width="1180" height="300" filter="url(#noise)" opacity="{'.022' if dark else '.01'}"/>
  </g>
  <rect x="1" y="1" width="1178" height="298" rx="25" fill="none" stroke="url(#accent)" stroke-opacity=".45"/>
</svg>
"""


def main():
    grid = read_grid()
    for theme in ("dark", "light"):
        output = ROOT / "images" / f"contribution-{theme}.svg"
        svg = render(theme, grid)
        ET.fromstring(svg)
        output.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()
