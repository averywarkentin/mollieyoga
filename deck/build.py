#!/usr/bin/env python3
# Generates deck/index.html — Mollie Yoga brand concepts, v2 (board-derived).
# All three directions are pulled from the actual "Mollie Yoga" Pinterest board:
# warm/earthy/tonal palettes, made distinct, with the board's named references cited.
import math

# ---------------------------------------------------------------- helpers
def swatch(hx, nm, role, dark=False):
    tc = "#fff" if dark else "#16110c"
    sc = "rgba(255,255,255,.78)" if dark else "rgba(0,0,0,.55)"
    return (f'<div class="sw" style="background:{hx};color:{tc}">'
            f'<div class="nm">{nm}</div>'
            f'<div class="hx" style="color:{sc}">{hx}</div></div>')

PAGE = 0
def page(cls, inner, foot="MOLLIE YOGA", num_label=""):
    global PAGE; PAGE += 1
    pn = f'<div class="pagenum">{num_label or PAGE:02}</div>' if num_label != "—" else ""
    ft = f'<div class="tag-foot">{foot}</div>' if foot else ""
    return f'<section class="page {cls}">{inner}{ft}{pn}</section>'

def curved_text(text, pid, fill, size=20, ls="0.04em", family="Fraunces", weight=500, italic=False,
                d="M20,150 C90,40 270,40 340,150", w=360, h=220, vb="0 0 360 220", startOffset="50%"):
    st = "italic" if italic else "normal"
    return (f'<svg viewBox="{vb}" width="{w}" height="{h}" style="overflow:visible">'
            f'<defs><path id="{pid}" d="{d}" fill="none"/></defs>'
            f'<text font-family="{family}" font-weight="{weight}" font-style="{st}" '
            f'font-size="{size}" letter-spacing="{ls}" fill="{fill}">'
            f'<textPath href="#{pid}" startOffset="{startOffset}" text-anchor="middle">{text}</textPath></text></svg>')

# ============================================================ CSS (board-derived gradient worlds)
CSS = r"""
/* 01 Studio Soma — warm bright earth */
.c1-field{background:
 radial-gradient(120% 95% at 12% 16%, #C9603A 0%, transparent 50%),
 radial-gradient(120% 100% at 88% 12%, #CFAA7B 0%, transparent 52%),
 radial-gradient(130% 115% at 82% 94%, #6E3E18 0%, transparent 55%),
 radial-gradient(120% 110% at 16% 96%, #B7816E 0%, transparent 56%),
 linear-gradient(120deg,#6E3E18,#9c5a36 52%,#c98a52);}
.c1-field2{background:
 radial-gradient(110% 95% at 80% 18%, #C9603A 0%, transparent 55%),
 radial-gradient(120% 110% at 16% 88%, #CFAA7B 0%, transparent 55%),
 radial-gradient(90% 90% at 88% 92%, #6E3E18 0%, transparent 55%),
 linear-gradient(135deg,#7a4520,#b7816e);}

/* 02 Nalu — greige tonal monochrome + dusty blue note */
.c2-field{background:
 radial-gradient(120% 95% at 18% 14%, #7F9FC2 0%, transparent 48%),
 radial-gradient(120% 110% at 86% 16%, #A9A398 0%, transparent 55%),
 radial-gradient(120% 115% at 88% 94%, #5A4F49 0%, transparent 55%),
 radial-gradient(90% 90% at 20% 92%, #645C54 0%, transparent 58%),
 linear-gradient(140deg,#4e4641,#7d756b 55%,#9aa0a3);}
.c2-field2{background:
 radial-gradient(110% 95% at 80% 18%, #7F9FC2 0%, transparent 52%),
 radial-gradient(120% 110% at 16% 88%, #645C54 0%, transparent 58%),
 linear-gradient(135deg,#3f3a36,#8a8378);}

/* 03 Grove — sage / ecru / umber natural calm */
.c3-field{background:
 radial-gradient(120% 95% at 14% 16%, #D6DBC3 0%, transparent 52%),
 radial-gradient(120% 105% at 86% 14%, #7C7E5E 0%, transparent 55%),
 radial-gradient(125% 115% at 84% 94%, #503E26 0%, transparent 55%),
 radial-gradient(110% 110% at 16% 96%, #9aa07e 0%, transparent 58%),
 linear-gradient(125deg,#41442b,#6d6f4f 55%,#a8a487);}
.c3-field2{background:
 radial-gradient(110% 95% at 80% 18%, #D6DBC3 0%, transparent 55%),
 radial-gradient(120% 110% at 16% 88%, #503E26 0%, transparent 55%),
 radial-gradient(90% 90% at 88% 90%, #7C7E5E 0%, transparent 55%),
 linear-gradient(135deg,#43452d,#7c7e5e);}
"""

# ============================================================ BRAND MARKS
# 01 Studio Soma — playful sun / bloom
def soma_sun(col="#F1ECE8", size=118):
    rays=""
    for i in range(12):
        a=2*math.pi*i/12
        x1=size/2+size*0.30*math.cos(a); y1=size/2+size*0.30*math.sin(a)
        x2=size/2+size*0.43*math.cos(a); y2=size/2+size*0.43*math.sin(a)
        rays+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{size*0.045:.1f}" stroke-linecap="round"/>'
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
      f'<circle cx="{size/2}" cy="{size/2}" r="{size*0.20:.1f}" fill="{col}"/>{rays}</svg>')

