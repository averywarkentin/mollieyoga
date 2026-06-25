#!/usr/bin/env python3
# Generates deck/index.html — Mollie Yoga brand concepts deck.
import html

# ---------------------------------------------------------------- helpers
def swatch(hx, nm, role, dark=False):
    tc = "#fff" if dark else "#11110f"
    sc = "rgba(255,255,255,.78)" if dark else "rgba(0,0,0,.6)"
    return (f'<div class="sw" style="background:{hx};color:{tc}">'
            f'<div class="nm">{nm}</div>'
            f'<div class="hx" style="color:{sc}">{hx}</div></div>')

def igcell(inner, bg=""):
    return f'<div class="igcell" style="{bg}">{inner}</div>'

PAGE = 0
def page(cls, inner, foot="MOLLIE YOGA", num_label=""):
    global PAGE; PAGE += 1
    pn = f'<div class="pagenum">{num_label or PAGE:02}</div>' if num_label != "—" else ""
    ft = f'<div class="tag-foot">{foot}</div>' if foot else ""
    return f'<section class="page {cls}">{inner}{ft}{pn}</section>'

# wavy textPath used for "type that follows the body" curved captions
def curved_text(text, pid, fill, size=20, ls="0.04em", family="Fraunces", weight=500, italic=False, d=None, vb="0 0 360 220", w=360, h=220, startOffset="50%"):
    d = d or "M20,150 C90,40 270,40 340,150"
    st = "italic" if italic else "normal"
    return (f'<svg viewBox="{vb}" width="{w}" height="{h}" style="overflow:visible">'
            f'<defs><path id="{pid}" d="{d}" fill="none"/></defs>'
            f'<text font-family="{family}" font-weight="{weight}" font-style="{st}" '
            f'font-size="{size}" letter-spacing="{ls}" fill="{fill}">'
            f'<textPath href="#{pid}" startOffset="{startOffset}" text-anchor="middle">{text}</textPath></text></svg>')

# ============================================================ CSS (themes)
CSS = r"""
/* ---- abstract gradient fields (stand in for photography) ---- */
.c1-aurora{background:
 radial-gradient(120% 95% at 10% 16%, #1C7C7A 0%, transparent 52%),
 radial-gradient(120% 100% at 88% 10%, #2E5BD6 0%, transparent 52%),
 radial-gradient(135% 115% at 80% 96%, #7140C2 0%, transparent 55%),
 radial-gradient(120% 115% at 16% 98%, #0E3B32 0%, transparent 58%),
 radial-gradient(55% 55% at 64% 58%, #F4A23E 0%, transparent 42%),
 linear-gradient(118deg,#0E3B32,#173c6b 55%,#3c2a78);}
.c1-aurora2{background:
 radial-gradient(100% 90% at 80% 22%, #2E5BD6 0%, transparent 55%),
 radial-gradient(110% 100% at 14% 84%, #1C7C7A 0%, transparent 55%),
 radial-gradient(90% 90% at 88% 90%, #8A5CD1 0%, transparent 55%),
 radial-gradient(50% 50% at 30% 22%, #F4A23E 0%, transparent 45%),
 linear-gradient(150deg,#10463a,#243a73 60%,#46307f);}

.c2-field{background:
 radial-gradient(100% 90% at 82% 18%, #16575E 0%, transparent 54%),
 radial-gradient(110% 100% at 16% 10%, #3E2147 0%, transparent 55%),
 radial-gradient(120% 115% at 90% 96%, #C24A2C 0%, transparent 52%),
 radial-gradient(80% 80% at 30% 84%, #5E6B33 0%, transparent 56%),
 radial-gradient(45% 45% at 60% 50%, #EE7A2E 0%, transparent 42%),
 linear-gradient(135deg,#1F3D2B,#182f2c 58%,#2c1731);}
.c2-field2{background:
 radial-gradient(110% 95% at 18% 16%, #16575E 0%, transparent 55%),
 radial-gradient(120% 110% at 86% 92%, #C24A2C 0%, transparent 52%),
 radial-gradient(80% 80% at 78% 16%, #3E2147 0%, transparent 55%),
 linear-gradient(120deg,#1c3826,#251433);}

.c3-duo{background:
 radial-gradient(120% 100% at 80% 18%, #2952CC 0%, transparent 60%),
 radial-gradient(110% 100% at 16% 90%, #1E7A55 0%, transparent 58%),
 radial-gradient(90% 90% at 90% 96%, #4B2E83 0%, transparent 55%),
 radial-gradient(60% 60% at 40% 26%, #F2762E 0%, transparent 48%),
 linear-gradient(135deg,#2643a8,#284a86 55%,#3f2a73);}
"""

# ============================================================ BRAND MARKS
# ---- Concept 1 : flowing single-line breath monogram + stamp
def c1_breath(stroke="#F4F1EA", sw=7, w=150, h=110):
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 150 110" fill="none">'
      f'<path d="M14,86 C14,40 30,22 46,22 C64,22 64,70 75,70 C86,70 86,22 104,22 '
      f'C120,22 136,40 136,86" stroke="{stroke}" stroke-width="{sw}" '
      f'stroke-linecap="round" stroke-linejoin="round"/>'
      f'<path d="M6,96 C46,80 104,80 144,96" stroke="{stroke}" stroke-width="{sw*0.62:.1f}" '
      f'stroke-linecap="round" opacity="0.65"/></svg>')

