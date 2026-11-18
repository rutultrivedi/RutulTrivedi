"""Generate assets/stats-30d.svg: GitHub contributions for the last 30 days.

Needs a token that can read the user's contribution counts (public and private):
a classic personal access token with the read:user scope, passed as GH_TOKEN.
"""
import base64, datetime as dt, html, json, os, re, sys, urllib.request

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OUT = os.path.join(ROOT, 'assets', 'stats-30d.svg')
README = os.path.join(ROOT, 'README.md')
LOGIN = os.environ.get('GITHUB_REPOSITORY_OWNER', 'rutultrivedi')
TOKEN = os.environ.get('GH_TOKEN', '')
DAYS = 30

if not TOKEN:
    print('GH_TOKEN is not set; leaving the existing card unchanged.')
    sys.exit(0)


def font(name):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts', name)
    return base64.b64encode(open(path, 'rb').read()).decode()


F = {'p600': font('poppins_latest_latin-600-normal.woff2'), 'i500': font('inter_latest_latin-500-normal.woff2')}
FALL = "-apple-system,'Segoe UI',Roboto,Arial,sans-serif"
NAVY2 = '#1d4079'
STEEL, SKY, MIST, DIM = '#3b6ea8', '#7fb0ff', '#dbe7f5', '#8da2c0'


def short(d):
    return d.strftime('%b ') + str(d.day)


# --- data: contribution calendar for the last 30 days (UTC); counts include private contributions
today = dt.datetime.now(dt.timezone.utc).date()
start = today - dt.timedelta(days=DAYS - 1)
query = ('query{user(login:"%s"){contributionsCollection(from:"%sT00:00:00Z",to:"%sT23:59:59Z")'
         '{contributionCalendar{weeks{contributionDays{date contributionCount}}}}}}') % (LOGIN, start, today)
req = urllib.request.Request('https://api.github.com/graphql', data=json.dumps({'query': query}).encode(),
                             headers={'Authorization': f'bearer {TOKEN}', 'Content-Type': 'application/json',
                                      'User-Agent': 'profile-stats'})
payload = json.load(urllib.request.urlopen(req, timeout=30))
if payload.get('errors') or not payload.get('data', {}).get('user'):
    sys.exit(f'GitHub API error: {payload.get("errors")}')
weeks = payload['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
by_day = {d['date']: d['contributionCount'] for w in weeks for d in w['contributionDays']}
days = [start + dt.timedelta(days=i) for i in range(DAYS)]
counts = [by_day.get(d.isoformat(), 0) for d in days]

total = sum(counts)
active = sum(1 for c in counts if c)
best = max(counts)
best_day = days[counts.index(best)]
streak, i = 0, DAYS - 1
if counts[i] == 0:      # today may not have activity yet; the streak is still alive until it ends
    i -= 1
while i >= 0 and counts[i] > 0:
    streak += 1
    i -= 1

# --- layout
W, H = 830, 440
PADX = 28
tiles = [(f'{total}', 'Contributions'), (f'{active}/{DAYS}', 'Active days'),
         (f'{best}', f'Busiest day ({short(best_day)})'), (f'{streak}', 'Current streak (days)')]
TG = 12
TWID = (W - 2 * PADX - 3 * TG) / 4
TY, TH = 76, 86
CH_X, CH_W = PADX, W - 2 * PADX
CH_TOP, CH_BASE = 214, 372
pitch = CH_W / DAYS
bw = pitch * 0.68
maxc = max(best, 1)

o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', '<defs>',
     f'<linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{NAVY2}"/><stop offset="0.5" stop-color="{SKY}"/><stop offset="1" stop-color="{NAVY2}"/><animate attributeName="x1" values="-1;1" dur="6s" repeatCount="indefinite"/><animate attributeName="x2" values="0;2" dur="6s" repeatCount="indefinite"/></linearGradient>',
     '<linearGradient id="tile" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14274a"/><stop offset="1" stop-color="#0c1730"/></linearGradient>',
     f'<linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SKY}"/><stop offset="1" stop-color="{STEEL}"/></linearGradient>',
     '</defs>', '<style>',
     f"@font-face{{font-family:'Poppins';font-weight:600;src:url(data:font/woff2;base64,{F['p600']}) format('woff2')}}",
     f"@font-face{{font-family:'Inter';font-weight:500;src:url(data:font/woff2;base64,{F['i500']}) format('woff2')}}",
     f".t{{font-family:'Poppins',{FALL};font-size:15px;font-weight:600;fill:{SKY};letter-spacing:2.2px}}",
     f".rng{{font-family:'Inter',{FALL};font-size:12.5px;font-weight:500;fill:{DIM}}}",
     f".num{{font-family:'Poppins',{FALL};font-size:30px;font-weight:600;fill:{MIST}}}",
     f".lab{{font-family:'Inter',{FALL};font-size:12px;font-weight:500;fill:{DIM}}}",
     f".ax{{font-family:'Inter',{FALL};font-size:11px;font-weight:500;fill:{DIM}}}",
     f".tb{{stroke:{STEEL};stroke-width:1;stroke-opacity:.55}}",
     '.tile{opacity:0;animation:in .6s ease-out forwards}',
     '.b{transform-box:fill-box;transform-origin:50% 100%;transform:scaleY(0);animation:grow .8s cubic-bezier(.2,.8,.2,1) forwards}',
     f'.dot{{fill:{SKY};animation:blink 2.4s ease-in-out infinite}}',
     '@keyframes in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}',
     '@keyframes grow{to{transform:scaleY(1)}}',
     '@keyframes blink{0%,100%{opacity:.35}50%{opacity:1}}', '</style>',
     f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="#0b1220" stroke="url(#g)" stroke-width="2"/>',
     '<circle class="dot" cx="34" cy="36" r="4.5"/>',
     '<text class="t" x="48" y="41">GITHUB ACTIVITY  -  LAST 30 DAYS</text>',
     f'<text class="rng" x="{W - PADX}" y="41" text-anchor="end">{short(start)} - {short(today)}, {today.year}</text>',
     f'<line x1="{PADX}" y1="58" x2="{W - PADX}" y2="58" stroke="#1c2d4d" stroke-width="1"/>']