def soma_stamp(col="#F1ECE8", size=150):
    r=size/2; txt="MOLLIE YOGA · MINDFUL MOVEMENT · QUIET JOY · "
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
      f'<defs><path id="somar" fill="none" d="M{r},{r} m-{r-14},0 a{r-14},{r-14} 0 1,1 {2*(r-14)},0 a{r-14},{r-14} 0 1,1 -{2*(r-14)},0"/></defs>'
      f'<text font-family="DM Sans" font-weight="600" font-size="10.5" letter-spacing="0.16em" fill="{col}">'
      f'<textPath href="#somar" startOffset="0">{txt}</textPath></text>'
      f'<g transform="translate({r-26},{r-26})">{soma_sun(col,52)}</g></svg>')

# 02 Nalu — fluid wave line (nalu = wave)
def nalu_wave(col="#E2E1DC", w=150, h=80):
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 150 80" fill="none">'
      f'<path d="M6,46 C30,18 50,18 74,40 C96,60 118,60 144,30" stroke="{col}" stroke-width="5" stroke-linecap="round"/>'
      f'<path d="M6,62 C30,38 50,38 74,56 C96,74 118,74 144,48" stroke="{col}" stroke-width="3.4" stroke-linecap="round" opacity="0.55"/></svg>')

def nalu_mono(col="#E2E1DC", size=80):
    # interlocking M / wave monogram
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 80 80" fill="none">'
      f'<path d="M14,60 L14,24 C14,18 22,18 26,26 L34,44 C37,50 43,50 46,44 L54,26 C58,18 66,18 66,24 L66,60" '
      f'stroke="{col}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# 03 Grove — botanical sprig + seal
def grove_sprig(col="#2A2117", w=70, h=110):
    leaves=""
    for i,(yy,sgn) in enumerate([(78,-1),(60,1),(42,-1),(26,1)]):
        dx=sgn*18
        leaves+=(f'<path d="M35,{yy} C{35+dx},{yy-4} {35+dx},{yy-20} 35,{yy-16}" stroke="{col}" stroke-width="3" fill="none" stroke-linecap="round"/>')
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 70 110" fill="none">'
      f'<path d="M35,100 C35,70 35,40 35,12" stroke="{col}" stroke-width="3.2" stroke-linecap="round"/>'
      f'<circle cx="35" cy="10" r="4" fill="{col}"/>{leaves}</svg>')

def grove_seal(col="#EAE7DC", ink="#41442b", size=150):
    r=size/2; txt="· MOLLIE YOGA · ROOTED · GROWING · CALM "
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
      f'<circle cx="{r}" cy="{r}" r="{r-2}" fill="{ink}"/>'
      f'<defs><path id="grover" fill="none" d="M{r},{r} m-{r-13},0 a{r-13},{r-13} 0 1,1 {2*(r-13)},0 a{r-13},{r-13} 0 1,1 -{2*(r-13)},0"/></defs>'
      f'<text font-family="Spectral" font-weight="500" font-size="10.5" letter-spacing="0.10em" fill="{col}">'
      f'<textPath href="#grover" startOffset="0">{txt}</textPath></text>'
      f'<g transform="translate({r-18},{r-34})">{grove_sprig(col,36,64)}</g></svg>')

MARKS = {"01": soma_sun, "02": nalu_wave, "03": grove_sprig}

# ============================================================ THEMES
C1 = dict(key="01", name="Studio Soma", tag="Mindful movement, quiet joy.",
    display="Bricolage", body="DM Sans", quote="Spectral",
    paper="#F1ECE8", ink="#140D08", soft="#7a5a44",
    field="c1-field", field2="c1-field2", duo="c1-field2",
    accent="#C9603A", accent2="#6E3E18",
    palette=[("#140D08","Espresso","ink",1),("#6E3E18","Sienna","anchor",1),
             ("#B7816E","Clay","primary",1),("#CFAA7B","Camel","primary",0),
             ("#C9603A","Flame","highlight",1),("#F1ECE8","Warm Cream","base",0)],
    cite="Pulled from <b>Studio Soma</b> on the board (“bright, uplifting… warm feel-good palette, playful logo suite”) and the board’s clay / camel / espresso pins — #b7816e · #cfaa7b · #6e3e18.",
    note="Bright, warm and welcoming — the sunniest read of the board. Playful bold type, rounded sun mark, terracotta-to-camel gradients. Grounded but never sleepy; ‘anyone can do yoga’.")

C2 = dict(key="02", name="Nalu", tag="Move like water.",
    display="Fraunces", body="Space Grotesk", quote="Fraunces",
    paper="#E2E1DC", ink="#020203", soft="#6e675f",
    field="c2-field", field2="c2-field2", duo="c2-field2",
    accent="#7F9FC2", accent2="#5A4F49",
    palette=[("#020203","Onyx","ink",1),("#5A4F49","Stone","anchor",1),
             ("#645C54","Taupe","primary",1),("#A9A398","Greige","primary",1),
             ("#7F9FC2","Dusty Blue","highlight",1),("#E2E1DC","Mist","base",0)],
    cite="Pulled from <b>nalu</b> on the board (“brand mark over dynamic photography… fluidity, graphic overlay, brand lookbooks”) and the board’s greige / taupe tonals — #a9a398 · #645c54 — with its one cool note, dusty blue #7f9fc2.",
    note="Tonal, editorial, photography-led. A high-contrast wordmark and a fluid wave mark sit over monochrome imagery; a single dusty-blue accent keeps it from going flat. Quiet luxury — the most ‘lookbook’ of the three.")