def c1_stamp(col="#F4F1EA", size=158):
    r=size/2
    txt="MOLLIE YOGA · MOVE WITH THE BREATH · "
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
      f'<defs><path id="c1ring" fill="none" d="M{r},{r} m-{r-15},0 a{r-15},{r-15} 0 1,1 {2*(r-15)},0 a{r-15},{r-15} 0 1,1 -{2*(r-15)},0"/></defs>'
      f'<text font-family="Space Grotesk" font-weight="500" font-size="11" letter-spacing="0.18em" fill="{col}">'
      f'<textPath href="#c1ring" startOffset="0">{txt}</textPath></text>'
      f'<g transform="translate({r-26},{r-22}) scale(0.34)">'
      f'<path d="M14,86 C14,40 30,22 46,22 C64,22 64,70 75,70 C86,70 86,22 104,22 C120,22 136,40 136,86" '
      f'stroke="{col}" stroke-width="9" fill="none" stroke-linecap="round"/></g></svg>')

# ---- Concept 2 : sun / horizon glyph + bold stack
def c2_sun(col="#EE7A2E", w=120, h=120):
    rays=""
    import math
    for i in range(11):
        a=math.pi*(0.04+ i*(0.92/10))  # arc above horizon
        x1=60+38*math.cos(a); y1=70-38*math.sin(a)
        x2=60+50*math.cos(a); y2=70-50*math.sin(a)
        rays+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="3.4" stroke-linecap="round"/>'
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 120 110">'
      f'<path d="M28,70 a32,32 0 0,1 64,0 Z" fill="{col}"/>'
      f'{rays}'
      f'<line x1="14" y1="70" x2="106" y2="70" stroke="{col}" stroke-width="4.4" stroke-linecap="round"/></svg>')

# ---- Concept 3 : talisman seal w/ prayer-hands + starburst, plus star motif
def star8(col, size=70, cx=35, cy=35):
    import math
    pts=[]
    for i in range(16):
        r = (size/2) if i%2==0 else (size/2)*0.4
        a=math.pi/8*i - math.pi/2
        pts.append(f"{cx+r*math.cos(a):.1f},{cy+r*math.sin(a):.1f}")
    return f'<svg width="{size}" height="{size}" viewBox="0 0 {2*cx} {2*cy}"><polygon points="{" ".join(pts)}" fill="{col}"/></svg>'

def prayer(col, w=70, h=92):
    # two symmetric petals meeting at top = hands in prayer / lotus bud
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 70 92">'
      f'<path d="M35,8 C20,30 18,58 30,82 L35,86 L35,8Z" fill="{col}"/>'
      f'<path d="M35,8 C50,30 52,58 40,82 L35,86 L35,8Z" fill="{col}" opacity="0.82"/>'
      f'<path d="M22,80 C28,72 42,72 48,80" stroke="{col}" stroke-width="3.4" fill="none" stroke-linecap="round"/></svg>')

def c3_seal(col="#F6EFE0", ink="#2952CC", size=176):
    r=size/2
    txt="· YOGA · WITH · MOLLIE · NAMASTE "
    rays=""
    import math
    for i in range(24):
        a=2*math.pi*i/24
        x1=r+ (r-30)*math.cos(a); y1=r+(r-30)*math.sin(a)
        x2=r+ (r-22)*math.cos(a); y2=r+(r-22)*math.sin(a)
        rays+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="2" opacity="0.8"/>'
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
      f'<circle cx="{r}" cy="{r}" r="{r-2}" fill="{ink}"/>'
      f'<defs><path id="c3ring" fill="none" d="M{r},{r} m-{r-12},0 a{r-12},{r-12} 0 1,1 {2*(r-12)},0 a{r-12},{r-12} 0 1,1 -{2*(r-12)},0"/></defs>'
      f'<text font-family="Space Mono" font-weight="700" font-size="11" letter-spacing="0.12em" fill="{col}">'
      f'<textPath href="#c3ring" startOffset="0">{txt}</textPath></text>'
      f'{rays}'
      f'<g transform="translate({r-23},{r-30}) scale(0.62)">'
      f'<path d="M35,8 C20,30 18,58 30,82 L35,86 L35,8Z" fill="{col}"/>'
      f'<path d="M35,8 C50,30 52,58 40,82 L35,86 L35,8Z" fill="{col}" opacity="0.78"/>'
      f'<path d="M22,80 C28,72 42,72 48,80" stroke="{col}" stroke-width="3.4" fill="none" stroke-linecap="round"/></g></svg>')

def yinyang(a,b,size=58):
    r=size/2
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 100 100">'
      f'<circle cx="50" cy="50" r="49" fill="{a}"/>'
      f'<path d="M50,1 a49,49 0 0,1 0,98 a24.5,24.5 0 0,1 0,-49 a24.5,24.5 0 0,0 0,-49Z" fill="{b}"/>'
      f'<circle cx="50" cy="25.5" r="8" fill="{a}"/><circle cx="50" cy="74.5" r="8" fill="{b}"/></svg>')