for k, (num, lab) in enumerate(tiles):
    x = PADX + k * (TWID + TG)
    o.append(f'<g class="tile" style="animation-delay:{0.1 + 0.1 * k:.1f}s"><rect class="tb" x="{x:.1f}" y="{TY}" width="{TWID:.1f}" height="{TH}" rx="14" fill="url(#tile)"/>'
             f'<text class="num" x="{x + TWID / 2:.1f}" y="{TY + 42}" text-anchor="middle">{html.escape(num)}</text>'
             f'<text class="lab" x="{x + TWID / 2:.1f}" y="{TY + 68}" text-anchor="middle">{html.escape(lab)}</text></g>')

for frac in (0, 0.5, 1):
    gy = CH_BASE - (CH_BASE - CH_TOP) * frac
    dash = '0' if frac == 0 else '3 5'
    o.append(f'<line x1="{PADX}" y1="{gy:.1f}" x2="{W - PADX}" y2="{gy:.1f}" stroke="#1c2d4d" stroke-width="1" stroke-dasharray="{dash}"/>')
for k, (d, c) in enumerate(zip(days, counts)):
    x = CH_X + k * pitch + (pitch - bw) / 2
    h = max((CH_BASE - CH_TOP) * (c / maxc) ** 0.5, 3)
    fill = 'url(#bar)' if c else '#1c2d4d'
    o.append(f'<rect class="b" style="animation-delay:{0.5 + 0.03 * k:.2f}s" x="{x:.1f}" y="{CH_BASE - h:.1f}" width="{bw:.1f}" height="{h:.1f}" rx="3" fill="{fill}"><title>{short(d)}: {c}</title></rect>')
for k in range(0, DAYS, 5):
    o.append(f'<text class="ax" x="{CH_X + k * pitch + pitch / 2:.1f}" y="{CH_BASE + 22}" text-anchor="middle">{short(days[k])}</text>')
o.append(f'<text class="ax" x="{CH_X + (DAYS - 1) * pitch + pitch / 2:.1f}" y="{CH_BASE + 22}" text-anchor="middle">Today</text>')
o.append(f'<text class="ax" x="{PADX}" y="{CH_TOP - 8}">{maxc}</text>')
o.append(f'<text class="lab" x="{W / 2}" y="{H - 26}" text-anchor="middle">Daily contributions (public and private, scaled so quiet days stay visible)</text>')
o.append('</svg>')
open(OUT, 'w', encoding='utf-8').write('\n'.join(o))

# version the image URL so GitHub and browsers fetch the fresh card instead of a cached copy
text = open(README, encoding='utf-8').read()
new = re.sub(r'assets/stats-30d\.svg(\?v=\d+)?', f'assets/stats-30d.svg?v={today:%Y%m%d}', text)
if new != text:
    open(README, 'w', encoding='utf-8').write(new)
print(f'{start}..{today} total={total} active={active} best={best} streak={streak}')