C3 = dict(key="03", name="Grove", tag="Rooted. Growing. Calm.",
    display="Spectral", body="DM Sans", quote="Spectral",
    paper="#EAE7DC", ink="#2A2117", soft="#6a6450",
    field="c3-field", field2="c3-field2", duo="c3-field2",
    accent="#7C7E5E", accent2="#503E26",
    palette=[("#2A2117","Bark","ink",1),("#503E26","Umber","anchor",1),
             ("#7C7E5E","Olive","primary",1),("#D6DBC3","Sage","primary",0),
             ("#C6C6C4","Stone","secondary",0),("#EAE7DC","Ecru","base",0)],
    cite="Pulled from the board’s <b>Behance yoga-identity</b> collection and its sage / ecru / umber pins — #d6dbc3 · #eae7dc · #503e26.",
    note="The calm, natural, grounded read. Humanist serif, botanical sprig mark, sage-and-ecru with deep umber to anchor it. Earthy and quiet without tipping into the soft ‘beige & sage’ cliché — the umber and olive give it backbone.")

THEMES=[C1,C2,C3]
for t in THEMES: t["mark"]=MARKS[t["key"]]

# ============================================================ IG CONTENT BLOCKS
def ig_announce(t):
    return (f'<div class="{t["field"]} grain" style="position:absolute;inset:0;"></div>'
      f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:space-between;padding:13px;color:#fff;z-index:5">'
      f'<div class="eyebrow" style="font-size:8px;letter-spacing:.3em;opacity:.92">NEW CLASS</div>'
      f'<div><div style="font-family:{t["display"]};font-weight:600;font-size:25px;line-height:.96">Slow<br>Flow</div>'
      f'<div style="font-family:{t["body"]};font-size:9px;letter-spacing:.04em;margin-top:6px;opacity:.95">Thursdays · 6.00pm<br>Abbey Wood, SE</div></div></div>')

def ig_schedule(t):
    days=[("MON","Vinyasa · 7am"),("TUE","—"),("WED","Slow Flow · 6pm"),("THU","Yin · 6pm"),("FRI","Hatha · 9am"),("SAT","Community · 10am")]
    rows="".join(f'<div style="display:flex;justify-content:space-between;border-bottom:1px solid rgba(0,0,0,.10);padding:4.5px 0"><span style="font-weight:600">{d}</span><span style="opacity:.7">{c}</span></div>' for d,c in days)
    return (f'<div style="position:absolute;inset:0;background:{t["paper"]};color:{t["ink"]};padding:13px 14px;z-index:5;font-family:{t["body"]};font-size:8.5px">'
      f'<div style="font-family:{t["display"]};font-weight:600;font-size:17px;margin-bottom:9px">This week</div>{rows}</div>')

def ig_quote(t, q='“When disturbed by negative thoughts, opposite ones should be thought of.”', cite="Yoga Sutras 2.33"):
    return (f'<div class="{t["field2"]} grain" style="position:absolute;inset:0;"></div>'
      f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;padding:18px;z-index:5">'
      f'<div style="font-family:{t["quote"]};{"font-style:italic;" if t["quote"] in ("Fraunces","Spectral") else ""}font-weight:500;color:#fff;font-size:15px;line-height:1.22;text-align:center">{q}</div></div>'
      f'<div style="position:absolute;bottom:11px;left:0;right:0;text-align:center;color:rgba(255,255,255,.85);font-family:{t["body"]};font-size:8px;letter-spacing:.16em;z-index:6">{cite.upper()}</div>')

def ig_retreat(t):
    return (f'<div class="{t["duo"]} grain" style="position:absolute;inset:0;"></div>'
      f'<div style="position:absolute;inset:0;border:1px solid rgba(255,255,255,.4);margin:9px;z-index:6"></div>'
      f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;text-align:center;color:#fff;z-index:5;padding:14px">'
      f'<div class="eyebrow" style="font-size:8px;opacity:.9">DAY RETREAT</div>'
      f'<div style="font-family:{t["display"]};font-weight:600;font-size:24px;line-height:.98;margin:8px 0">Autumn<br>Reset</div>'
      f'<div style="font-family:{t["body"]};font-size:9px;letter-spacing:.05em;opacity:.95">SAT 12 OCT · 10–4<br>+ tea, sound, stillness</div></div>')

def ig_life(t, lbl="on the mat"):
    return (f'<div class="{t["field"]} grain" style="position:absolute;inset:0;filter:saturate(1.04)"></div>'
      f'<div style="position:absolute;bottom:11px;left:12px;color:#fff;font-family:{t["quote"]};{"font-style:italic" if t["quote"] in ("Fraunces","Spectral") else ""}font-size:14px;z-index:5;text-shadow:0 1px 8px rgba(0,0,0,.35)">{lbl}</div>')