# ============================================================ THEMES
C1 = dict(key="01", name="In Flow", tag="Move with the breath.",
    display="Fraunces", body="Space Grotesk", quote="Fraunces",
    paper="#F2F1EA", ink="#15271f", soft="#5b6b62",
    field="c1-aurora", field2="c1-aurora2", duo="c1-aurora2",
    accent="#F4A23E", accent2="#2E5BD6",
    mark=lambda c="#F2F1EA": c1_breath(c),
    palette=[("#0E3B32","Deep Pine","anchor",1),("#1C7C7A","Tidal Teal","primary",1),
             ("#2E5BD6","Lapis Blue","primary",1),("#6E3FB0","Iris Violet","primary",1),
             ("#8A5CD1","Amethyst","secondary",1),("#F4A23E","Amber Flare","highlight",0),
             ("#F2F1EA","Mist Paper","base",0)],
    note="Aurora gradients flow green → blue → violet, warmed by a single amber. Dreamy, watery, kinetic — your photos drop straight into these fields.")

C2 = dict(key="02", name="Earth & Ember", tag="Rooted in earth. Lit by fire.",
    display="Bricolage", body="Bricolage", quote="Spectral",
    paper="#ECE3D2", ink="#211a12", soft="#6f6552",
    field="c2-field", field2="c2-field2", duo="c2-field2",
    accent="#EE7A2E", accent2="#C24A2C",
    mark=lambda c="#EE7A2E": c2_sun(c),
    palette=[("#1F3D2B","Forest","anchor",1),("#5E6B33","Moss","primary",1),
             ("#16575E","Deep Teal","primary",1),("#3E2147","Aubergine","primary",1),
             ("#C24A2C","Clay","secondary",1),("#EE7A2E","Ember","highlight",0),
             ("#ECE3D2","Bone","base",0)],
    note="Deep earth tones — forest, moss, teal, aubergine — struck through with ember orange. Bold and grounded, with a bit of fire and challenge. The elemental chips below map to how you theme classes.")

C3 = dict(key="03", name="Talisman", tag="An old practice, your way.",
    display="Syne", body="DM Sans", quote="Syne",
    paper="#F6EFE0", ink="#171310", soft="#736b5b",
    field="c3-duo", field2="c3-duo", duo="c3-duo",
    accent="#F2762E", accent2="#2952CC",
    mark=lambda c="#2952CC": c3_seal(ink=c),
    palette=[("#2952CC","Cobalt","primary",1),("#1E7A55","Viridian","primary",1),
             ("#4B2E83","Deep Violet","primary",1),("#F2762E","Sunburst","highlight",0),
             ("#F4B33C","Marigold","secondary",0),("#F6EFE0","Cream","base",0),
             ("#171310","Ink","anchor",1)],
    note="Bold flat colour-blocking and symbolic marks — prayer hands, sun, yin-yang, eight-point stars — drawn modern, never whimsical. Folk-poster energy in colours this space never uses.")

# ============================================================ IG CONTENT BLOCKS
def ig_announce(t, small=False):
    fs = "scale(.62)" if small else ""
    return (f'<div class="{t["field"]} grain" style="position:absolute;inset:0;"></div>'
      f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:space-between;padding:13px;color:#fff;z-index:5">'
      f'<div class="eyebrow" style="font-size:8px;letter-spacing:.3em;opacity:.92">NEW CLASS</div>'
      f'<div><div style="font-family:{t["display"]};font-weight:600;font-size:25px;line-height:.96;{"font-style:italic" if t["display"]=="Fraunces" else ""}">Slow<br>Flow</div>'
      f'<div style="font-family:{t["body"]};font-size:9px;letter-spacing:.04em;margin-top:6px;opacity:.95">Thursdays · 6.00pm<br>Abbey Wood, SE</div></div></div>')

def ig_schedule(t):
    days=[("MON","Vinyasa · 7am"),("TUE","—"),("WED","Slow Flow · 6pm"),("THU","Yin · 6pm"),("FRI","Hatha · 9am"),("SAT","Community · 10am")]
    rows="".join(f'<div style="display:flex;justify-content:space-between;border-bottom:1px solid rgba(0,0,0,.10);padding:4.5px 0"><span style="font-weight:600">{d}</span><span style="opacity:.7">{c}</span></div>' for d,c in days)
    return (f'<div style="position:absolute;inset:0;background:{t["paper"]};color:{t["ink"]};padding:13px 14px;z-index:5;font-family:{t["body"]};font-size:8.5px">'
      f'<div style="font-family:{t["display"]};font-weight:600;font-size:17px;margin-bottom:9px;{"font-style:italic" if t["display"]=="Fraunces" else ""}">This week</div>{rows}</div>')

def ig_quote(t, q='"When disturbed by negative thoughts, opposite ones should be thought of."', cite="Yoga Sutras 2.33"):
    cap = curved_text("· breathe · soften · return ·","qc"+str(id(q))[-4:], t["accent"], size=11, family=t["body"], weight=600, d="M30,120 C100,60 260,60 330,120", w=200, h=70)
    return (f'<div class="{t["field2"]} grain" style="position:absolute;inset:0;"></div>'
      f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;padding:18px;z-index:5">'
      f'<div style="font-family:{t["quote"]};{"font-style:italic;" if t["quote"] in ("Fraunces","Spectral") else ""}font-weight:{500 if t["quote"]!="Syne" else 700};color:#fff;font-size:15px;line-height:1.22;text-align:center">{q}</div></div>'
      f'<div style="position:absolute;bottom:11px;left:0;right:0;text-align:center;color:rgba(255,255,255,.85);font-family:{t["body"]};font-size:8px;letter-spacing:.16em;z-index:6">{cite.upper()}</div>')

