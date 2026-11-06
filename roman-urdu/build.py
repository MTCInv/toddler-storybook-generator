from PIL import Image, ImageDraw, ImageFont
from story import P,SABAQ
A="/cursor/stores/store-08c5030f-417a-4f3d-9399-e85e561a9b67/grok-bot/agents/43799f34-812d-4428-82bd-ee664dc8f7ad/assets"
F="/usr/share/fonts/truetype/sand-box/google/Fredoka/Fredoka-VariableFont_wdth,wght.ttf"
def font(s,w):
    f=ImageFont.truetype(F,s); f.set_variation_by_axes([w,100]); return f
W,H=2400,1800; BODY=font(68,500); LH=96
def wrap(d,t,f,mw):
    out=[];cur=""
    for w in t.split():
        c=(cur+" "+w).strip()
        if d.textlength(c,font=f)<=mw: cur=c
        else: out.append(cur);cur=w
    out.append(cur);return out
pages=[]
for i,(h,t) in enumerate(P):
    if h: im=Image.open(f"{A}/{h}.jpg").convert("RGB").resize((W,H),Image.LANCZOS)
    else: im=Image.new("RGB",(W,H),(255,248,225))
    ov=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    if t=="TITLE":
        x0,x1=1520,2340
        d.rounded_rectangle([x0,330,x1,1470],70,fill=(255,253,240,235))
        tf=font(150,700)
        for k,l in enumerate(["Mowgli","aur Jungle","ka Ghar"]):
            d.text(((x0+x1)/2,420+k*175),l,font=tf,fill=(200,80,30),anchor="mt")
        st=font(64,500)
        for k,l in enumerate(wrap(d,"Ek pyaari kahani: dosti, sach aur himmat ki",st,x1-x0-100)):
            d.text(((x0+x1)/2,1000+k*90),l,font=st,fill=(30,100,55),anchor="mt")
    elif t=="SABAQ":
        cs=Image.open("/workspace/jungle-book-toddler/character_sheet.jpg").convert("RGB")
        cs=cs.resize((1500,int(1500*cs.height/cs.width)));im.paste(cs,((W-1500)//2,H-cs.height-20))
        d.text((W/2,90),"Kahani ka sabaq",font=font(130,700),fill=(200,80,30),anchor="mt")
        y=290
        for k,s in enumerate(SABAQ):
            for j,l in enumerate(wrap(d,f"{k+1}. {s}",font(72,600),W-400)):
                d.text((200 if j==0 else 262,y),l,font=font(72,600),fill=(30,70,40)); y+=98
            y+=12
        assert y< H-cs.height, (i,y)
    else:
        x0,x1=1500,2350; lines=wrap(d,t,BODY,x1-x0-110)
        th=len(lines)*LH; y0=(H-th)/2-60
        d.rounded_rectangle([x0,y0,x1,y0+th+120],70,fill=(255,253,240,235))
        for k,l in enumerate(lines): d.text((x0+55,y0+60+k*LH),l,font=BODY,fill=(35,55,40))
        d.text((x1-50,y0+th+75),str(i),font=font(44,600),fill=(150,150,150),anchor="rm")
        assert th+120<H-100,(i,len(lines))
        print(i,len(lines),len(t.split('.'))-1)
    im=Image.alpha_composite(im.convert("RGBA"),ov).convert("RGB")
    im.save(f"page_{i:02d}.jpg",quality=92); pages.append(im)
pages[0].save("jungle_book_urdu.pdf",save_all=True,append_images=pages[1:],resolution=200)
ims=[p.resize((480,360)) for p in pages]
s=Image.new("RGB",(2400,360*5),"white");[s.paste(m,((k%5)*480,(k//5)*360)) for k,m in enumerate(ims)];s.save("contact.jpg")