def profile_grid(t):
    cells=[ig_announce(t), ig_quote(t), ig_life(t,"breath"),
           ig_schedule(t), ig_life(t,"studio light"), ig_retreat(t),
           ig_quote(t,'“You become what you believe you can become.”','Bhagavad Gita'), ig_announce(t), ig_life(t,"after savasana"),
           ig_retreat(t), ig_schedule(t), ig_life(t,"morning")]
    return "".join(f'<div class="igcell">{c}</div>' for c in cells)

# ============================================================ PAGE TEMPLATES
def concept_cover(t):
    if t["key"]=="01":   markbig=soma_stamp("#F1ECE8",150)
    elif t["key"]=="02": markbig=nalu_wave("#E2E1DC",170,90)
    else:                markbig=grove_seal("#EAE7DC","#41442b",150)
    big=f'<div style="font-family:{t["display"]};color:#fff;font-weight:600;font-size:122px;line-height:.84;letter-spacing:-.02em;{"font-style:italic" if t["display"]=="Fraunces" else ""}">Mollie<br>Yoga</div>'
    inner=(f'<div class="{t["field"]} grain" style="position:absolute;inset:0"></div>'
      f'<div style="position:absolute;top:54px;right:70px;z-index:12">{markbig}</div>'
      f'<div class="pad col" style="justify-content:space-between">'
      f'<div class="eyebrow" style="color:rgba(255,255,255,.9)">Direction {t["key"]} / Three · from the board</div>'
      f'<div>{big}'
      f'<div style="font-family:{t["quote"] if t["quote"] in ("Fraunces","Spectral") else t["body"]};{"font-style:italic;" if t["quote"] in ("Fraunces","Spectral") else ""}color:#fff;font-size:25px;margin-top:24px;opacity:.96">{t["tag"]}</div></div>'
      f'<div class="row" style="justify-content:space-between;align-items:flex-end;color:rgba(255,255,255,.86);font-family:{t["body"]};font-size:13px">'
      f'<div style="font-size:34px;font-family:{t["display"]};font-weight:600;{"font-style:italic" if t["display"]=="Fraunces" else ""}">{t["name"]}</div>'
      f'<div style="text-align:right;max-width:380px;opacity:.92">{t["note"]}</div></div></div>')
    return page(t["field"], inner, foot=f"DIRECTION {t['key']} · {t['name'].upper()}")

def marks_panel(t):
    if t["key"]=="01":
        m=(f'<div style="display:flex;gap:30px;align-items:center">{soma_sun("#F1ECE8",96)}{soma_stamp("#F1ECE8",118)}</div>')
        wm=f'<div style="font-family:Bricolage;font-weight:800;font-size:48px;color:#fff;letter-spacing:-.02em">Mollie</div>'
    elif t["key"]=="02":
        m=(f'<div style="display:flex;gap:30px;align-items:center">{nalu_wave("#E2E1DC",132,72)}{nalu_mono("#E2E1DC",76)}</div>')
        wm=f'<div style="font-family:Fraunces;font-style:italic;font-weight:500;font-size:50px;color:#fff">Mollie</div>'
    else:
        m=(f'<div style="display:flex;gap:30px;align-items:center">{grove_seal("#EAE7DC","#41442b",120)}{grove_sprig("#EAE7DC",60,104)}</div>')
        wm=f'<div style="font-family:Spectral;font-weight:500;font-size:50px;color:#fff;letter-spacing:.01em">Mollie</div>'
    return m, wm

def identity_page(t):
    disp_it="font-style:italic;" if t["display"]=="Fraunces" else ""
    sw="".join(swatch(hx,nm,role,bool(d)) for hx,nm,role,d in t["palette"])
    spec=(f'<div style="font-family:{t["display"]};font-weight:600;font-size:60px;line-height:.92;color:{t["ink"]};{disp_it}">Aa Gg</div>'
      f'<div style="font-family:{t["body"]};font-size:12.5px;letter-spacing:.04em;color:{t["soft"]};margin-top:6px">{t["display"]} — display & headlines</div>'
      f'<div style="font-family:{t["quote"]};{"font-style:italic;" if t["quote"] in ("Fraunces","Spectral") else ""}font-size:23px;color:{t["ink"]};margin-top:20px;line-height:1.2">“Live your own destiny, imperfectly.”</div>'
      f'<div style="font-family:{t["body"]};font-size:12.5px;letter-spacing:.04em;color:{t["soft"]};margin-top:6px">{t["quote"]} — philosophy & quotes</div>'
      f'<div style="font-family:{t["body"]};font-size:13px;line-height:1.5;color:{t["ink"]};margin-top:20px;max-width:430px">Body copy, schedules, captions and buttons sit in {t["body"]} — clean and legible. ABCDEFGHIJKLM 0123456789</div>')
    marks, wordmk = marks_panel(t)
    inner=(f'<div style="position:absolute;inset:0;background:{t["paper"]}"></div><div class="paper-grain grain" style="position:absolute;inset:0"></div>'
      f'<div class="pad col">'
      f'<div class="row" style="justify-content:space-between;align-items:baseline">'
      f'<div style="font-family:{t["display"]};font-weight:600;font-size:30px;color:{t["ink"]};{disp_it}">Identity system</div>'
      f'<div class="eyebrow" style="color:{t["soft"]}">{t["name"]} · palette · type · mark</div></div>'
      f'<div style="height:20px"></div>'
      f'<div class="swatches" style="box-shadow:0 16px 40px -24px rgba(0,0,0,.4)">{sw}</div>'
      f'<div style="font-family:{t["body"]};font-size:10.5px;color:{t["soft"]};margin-top:9px;max-width:1130px;line-height:1.4">{t["cite"]}</div>'
      f'<div style="height:18px"></div>'
      f'<div class="row" style="gap:46px">'
      f'<div style="flex:1.12">{spec}</div>'
      f'<div style="flex:1;border-radius:16px;padding:26px;display:flex;flex-direction:column;justify-content:space-between;gap:16px;" class="{t["field"]}">'
      f'<div class="eyebrow" style="color:rgba(255,255,255,.85)">Brand marks · the “little tag”</div>'
      f'{marks}{wordmk}'
      f'<div style="font-family:{t["body"]};font-size:11px;color:rgba(255,255,255,.85)">Stamp on photos, profile picture, story sign-off — initials or full wordmark.</div></div>'
      f'</div></div>')
    return page("ident", inner, foot=f"DIRECTION {t['key']} · IDENTITY")