def ig_retreat(t):
    return (f'<div class="{t["duo"]} grain" style="position:absolute;inset:0;"></div>'
      f'<div style="position:absolute;inset:0;border:1px solid rgba(255,255,255,.4);margin:9px;z-index:6"></div>'
      f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;text-align:center;color:#fff;z-index:5;padding:14px">'
      f'<div class="eyebrow" style="font-size:8px;opacity:.9">DAY RETREAT</div>'
      f'<div style="font-family:{t["display"]};font-weight:{600 if t["display"]!="Syne" else 800};font-size:24px;line-height:.98;margin:8px 0;{"font-style:italic" if t["display"]=="Fraunces" else ""}">Autumn<br>Reset</div>'
      f'<div style="font-family:{t["body"]};font-size:9px;letter-spacing:.05em;opacity:.95">SAT 12 OCT · 10–4<br>+ tea, sound, stillness</div></div>')

def ig_life(t, lbl="on the mat"):
    return (f'<div class="{t["field"]} grain" style="position:absolute;inset:0;filter:saturate(1.05)"></div>'
      f'<div style="position:absolute;bottom:11px;left:12px;color:#fff;font-family:{t["quote"]};{"font-style:italic" if t["quote"] in ("Fraunces","Spectral") else ""}font-size:14px;z-index:5;text-shadow:0 1px 8px rgba(0,0,0,.35)">{lbl}</div>')

def profile_grid(t):
    cells=[ig_announce(t), ig_quote(t), ig_life(t,"breath"),
           ig_schedule(t), ig_life(t,"studio light"), ig_retreat(t),
           ig_quote(t,'"You become what you believe you can become."','Bhagavad Gita'), ig_announce(t), ig_life(t,"after savasana"),
           ig_retreat(t), ig_schedule(t), ig_life(t,"morning")]
    return "".join(f'<div class="igcell">{c}</div>' for c in cells)

# ============================================================ PAGE TEMPLATES
def concept_cover(t):
    big = f'<div style="font-family:{t["display"]};color:#fff;font-weight:{600 if t["display"]!="Syne" else 800};font-size:128px;line-height:.84;letter-spacing:-.02em;{"font-style:italic" if t["display"]=="Fraunces" else ""}">Mollie<br>Yoga</div>'
    markbig = f'<div style="position:absolute;top:54px;right:70px;z-index:12">{t["mark"]("#fff") if t["key"]!="03" else c3_seal(col="#F6EFE0", ink="#F2762E")}</div>'
    inner=(f'<div class="{t["field"]} grain" style="position:absolute;inset:0"></div>'
      f'{markbig}'
      f'<div class="pad col" style="justify-content:space-between">'
      f'<div class="row" style="justify-content:space-between;align-items:flex-start">'
      f'<div class="eyebrow" style="color:rgba(255,255,255,.9)">Direction {t["key"]} / Three</div></div>'
      f'<div>{big}'
      f'<div style="font-family:{t["body"]};color:#fff;font-size:24px;margin-top:26px;letter-spacing:.01em;opacity:.95;{"font-style:italic;font-family:"+t["quote"] if t["quote"] in ("Fraunces","Spectral") else ""}">{t["tag"]}</div></div>'
      f'<div class="row" style="justify-content:space-between;align-items:flex-end;color:rgba(255,255,255,.85);font-family:{t["body"]};font-size:13px;letter-spacing:.04em">'
      f'<div style="font-size:34px;font-family:{t["display"]};font-weight:{600 if t["display"]!="Syne" else 800};{"font-style:italic" if t["display"]=="Fraunces" else ""}">{t["name"]}</div>'
      f'<div style="text-align:right;max-width:360px;opacity:.92">{t["note"]}</div></div></div>')
    return page(t["field"], inner, foot=f"DIRECTION {t['key']} · {t['name'].upper()}")

