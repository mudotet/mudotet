import json
import os
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET

from build_contribution_graph import read_grid


ROOT = Path(__file__).resolve().parents[1]
USERNAME = os.getenv("GITHUB_USERNAME", "mudotet")
API = "https://api.github.com"


def get_json(path):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "mudotet-profile-stats",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token := os.getenv("GH_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(f"{API}{path}", headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def get_stats():
    user = get_json(f"/users/{USERNAME}")
    repos = []
    page = 1
    while True:
        batch = get_json(f"/users/{USERNAME}/repos?per_page=100&type=owner&page={page}")
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    languages = {repo["language"] for repo in repos if repo["language"]}
    grid = read_grid()
    active_days = sum(level and level > 0 for week in grid for level in week if level is not None)
    return [
        ("PUBLIC REPOS", user["public_repos"], "repositories"),
        ("ACTIVE DAYS", active_days, "last 53 weeks"),
        ("LANGUAGES", len(languages), "across public repos"),
        ("FOLLOWERS", user["followers"], "public network"),
        ("FORKS", sum(repo["forks_count"] for repo in repos), "work reused"),
    ]


def render(theme, metrics):
    dark = theme == "dark"
    bg = ("#030712", "#07101F", "#0B1324") if dark else ("#FFFFFF", "#F8FAFC", "#EEF4F7")
    panel = "#0F172A" if dark else "#FFFFFF"
    card = "#111C31" if dark else "#FFFFFF"
    text = "#F8FAFC" if dark else "#0F172A"
    muted = "#94A3B8" if dark else "#475569"
    faint = "#64748B"
    border = "#FFFFFF" if dark else "#0F172A"
    cyan = "#22D3EE" if dark else "#06B6D4"
    green = "#34D399" if dark else "#10B981"
    violet = "#A78BFA" if dark else "#2563EB"

    cards = []
    icons = [
        '<path d="M0 6h14M3 2v8M11 2v8" fill="none" stroke="currentColor"/>',
        '<path d="M0 7h4l2-5 3 10 2-5h4" fill="none" stroke="currentColor"/>',
        '<path d="m4 2-4 5 4 5m7-10 4 5-4 5" fill="none" stroke="currentColor"/>',
        '<circle cx="5" cy="5" r="3" fill="none" stroke="currentColor"/><circle cx="12" cy="6" r="2.5" fill="none" stroke="currentColor"/><path d="M0 14c1-4 9-4 10 0m0-2c2-2 5-1 6 2" fill="none" stroke="currentColor"/>',
        '<path d="M8 1v9m0 0-5-3m5 3 5-3M3 7V3m10 4V3" fill="none" stroke="currentColor"/><circle cx="3" cy="2" r="1.5"/><circle cx="13" cy="2" r="1.5"/><circle cx="8" cy="12" r="1.5"/>',
    ]
    for index, ((label, value, note), icon) in enumerate(zip(metrics, icons)):
        x = 42 + index * 220
        delay = index * 0.55
        cards.append(
            f"""<g transform="translate({x} 92)">
      <rect width="202" height="126" rx="18" fill="{card}" fill-opacity="{'.62' if dark else '.8'}" stroke="{border}" stroke-opacity="{'.07' if dark else '.08'}"/>
      <rect width="202" height="126" rx="18" fill="none" stroke="url(#accent)" stroke-opacity=".08">
        <animate attributeName="stroke-opacity" values=".08;.48;.08" dur="5s" begin="-{delay:.2f}s" repeatCount="indefinite"/>
      </rect>
      <g transform="translate(20 18)" color="{cyan}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
      <text x="20" y="55" fill="{muted}" font-size="9.5" letter-spacing="1.35">{label}</text>
      <text x="20" y="94" fill="url(#accent)" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="38" font-weight="760">{value}
        <animate attributeName="opacity" values=".78;1;.78" dur="4.5s" begin="-{delay:.2f}s" repeatCount="indefinite"/>
      </text>
      <text x="75" y="92" fill="{faint}" font-size="9.5">{note}</text>
      <rect x="20" y="109" width="162" height="2" rx="1" fill="{border}" fill-opacity="{'.055' if dark else '.07'}"/>
      <rect x="20" y="109" width="0" height="2" rx="1" fill="url(#accent)">
        <animate attributeName="width" values="0;162;162;0" keyTimes="0;.35;.82;1" dur="7s" begin="-{delay:.2f}s" repeatCount="indefinite"/>
      </rect>
    </g>"""
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="310" viewBox="0 0 1180 310" preserveAspectRatio="xMidYMid meet" role="img" aria-labelledby="title desc">
  <title id="title">Phan Thanh Tu — animated GitHub stats</title>
  <desc id="desc">Live public GitHub statistics for @{USERNAME}: repositories, active days, languages, followers, and forks.</desc>
  <defs>
    <clipPath id="canvas"><rect width="1180" height="310" rx="28"/></clipPath>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{bg[0]}"/><stop offset=".55" stop-color="{bg[1]}"/><stop offset="1" stop-color="{bg[2]}"/>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{violet}"><animate attributeName="stop-color" values="{violet};{cyan};{violet}" dur="8s" repeatCount="indefinite"/></stop>
      <stop offset=".55" stop-color="{cyan}"><animate attributeName="stop-color" values="{cyan};{green};{cyan}" dur="8s" repeatCount="indefinite"/></stop>
      <stop offset="1" stop-color="{green}"><animate attributeName="stop-color" values="{green};{violet};{green}" dur="8s" repeatCount="indefinite"/></stop>
      <animate attributeName="x1" values="-.3;.35;-.3" dur="7s" repeatCount="indefinite"/>
      <animate attributeName="x2" values=".7;1.35;.7" dur="7s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="glow"><stop offset="0" stop-color="{cyan}" stop-opacity="{'.13' if dark else '.075'}"/><stop offset="1" stop-color="{cyan}" stop-opacity="0"/></radialGradient>
    <filter id="soft" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <filter id="noise"><feTurbulence type="fractalNoise" baseFrequency=".74" numOctaves="2" seed="23"><animate attributeName="baseFrequency" values=".72;.78;.72" dur="9s" repeatCount="indefinite"/></feTurbulence><feColorMatrix type="saturate" values="0"/></filter>
  </defs>
  <g clip-path="url(#canvas)" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
    <rect width="1180" height="310" fill="url(#bg)"/>
    <ellipse cx="940" cy="12" rx="360" ry="175" fill="url(#glow)"><animateTransform attributeName="transform" type="translate" values="0 0;-80 25;0 0" dur="14s" repeatCount="indefinite"/></ellipse>
    <rect x="20" y="20" width="1140" height="270" rx="22" fill="{panel}" fill-opacity="{'.66' if dark else '.74'}" stroke="{border}" stroke-opacity="{'.08' if dark else '.07'}"/>
    <rect x="21" y="21" width="1138" height="268" rx="21" fill="none" stroke="url(#accent)" stroke-opacity=".36" stroke-dasharray="70 250"><animate attributeName="stroke-dashoffset" values="0;-640" dur="8s" repeatCount="indefinite"/></rect>
    <circle cx="48" cy="49" r="4" fill="{green}" filter="url(#soft)"><animate attributeName="opacity" values="1;.3;1" dur="2.2s" repeatCount="indefinite"/></circle>
    <text x="62" y="53" fill="{text}" font-size="12" font-weight="700" letter-spacing="1.7">GITHUB STATS</text>
    <text x="180" y="53" fill="{faint}" font-size="9.5" letter-spacing=".8">PUBLIC SIGNAL / UPDATED DAILY</text>
    <text x="1132" y="53" text-anchor="end" fill="{muted}" font-size="10">@{USERNAME} · LIVE DATA</text>

    {''.join(cards)}

    <path id="signal" d="M58 252 C260 232 380 276 570 252 S880 228 1118 252" fill="none" stroke="url(#accent)" stroke-width="1.5" stroke-opacity=".42" stroke-dasharray="5 9"><animate attributeName="stroke-dashoffset" values="0;-56" dur="6s" repeatCount="indefinite"/></path>
    <circle r="4" fill="{cyan}" filter="url(#soft)"><animateMotion dur="7s" repeatCount="indefinite"><mpath href="#signal"/></animateMotion><animate attributeName="opacity" values=".35;1;.35" dur="2.4s" repeatCount="indefinite"/></circle>
    <g fill="{muted}" font-size="9" letter-spacing=".8">
      <text x="58" y="276">API</text><text x="280" y="276">BUILD</text><text x="548" y="276">SHIP</text><text x="812" y="276">LEARN</text><text x="1081" y="276">REPEAT</text>
    </g>
    <rect width="1180" height="310" filter="url(#noise)" opacity="{'.02' if dark else '.01'}"/>
  </g>
</svg>
"""


def main():
    metrics = get_stats()
    assert len(metrics) == 5 and all(isinstance(value, int) and value >= 0 for _, value, _ in metrics)
    for theme in ("dark", "light"):
        svg = render(theme, metrics)
        ET.fromstring(svg)
        (ROOT / "images" / f"stats-{theme}.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()