def instagram_page(t):
    disp_it="font-style:italic;" if t["display"]=="Fraunces" else ""
    head=(f'<div style="display:flex;align-items:center;gap:9px;padding:9px 11px 8px">'
      f'<div style="width:38px;height:38px;border-radius:50%;overflow:hidden;position:relative" class="{t["field"]} grain"></div>'
      f'<div style="font-family:{t["body"]};font-size:10.5px;color:{t["ink"]};line-height:1.2"><b>mollie.yoga</b><div style="opacity:.6;font-size:8px">Yoga in SE London · classes, corporate & private</div></div></div>')
    phone1=(f'<div class="phone" style="width:262px;height:430px"><div class="notch"></div>'
      f'<div class="screen" style="background:{t["paper"]}">{head}'
      f'<div class="iggrid" style="grid-template-rows:repeat(4,1fr);gap:2px;height:360px">{profile_grid(t)}</div></div></div>')
    def story(layers):
        return f'<div class="phone" style="width:154px;height:326px"><div class="screen" style="background:{t["paper"]}">{layers}</div></div>'
    s1=story(f'<div class="{t["field2"]} grain" style="position:absolute;inset:0"></div>'
        f'<div style="position:absolute;inset:0;color:#fff;padding:16px;display:flex;flex-direction:column;justify-content:space-between;z-index:5">'
        f'<div class="eyebrow" style="font-size:8px">THIS WEEK · COVER</div>'
        f'<div><div style="font-family:{t["display"]};font-weight:600;font-size:27px;line-height:.95;{disp_it}">Subbing<br>Wed Yin</div>'
        f'<div style="font-family:{t["body"]};font-size:9px;margin-top:8px;opacity:.95">6.00pm · Abbey Wood<br>covering for Sam</div></div>'
        f'<div style="transform:scale(.42);transform-origin:left;height:30px">{t["mark"]("#fff")}</div></div>')
    s2=story(f'<div style="position:absolute;inset:0;background:{t["paper"]};color:{t["ink"]};padding:16px;display:flex;flex-direction:column;justify-content:space-between;z-index:5">'
        f'<div class="eyebrow" style="font-size:8px;color:{t["soft"]}">REFLECTION</div>'
        f'<div style="font-family:{t["quote"]};{"font-style:italic;" if t["quote"] in ("Fraunces","Spectral") else ""}font-size:17px;line-height:1.28">Friendliness toward the happy, compassion for the unhappy.</div>'
        f'<div style="transform:scale(.5);transform-origin:left;height:26px">{t["mark"](t["accent2"])}</div></div>')
    s3=story(f'<div class="{t["duo"]} grain" style="position:absolute;inset:0"></div>'
        f'<div style="position:absolute;inset:0;z-index:5;color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:16px">'
        f'<div style="width:44px;height:44px;border-radius:50%;border:2px solid #fff;display:flex;align-items:center;justify-content:center;margin-bottom:12px;font-family:{t["body"]};font-size:8.5px;letter-spacing:.1em">REEL</div>'
        f'<div style="font-family:{t["display"]};font-weight:600;font-size:22px;line-height:1.0;{disp_it}">On the<br>practice</div>'
        f'<div style="font-family:{t["body"]};font-size:8.5px;margin-top:8px;opacity:.9;letter-spacing:.16em">EP. 01 · APARIGRAHA</div></div>')
    inner=(f'<div style="position:absolute;inset:0;background:{t["paper"]}"></div><div class="paper-grain grain" style="position:absolute;inset:0"></div>'
      f'<div class="pad col">'
      f'<div class="row" style="justify-content:space-between;align-items:baseline">'
      f'<div style="font-family:{t["display"]};font-weight:600;font-size:30px;color:{t["ink"]};{disp_it}">Instagram system</div>'
      f'<div class="eyebrow" style="color:{t["soft"]}">grid · stories · reel cover</div></div>'
      f'<div style="height:16px"></div>'
      f'<div class="row" style="gap:36px;align-items:flex-start">'
      f'<div>{phone1}</div>'
      f'<div class="col" style="gap:16px">'
      f'<div class="row" style="gap:13px">{s1}{s2}{s3}</div>'
      f'<div style="font-family:{t["body"]};font-size:12px;line-height:1.5;color:{t["ink"]};max-width:430px">'
      f'<b>Five grid templates:</b> announcement · weekly schedule · quote · retreat poster · class &amp; life. '
      f'<b>Five story templates:</b> schedule swap · event invite · reflection (brand-mark sign-off) · testimonial · reel cover. '
      f'Tonal photo fields + the {t["name"]} mark keep every post unmistakably yours — never Canva.</div>'
      f'</div></div></div>')
    return page("ig", inner, foot=f"DIRECTION {t['key']} · INSTAGRAM")