def identity_page(t):
    sw="".join(swatch(hx,nm,role,bool(d)) for hx,nm,role,d in t["palette"])
    # type specimen
    disp_style = "font-style:italic;" if t["display"]=="Fraunces" else ""
    spec=(f'<div style="font-family:{t["display"]};font-weight:{600 if t["display"]!="Syne" else 800};font-size:62px;line-height:.92;color:{t["ink"]};{disp_style}">Aa Gg</div>'
      f'<div style="font-family:{t["display"]};font-size:13px;letter-spacing:.04em;color:{t["soft"]};margin-top:6px">{t["display"]} — display & headlines</div>'
      f'<div style="font-family:{t["quote"]};{"font-style:italic;" if t["quote"] in ("Fraunces","Spectral") else ""}font-size:23px;color:{t["ink"]};margin-top:22px;line-height:1.2">“Live your own destiny, imperfectly.”</div>'
      f'<div style="font-family:{t["body"]};font-size:13px;letter-spacing:.04em;color:{t["soft"]};margin-top:6px">{t["quote"]} — philosophy & quotes</div>'
      f'<div style="font-family:{t["body"]};font-size:13.5px;line-height:1.5;color:{t["ink"]};margin-top:22px;max-width:420px">The quick brown fox. Body copy, schedules, captions and buttons sit in {t["body"]} — clean, legible, modern. ABCDEFGHIJKLM 0123456789</div>')
    # brand marks panel (on a dark field)
    if t["key"]=="03":
        marks=(f'<div style="display:flex;gap:24px;align-items:center">{c3_seal(ink=t["accent2"],size=146)}'
          f'<div style="display:flex;flex-direction:column;gap:12px">{star8(t["accent"],46)}{yinyang(t["accent2"],t["accent"],44)}{prayer(t["accent2"],40,50)}</div></div>')
        wordmk=f'<div style="font-family:Syne;font-weight:800;font-size:42px;color:#fff;letter-spacing:-.01em">Mollie</div>'
    elif t["key"]=="02":
        marks=(f'<div style="display:flex;gap:34px;align-items:center">{c2_sun(t["accent"],112,110)}'
          f'<div style="font-family:Bricolage;font-weight:800;color:#fff;font-size:52px;line-height:.82;letter-spacing:-.01em">MY<br><span style="font-size:18px;font-weight:600;letter-spacing:.18em">YOGA</span></div></div>')
        wordmk=f'<div style="font-family:Bricolage;font-weight:800;font-size:50px;color:#fff;letter-spacing:-.02em">MOLLIE</div>'
    else:
        marks=(f'<div style="display:flex;gap:34px;align-items:center">{c1_breath("#F2F1EA",7,140,104)}{c1_stamp("#F2F1EA",132)}</div>')
        wordmk=f'<div style="font-family:Fraunces;font-style:italic;font-weight:600;font-size:52px;color:#fff">Mollie</div>'
    inner=(f'<div style="position:absolute;inset:0;background:{t["paper"]}"></div><div class="paper-grain grain" style="position:absolute;inset:0"></div>'
      f'<div class="pad col" style="gap:0">'
      f'<div class="row" style="justify-content:space-between;align-items:baseline">'
      f'<div style="font-family:{t["display"]};font-weight:{600 if t["display"]!="Syne" else 800};font-size:30px;color:{t["ink"]};{disp_style}">Identity system</div>'
      f'<div class="eyebrow" style="color:{t["soft"]}">{t["name"]} · palette · type · mark</div></div>'
      f'<div style="height:22px"></div>'
      f'<div class="swatches" style="box-shadow:0 16px 40px -24px rgba(0,0,0,.4)">{sw}</div>'
      f'<div style="height:30px"></div>'
      f'<div class="row" style="gap:48px">'
      f'<div style="flex:1.15">{spec}</div>'
      f'<div style="flex:1;border-radius:16px;padding:26px;display:flex;flex-direction:column;justify-content:space-between;gap:18px;" class="{t["field"]}">'
      f'<div class="eyebrow" style="color:rgba(255,255,255,.85)">Brand marks · the “little tag”</div>'
      f'{marks}{wordmk}'
      f'<div style="font-family:{t["body"]};font-size:11px;color:rgba(255,255,255,.85);letter-spacing:.03em">Works as a stamp on photos, a profile picture, and a sign-off on stories.</div></div>'
      f'</div></div>')
    return page("ident", inner, foot=f"DIRECTION {t['key']} · IDENTITY")