def website_page(t):
    disp_it="font-style:italic;" if t["display"]=="Fraunces" else ""
    nav=" ".join(f'<span style="margin-left:18px;opacity:.85">{x}</span>' for x in ["Classes","Corporate","Private","Philosophy"])
    hero=(f'<div class="{t["field"]} grain" style="height:268px;position:relative;display:flex;flex-direction:column;justify-content:space-between;padding:18px 24px;color:#fff">'
      f'<div style="display:flex;justify-content:space-between;align-items:center;font-family:{t["body"]};font-size:11px">'
      f'<div style="font-family:{t["display"]};font-weight:600;font-size:19px;{disp_it}">Mollie Yoga</div><div>{nav}<span style="margin-left:18px;background:{t["accent"]};color:#fff;padding:5px 12px;border-radius:20px;font-weight:600">Book</span></div></div>'
      f'<div><div style="font-family:{t["display"]};font-weight:600;font-size:52px;line-height:.94;{disp_it}">{t["tag"]}</div>'
      f'<div style="font-family:{t["body"]};font-size:12px;margin-top:10px;opacity:.95;max-width:430px">In-person & online classes, corporate sessions and private 1:1s — for every body, in SE London and on Zoom.</div></div></div>')
    cards=""
    for title,desc,c in [("Classes & schedule","Self-running booking — drop in or book a block.",t["palette"][1][0]),
                         ("Corporate yoga","Bring calm and focus to your team, on-site or remote.",t["palette"][2][0]),
                         ("Private & 1:1","Tailored practice for your body and your goals.",t["accent2"])]:
        cards+=(f'<div style="flex:1;background:{c};color:#fff;border-radius:12px;padding:16px;min-height:120px;display:flex;flex-direction:column;justify-content:space-between">'
          f'<div style="font-family:{t["display"]};font-weight:600;font-size:18px;line-height:1.0;{disp_it}">{title}</div>'
          f'<div style="font-family:{t["body"]};font-size:10.5px;opacity:.92;line-height:1.35">{desc}</div></div>')
    body=f'<div style="background:{t["paper"]};padding:18px 24px;display:flex;gap:12px">{cards}</div>'
    desktop=(f'<div class="browser" style="width:660px"><div class="bar"><span class="dot" style="background:#e0564a"></span><span class="dot" style="background:#ecae3e"></span><span class="dot" style="background:#5bbd57"></span><span class="url">www.mollie.yoga</span></div>{hero}{body}</div>')
    mrows="".join(f'<div style="display:flex;justify-content:space-between;align-items:center;border:1px solid rgba(0,0,0,.10);border-radius:9px;padding:8px 10px;margin-bottom:7px"><div><b>{d}</b><div style="opacity:.6">{x}</div></div><span style="background:{t["accent"]};color:#fff;border-radius:16px;padding:3px 9px;font-weight:600;font-size:8.5px">Book</span></div>' for d,x in [("Slow Flow","Thu 6.00pm · Studio"),("Vinyasa","Sat 10am · Online"),("Yin","Sun 5pm · Studio")])
    mphone=(f'<div class="phone" style="width:188px;height:394px"><div class="notch"></div><div class="screen" style="background:{t["paper"]}">'
      f'<div class="{t["field2"]} grain" style="height:150px;padding:14px;color:#fff;display:flex;flex-direction:column;justify-content:flex-end">'
      f'<div style="font-family:{t["display"]};font-weight:600;font-size:24px;{disp_it}">Book a<br>class</div></div>'
      f'<div style="padding:12px 13px;font-family:{t["body"]};color:{t["ink"]};font-size:9.5px">{mrows}'
      f'<div style="margin-top:6px;font-size:8px;opacity:.6">Powered by your Wix scheduler & payments</div></div></div></div>')
    inner=(f'<div style="position:absolute;inset:0;background:{t["paper"]}"></div><div class="paper-grain grain" style="position:absolute;inset:0"></div>'
      f'<div class="pad col">'
      f'<div class="row" style="justify-content:space-between;align-items:baseline">'
      f'<div style="font-family:{t["display"]};font-weight:600;font-size:30px;color:{t["ink"]};{disp_it}">Website</div>'
      f'<div class="eyebrow" style="color:{t["soft"]}">on Wix · home · classes · corporate · private · philosophy</div></div>'
      f'<div style="height:20px"></div>'
      f'<div class="row" style="gap:34px;align-items:flex-start">{desktop}<div class="col" style="gap:12px">{mphone}</div></div>'
      f'<div style="font-family:{t["body"]};font-size:11.5px;color:{t["soft"]};margin-top:18px;max-width:900px">Built on your existing Wix Premium — keeps the inbuilt scheduler, payments and Zoom links. Same five-section structure across all three directions; only the brand world changes.</div>'
      f'</div>')
    return page("web", inner, foot=f"DIRECTION {t['key']} · WEBSITE")

def build_concept(t):
    return concept_cover(t)+identity_page(t)+instagram_page(t)+website_page(t)

# ============================================================ FRAMING PAGES
DATE="June 2026"

# the 19 board pins: (dominant_color, family-tag, orientation)
BOARD=[("#b7816e","clay","P"),("#a9a398","greige","P"),("#c6c6c4","stone","L"),("#020203","onyx","P"),
("#f1ece8","cream","L"),("#909090","grey","P"),("#cdc4b9","sand","P"),("#cfaa7b","camel","P"),
("#929292","grey","P"),("#5a4f49","taupe","P"),("#eae7dc","ecru","P"),("#d6dbc3","sage","P"),
("#645c54","taupe","S"),("#7f9fc2","dusty blue","P"),("#e2e1dc","mist","P"),("#c0c0bf","stone","L"),
("#140d08","espresso","L"),("#503e26","umber","P"),("#6e3e18","sienna","L")]

def cover():
    inner=(f'<div class="c1-field grain" style="position:absolute;inset:0"></div>'
      f'<div style="position:absolute;top:58px;right:72px;z-index:12">{soma_stamp("#F1ECE8",146)}</div>'
      f'<div class="pad col" style="justify-content:space-between">'
      f'<div class="eyebrow" style="color:rgba(255,255,255,.92)">Brand & Visual Direction · v2 · {DATE}</div>'
      f'<div><div style="font-family:Bricolage;font-weight:700;color:#fff;font-size:130px;line-height:.84;letter-spacing:-.025em">Mollie<br>Yoga</div>'
      f'<div style="font-family:DM Sans;color:#fff;font-size:21px;margin-top:24px;opacity:.95">Three directions, rebuilt from your Pinterest board — warm, earthy, and pulled further apart.</div></div>'
      f'<div class="row" style="gap:14px;align-items:center;color:#fff;font-family:DM Sans;font-size:13px">'
      f'<span style="opacity:.85">01 Studio Soma</span><span style="opacity:.5">·</span>'
      f'<span style="opacity:.85">02 Nalu</span><span style="opacity:.5">·</span>'
      f'<span style="opacity:.85">03 Grove</span></div></div>')
    return page("cover", inner, foot="", num_label="—")

def board_page():
    tiles=""
    for hx,fam,o in BOARD:
        dark = int(hx[1:3],16)*0.299+int(hx[3:5],16)*0.587+int(hx[5:7],16)*0.114 < 140
        tc="#fff" if dark else "#16110c"
        tiles+=(f'<div style="background:{hx};border-radius:9px;height:84px;display:flex;flex-direction:column;justify-content:flex-end;padding:8px;color:{tc}">'
          f'<div style="font-family:DM Sans;font-weight:600;font-size:9.5px">{fam}</div>'
          f'<div style="font-family:Space Mono;font-size:8px;opacity:.8">{hx}</div></div>')
    refs=[("Studio Soma","“bright, uplifting… warm feel-good palette, playful logo suite” → Direction 01"),
          ("nalu","“brand mark over dynamic photography, fluidity, graphic overlay” → Direction 02"),
          ("Behance — yoga identity","reference collection of grounded, natural identities → Direction 03")]
    rl="".join(f'<div style="border-top:1.4px solid #2A2117;padding-top:8px;margin-bottom:13px"><div style="font-family:DM Sans;font-weight:700;font-size:13px;color:#2A2117">{a}</div><div style="font-family:DM Sans;font-size:11px;color:#6a6450;margin-top:3px;line-height:1.35">{b}</div></div>' for a,b in refs)
    inner=(f'<div style="position:absolute;inset:0;background:#EAE7DC"></div><div class="paper-grain grain" style="position:absolute;inset:0"></div>'
      f'<div class="pad col">'
      f'<div class="eyebrow" style="color:#6a6450">The Mollie Yoga board → palette</div>'
      f'<div style="font-family:Spectral;font-size:40px;color:#2A2117;margin-top:8px;line-height:1.0">What the board actually says</div>'
      f'<div style="font-family:DM Sans;font-size:12.5px;color:#6a6450;margin-top:9px;max-width:880px;line-height:1.5">Dominant colours extracted from all 19 pins. The board reads <b>warm, earthy and tonal</b> — clay, camel, cream, taupe and espresso — with two accent notes: a soft <b>sage</b> and a single <b>dusty blue</b>. Each direction below is built from a different cluster of these, so they pull apart instead of blurring together.</div>'
      f'<div style="height:20px"></div>'
      f'<div class="row" style="gap:38px;align-items:flex-start">'
      f'<div style="flex:1.6;display:grid;grid-template-columns:repeat(7,1fr);gap:7px">{tiles}</div>'
      f'<div style="flex:1"><div class="eyebrow" style="color:#6a6450;margin-bottom:12px">Named references on the board</div>{rl}'
      f'<div style="font-family:DM Sans;font-size:10.5px;color:#8a8470;line-height:1.4;margin-top:4px">Note: the pin photography itself can’t be embedded from this environment — these palettes and the cited references are extracted directly from the board’s live data.</div></div>'
      f'</div></div>')
    return page("board", inner, foot="BOARD → PALETTE")