def instagram_page(t):
    disp_style="font-style:italic;" if t["display"]=="Fraunces" else ""
    # profile phone — sized so 4 rows of 3 fill the screen with no dead space
    head=(f'<div style="display:flex;align-items:center;gap:9px;padding:9px 11px 8px">'
      f'<div style="width:38px;height:38px;border-radius:50%;overflow:hidden;position:relative" class="{t["field"]} grain"></div>'
      f'<div style="font-family:{t["body"]};font-size:10.5px;color:{t["ink"]};line-height:1.2"><b>mollie.yoga</b><div style="opacity:.6;font-size:8px">Yoga in SE London · classes, corporate & private</div></div></div>')
    phone1=(f'<div class="phone" style="width:262px;height:430px"><div class="notch"></div>'
      f'<div class="screen" style="background:{t["paper"]}">{head}'
      f'<div class="iggrid" style="grid-template-rows:repeat(4,1fr);gap:2px;height:360px">{profile_grid(t)}</div></div></div>')
    # story phones — each builds its own background layer so nothing is overridden
    def story(layers):
        return f'<div class="phone" style="width:154px;height:326px"><div class="screen" style="background:{t["paper"]}">{layers}</div></div>'
    s1=story(f'<div class="{t["field2"]} grain" style="position:absolute;inset:0"></div>'
        f'<div style="position:absolute;inset:0;color:#fff;padding:16px;display:flex;flex-direction:column;justify-content:space-between;z-index:5">'
        f'<div class="eyebrow" style="font-size:8px">THIS WEEK · COVER</div>'
        f'<div><div style="font-family:{t["display"]};font-weight:{600 if t["display"]!="Syne" else 800};font-size:27px;line-height:.95;{disp_style}">Subbing<br>Wed Yin</div>'
        f'<div style="font-family:{t["body"]};font-size:9px;margin-top:8px;opacity:.95">6.00pm · Abbey Wood<br>covering for Sam</div></div>'
        f'<div style="transform:scale(.42);transform-origin:left;height:30px">{t["mark"]("#fff") if t["key"]!="03" else star8("#fff",30)}</div></div>')
    s2=story(f'<div style="position:absolute;inset:0;background:{t["paper"]};color:{t["ink"]};padding:16px;display:flex;flex-direction:column;justify-content:space-between;z-index:5">'
        f'<div class="eyebrow" style="font-size:8px;color:{t["soft"]}">REFLECTION</div>'
        f'<div style="font-family:{t["quote"]};{"font-style:italic;" if t["quote"] in ("Fraunces","Spectral") else ""}font-size:17px;line-height:1.28">Friendliness toward the happy, compassion for the unhappy.</div>'
        f'<div style="transform:scale(.5);transform-origin:left;height:26px">{t["mark"](t["accent2"]) if t["key"]!="03" else prayer(t["accent2"],34,44)}</div></div>')
    s3=story(f'<div class="{t["duo"]} grain" style="position:absolute;inset:0"></div>'
        f'<div style="position:absolute;inset:0;z-index:5;color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:16px">'
        f'<div style="width:44px;height:44px;border-radius:50%;border:2px solid #fff;display:flex;align-items:center;justify-content:center;margin-bottom:12px;font-family:{t["body"]};font-size:8.5px;letter-spacing:.1em">REEL</div>'
        f'<div style="font-family:{t["display"]};font-weight:{600 if t["display"]!="Syne" else 800};font-size:{18 if t["display"]=="Syne" else 22}px;line-height:1.0;{disp_style}">On the<br>philosophy</div>'
        f'<div style="font-family:{t["body"]};font-size:8.5px;margin-top:8px;opacity:.9;letter-spacing:.16em">EP. 01 · APARIGRAHA</div></div>')
    inner=(f'<div style="position:absolute;inset:0;background:{t["paper"]}"></div><div class="paper-grain grain" style="position:absolute;inset:0"></div>'
      f'<div class="pad col">'
      f'<div class="row" style="justify-content:space-between;align-items:baseline">'
      f'<div style="font-family:{t["display"]};font-weight:{600 if t["display"]!="Syne" else 800};font-size:30px;color:{t["ink"]};{disp_style}">Instagram system</div>'
      f'<div class="eyebrow" style="color:{t["soft"]}">grid · stories · reel cover</div></div>'
      f'<div style="height:16px"></div>'
      f'<div class="row" style="gap:36px;align-items:flex-start">'
      f'<div>{phone1}</div>'
      f'<div class="col" style="gap:16px">'
      f'<div class="row" style="gap:13px">{s1}{s2}{s3}</div>'
      f'<div style="font-family:{t["body"]};font-size:12px;line-height:1.5;color:{t["ink"]};max-width:430px">'
      f'<b>Five grid templates:</b> announcement · weekly schedule · quote · retreat poster · class &amp; life. '
      f'<b>Five story templates:</b> schedule swap · event invite · reflection (brand-mark sign-off) · testimonial · reel cover. '
      f'Curved captions trace the body; the mark tags everything so it reads as <i>yours</i> at a glance — never Canva.</div>'
      f'</div></div></div>')
    return page("ig", inner, foot=f"DIRECTION {t['key']} · INSTAGRAM")