def overview():
    dirs=[("01","Studio Soma","Bright warm earth · playful bold","c1-field"),
          ("02","Nalu","Greige editorial + dusty blue · fluid","c2-field"),
          ("03","Grove","Sage / ecru / umber · natural calm","c3-field")]
    dd="".join(f'<div class="{cl} grain" style="flex:1;border-radius:13px;height:150px;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:space-between;padding:16px;color:#fff">'
      f'<div class="eyebrow" style="font-size:9px">DIRECTION {k}</div>'
      f'<div><div style="font-family:Spectral;font-size:27px;line-height:1">{n}</div>'
      f'<div style="font-family:DM Sans;font-size:10.5px;opacity:.92;margin-top:3px">{d}</div></div></div>' for k,n,d,cl in dirs)
    pts=[("Built from the board","Every palette, type choice and mark traces back to a cluster of your saved pins."),
         ("Pulled further apart","Warm-bright vs tonal-editorial vs natural-calm — distinct colour, type and layout, not three shades of one idea."),
         ("Warm & earthy, with backbone","Following the board means warm neutrals and a touch of sage — kept from going sleepy with deep umber, flame and a dusty-blue accent.")]
    pl="".join(f'<div style="border-top:1.5px solid #2A2117;padding-top:9px"><div style="font-family:DM Sans;font-weight:700;font-size:14px;color:#2A2117">{a}</div><div style="font-family:DM Sans;font-size:11.5px;color:#6a6450;margin-top:4px;line-height:1.4">{b}</div></div>' for a,b in pts)
    inner=(f'<div style="position:absolute;inset:0;background:#EAE7DC"></div><div class="paper-grain grain" style="position:absolute;inset:0"></div>'
      f'<div class="pad col">'
      f'<div class="eyebrow" style="color:#6a6450">How to read this deck · v2</div>'
      f'<div style="font-family:Spectral;font-size:42px;color:#2A2117;margin-top:8px;line-height:1.0">Three directions, from your board</div>'
      f'<div style="font-family:DM Sans;font-size:12.5px;color:#6a6450;margin-top:10px;max-width:800px;line-height:1.5">You felt the first round was too similar and didn’t lean on your references enough. This version rebuilds all three from the Mollie Yoga board — warmer, earthier, and clearly distinct.</div>'
      f'<div style="height:22px"></div>'
      f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px 38px">{pl}</div>'
      f'<div style="height:26px"></div>'
      f'<div class="row" style="gap:18px">{dd}</div></div>')
    return page("overview", inner, foot="THE BRIEF · v2")

def closing():
    qs=["Which direction feels most <i>you</i> — Studio Soma’s warmth, Nalu’s editorial cool, or Grove’s calm?",
        "Now I have the colours from the board: want me to commission/shoot photography to match the chosen world?",
        "Brand mark: sun (Soma), wave (Nalu) or sprig (Grove) — and wordmark vs initials as your main tag?",
        "Anything from the board I’ve under- or over-weighted before I refine one route?"]
    ql="".join(f'<div style="display:flex;gap:14px;align-items:flex-start;margin-bottom:14px"><div style="font-family:Spectral;font-style:italic;font-size:22px;color:#D6DBC3;line-height:1">{i+1}</div><div style="font-family:DM Sans;font-size:15px;color:#fff;line-height:1.4;max-width:640px">{q}</div></div>' for i,q in enumerate(qs))
    inner=(f'<div class="c3-field grain" style="position:absolute;inset:0"></div>'
      f'<div class="pad col" style="justify-content:space-between">'
      f'<div class="eyebrow" style="color:rgba(255,255,255,.9)">Next step · let’s talk</div>'
      f'<div><div style="font-family:Spectral;font-size:46px;color:#fff;line-height:1.0;margin-bottom:26px">A few things to react to</div>{ql}</div>'
      f'<div style="font-family:DM Sans;font-size:13px;color:rgba(255,255,255,.85)">Pick a lane and I’ll take one direction to a finished system — wordmark, templates and a Wix build — for the July 6 timeline.</div></div>')
    return page("closing", inner, foot="MOLLIE YOGA · BRAND CONCEPTS v2", num_label="—")

# ============================================================ ASSEMBLE
HEAD=('<!doctype html><html><head><meta charset="utf-8">'
  '<link rel="stylesheet" href="css/deck.css"><style>'+CSS+'</style></head><body>')
pages = cover()+overview()+board_page()+build_concept(C1)+build_concept(C2)+build_concept(C3)+closing()
with open("deck/index.html","w") as f:
    f.write(HEAD+pages+"</body></html>")
print("wrote deck/index.html ; pages =", PAGE)