def website_page(t):
    disp_style="font-style:italic;" if t["display"]=="Fraunces" else ""
    nav=" ".join(f'<span style="margin-left:18px;opacity:.85">{x}</span>' for x in ["Classes","Corporate","Private","Philosophy"])
    hero=(f'<div class="{t["field"]} grain" style="height:268px;position:relative;display:flex;flex-direction:column;justify-content:space-between;padding:18px 24px;color:#fff">'
      f'<div style="display:flex;justify-content:space-between;align-items:center;font-family:{t["body"]};font-size:11px">'
      f'<div style="font-family:{t["display"]};font-weight:{600 if t["display"]!="Syne" else 800};font-size:19px;{disp_style}">Mollie Yoga</div><div>{nav}<span style="margin-left:18px;background:{t["accent"]};color:#15110c;padding:5px 12px;border-radius:20px;font-weight:600">Book</span></div></div>'
      f'<div><div style="font-family:{t["display"]};font-weight:{600 if t["display"]!="Syne" else 800};font-size:54px;line-height:.92;{disp_style}">{t["tag"]}</div>'
      f'<div style="font-family:{t["body"]};font-size:12px;margin-top:10px;opacity:.95;max-width:430px">In-person & online classes, corporate sessions and private 1:1s — for every body, in SE London and on Zoom.</div></div></div>')
    cards=""
    for title,desc,c in [("Classes & schedule","Self-running booking — drop in or book a block.",t["palette"][0][0]),
                         ("Corporate yoga","Bring calm and focus to your team, on-site or remote.",t["palette"][1][0]),
                         ("Private & 1:1","Tailored practice for your body and your goals.",t["palette"][2][0])]:
        cards+=(f'<div style="flex:1;background:{c};color:#fff;border-radius:12px;padding:16px;min-height:120px;display:flex;flex-direction:column;justify-content:space-between">'
          f'<div style="font-family:{t["display"]};font-weight:{600 if t["display"]!="Syne" else 800};font-size:18px;line-height:1.0;{disp_style}">{title}</div>'
          f'<div style="font-family:{t["body"]};font-size:10.5px;opacity:.9;line-height:1.35">{desc}</div></div>')
    body=(f'<div style="background:{t["paper"]};padding:18px 24px;display:flex;gap:12px">{cards}</div>')
    desktop=(f'<div class="browser" style="width:660px"><div class="bar"><span class="dot" style="background:#e0564a"></span><span class="dot" style="background:#ecae3e"></span><span class="dot" style="background:#5bbd57"></span><span class="url">www.mollie.yoga</span></div>{hero}{body}</div>')
    # mobile booking phone
    mphone=(f'<div class="phone" style="width:188px;height:394px"><div class="notch"></div><div class="screen" style="background:{t["paper"]}">'
      f'<div class="{t["field2"]} grain" style="height:150px;padding:14px;color:#fff;display:flex;flex-direction:column;justify-content:flex-end">'
      f'<div style="font-family:{t["display"]};font-weight:{600 if t["display"]!="Syne" else 800};font-size:24px;{disp_style}">Book a<br>class</div></div>'
      f'<div style="padding:12px 13px;font-family:{t["body"]};color:{t["ink"]};font-size:9.5px">'
      + "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;border:1px solid rgba(0,0,0,.10);border-radius:9px;padding:8px 10px;margin-bottom:7px"><div><b>{d}</b><div style="opacity:.6">{x}</div></div><span style="background:{t["accent"]};color:#15110c;border-radius:16px;padding:3px 9px;font-weight:600;font-size:8.5px">Book</span></div>' for d,x in [("Slow Flow","Thu 6.00pm · Studio"),("Vinyasa","Sat 10am · Online"),("Yin","Sun 5pm · Studio")])
      + f'<div style="margin-top:6px;font-family:{t["mono"] if False else t["body"]};font-size:8px;opacity:.6">Powered by your Wix scheduler & payments</div></div></div></div>')
    inner=(f'<div style="position:absolute;inset:0;background:{t["paper"]}"></div><div class="paper-grain grain" style="position:absolute;inset:0"></div>'
      f'<div class="pad col">'
      f'<div class="row" style="justify-content:space-between;align-items:baseline">'
      f'<div style="font-family:{t["display"]};font-weight:{600 if t["display"]!="Syne" else 800};font-size:30px;color:{t["ink"]};{disp_style}">Website</div>'
      f'<div class="eyebrow" style="color:{t["soft"]}">on Wix · home · classes · corporate · private · philosophy</div></div>'
      f'<div style="height:20px"></div>'
      f'<div class="row" style="gap:34px;align-items:flex-start">{desktop}'
      f'<div class="col" style="gap:12px">{mphone}</div></div>'
      f'<div style="font-family:{t["body"]};font-size:11.5px;color:{t["soft"]};margin-top:18px;max-width:900px">Built on your existing Wix Premium — keeps the inbuilt scheduler, payments and Zoom links you already use. Same five-section structure; the brand world changes the feel, not the functionality.</div>'
      f'</div>')
    return page("web", inner, foot=f"DIRECTION {t['key']} · WEBSITE")

def build_concept(t):
    return concept_cover(t)+identity_page(t)+instagram_page(t)+website_page(t)

# ============================================================ COVER + FRAMING
def cover():
    inner=(f'<div class="c1-aurora grain" style="position:absolute;inset:0"></div>'
      f'<div style="position:absolute;top:60px;right:74px;z-index:12">{c1_stamp("#F2F1EA",150)}</div>'
      f'<div class="pad col" style="justify-content:space-between">'
      f'<div class="eyebrow" style="color:rgba(255,255,255,.92)">Brand & Visual Direction · {DATE}</div>'
      f'<div><div style="font-family:Fraunces;font-style:italic;font-weight:600;color:#fff;font-size:138px;line-height:.82;letter-spacing:-.02em">Mollie<br>Yoga</div>'
      f'<div style="font-family:Space Grotesk;color:#fff;font-size:21px;letter-spacing:.02em;margin-top:26px;opacity:.95">Three brand directions to align on — colour, type, mark, Instagram & website.</div></div>'
      f'<div class="row" style="gap:14px;align-items:center;color:#fff;font-family:Space Grotesk;font-size:13px;letter-spacing:.05em">'
      f'<span style="opacity:.85">01 In Flow</span><span style="opacity:.5">·</span>'
      f'<span style="opacity:.85">02 Earth &amp; Ember</span><span style="opacity:.5">·</span>'
      f'<span style="opacity:.85">03 Talisman</span></div></div>')
    return page("cover", inner, foot="", num_label="—")

def overview():
    likes=[("Type with movement","Fonts and captions that flow and curve with the body."),
           ("Bold text + photo","Posts that are confidently just words, or words over abstract image."),
           ("Gradient / watercolour","Dreamy, abstract photography and colour fields."),
           ("Colour, not cliché","Green · blue · violet with warm highlights. No beige & sage."),
           ("Symbol & spirit","Prayer hands, yin-yang, sun, the elements — drawn modern."),
           ("Earthy + a little fire","Grounded and approachable, with challenge and heat.")]
    nos=["Beige & sage wellness palettes","Soft, timid, “gentle” type","Hand-drawn / whimsy","Generic asana stick-figures","Anything that looks like a Canva template"]
    lk="".join(f'<div style="border-top:1.5px solid {C1["ink"]};padding-top:9px"><div style="font-family:Space Grotesk;font-weight:600;font-size:14px;color:{C1["ink"]}">{a}</div><div style="font-family:Space Grotesk;font-size:11.5px;color:#5b6b62;margin-top:4px;line-height:1.35">{b}</div></div>' for a,b in likes)
    dirs=[("01","In Flow","Aurora gradients & kinetic type","c1-aurora"),
          ("02","Earth & Ember","Bold, grounded, lit by fire","c2-field"),
          ("03","Talisman","Folk-modern symbols & flat colour","c3-duo")]
    dd="".join(f'<div class="{cl} grain" style="flex:1;border-radius:13px;height:118px;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:space-between;padding:14px;color:#fff">'
      f'<div class="eyebrow" style="font-size:9px">DIRECTION {k}</div>'
      f'<div><div style="font-family:Fraunces;font-style:italic;font-weight:600;font-size:24px">{n}</div>'
      f'<div style="font-family:Space Grotesk;font-size:10px;opacity:.92;margin-top:2px">{d}</div></div></div>' for k,n,d,cl in dirs)
    nolist="".join(f'<span style="display:inline-block;border:1.3px solid #b9442f;color:#b9442f;border-radius:20px;padding:5px 12px;font-family:Space Grotesk;font-size:11px;margin:0 7px 7px 0">✕ {x}</span>' for x in nos)
    inner=(f'<div style="position:absolute;inset:0;background:{C1["paper"]}"></div><div class="paper-grain grain" style="position:absolute;inset:0"></div>'
      f'<div class="pad col">'
      f'<div class="eyebrow" style="color:#5b6b62">How to read this deck</div>'
      f'<div style="font-family:Fraunces;font-style:italic;font-weight:600;font-size:42px;color:{C1["ink"]};margin-top:8px;line-height:1.0">What we’re aligning on</div>'
      f'<div style="font-family:Space Grotesk;font-size:13px;color:#5b6b62;margin-top:10px;max-width:760px;line-height:1.5">Pulled straight from your likes / dislikes and our call. Three directions follow — each a complete world (palette, type, a little brand mark, Instagram templates and a website). They’re starting points, not finished art; nothing here is precious.</div>'
      f'<div style="height:22px"></div>'
      f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px 38px">{lk}</div>'
      f'<div style="height:24px"></div>'
      f'<div class="row" style="gap:18px">{dd}</div>'
      f'<div style="height:20px"></div>'
      f'<div class="row" style="align-items:center;gap:16px;flex-wrap:wrap"><span style="font-family:Space Grotesk;font-weight:600;font-size:12px;letter-spacing:.16em;color:#b9442f">STAYING WELL AWAY FROM</span>{nolist}</div>'
      f'</div>')
    return page("overview", inner, foot="THE BRIEF")

def closing():
    qs=["Which direction feels most <i>you</i> — or which pieces to splice together?",
        "Photography: gradient fields hold the space beautifully until your shoot — shall we lock a date?",
        "Brand mark: prefer the wordmark, the monogram, or the seal as your main “tag”?",
        "Any colours to push warmer / cooler / bolder before we refine one route?"]
    ql="".join(f'<div style="display:flex;gap:14px;align-items:flex-start;margin-bottom:14px"><div style="font-family:Fraunces;font-style:italic;font-size:22px;color:{C1["accent"]};line-height:1">{i+1}</div><div style="font-family:Space Grotesk;font-size:15px;color:#fff;line-height:1.4;max-width:620px">{q}</div></div>' for i,q in enumerate(qs))
    inner=(f'<div class="c1-aurora2 grain" style="position:absolute;inset:0"></div>'
      f'<div class="pad col" style="justify-content:space-between">'
      f'<div class="eyebrow" style="color:rgba(255,255,255,.9)">Next step · let’s talk</div>'
      f'<div><div style="font-family:Fraunces;font-style:italic;font-weight:600;font-size:46px;color:#fff;line-height:1.0;margin-bottom:26px">A few things to react to</div>{ql}</div>'
      f'<div style="font-family:Space Grotesk;font-size:13px;color:rgba(255,255,255,.85);letter-spacing:.02em">Pick a lane and I’ll take one direction to a tight, finished system — wordmark, templates and a Wix build — for the July 6 timeline.</div></div>')
    return page("closing", inner, foot="MOLLIE YOGA · BRAND CONCEPTS", num_label="—")

# ============================================================ ASSEMBLE
DATE="June 2026"
HEAD=('<!doctype html><html><head><meta charset="utf-8">'
  '<link rel="stylesheet" href="css/deck.css">'
  '<style>'+CSS+'</style></head><body>')
FOOT="</body></html>"

pages = cover()+overview()+build_concept(C1)+build_concept(C2)+build_concept(C3)+closing()
with open("deck/index.html","w") as f:
    f.write(HEAD+pages+FOOT)
print("wrote deck/index.html ; pages =", PAGE)
