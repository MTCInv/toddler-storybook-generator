import sys
from PIL import Image, ImageDraw, ImageFont
A=sys.argv[1]
F="/usr/share/fonts/truetype/sand-box/google/Fredoka/Fredoka-VariableFont_wdth,wght.ttf"
pages=[
("0c096df00cd61335efedb54dcb2e92131f93f6a0f2030be4ed6953159ae2f29c","Mowgli's Jungle Day",'Swing, stomp, ROAR... and goodnight!'),
("5c6fc8ced72fc06eae33508cb22c696f63ec9e42e0bc2295be1356628816e094",'Deep in the jungle, green and tall,','lives little Mowgli. Hello, Mowgli! Wave to us all!'),
("0d6a90a97cdde15efdb2725dc16ff263db83501326932485cdc01a607dbf174e",'Bagheera the panther goes pad, pad, pad.','"Good morning, Mowgli!" Mowgli is glad.'),
("257ef156ebe190f009cc6e1efd41dde049435167a431bb6f25fb6a70f519ac5c",'Baloo the bear goes BOUNCE, BOUNCE, BOUNCE!','"Let\'s dance, little cub!" Boom-boom, bounce!'),
("526b525f172186d1f61b4db1f80570cfaa2e05a18023685caf8372cb6c3ec30b",'Up in the trees, the monkeys sing:','"Oo-oo! Ah-ah! Swing, swing, swing!"'),
("e5015b65fafb5e61da73c321b7ae96ffec51e44481538f8f4805725ac40f9005",'Mowgli swings too! Wheeee!','Swing, swing, swing!'),
("14e2a339a689c52fb79400948bb67049e0ef814ebce191cc680e695817a3c8e5",'STOMP, STOMP, STOMP!','Here come the elephants, all in a line.'),
("965e8a0dae2ecbad11df68adcb529644375f80cef0dbd4eaed64eeb88955554d",'Little Hathi goes TOOT-TOOT!','Mowgli marches too. Stomp, stomp, stomp!'),
("76bfbb10f6d9fc3888e17ae3cf246b60de4c76c34b2ae03a14702a5faad98c16",'Hissss, hissss! Kaa the snake wiggles by.','"Ssso sssleepy," says Kaa. Yaaawn!'),
("2a58bc58e9012d5fa51084a9372050a61d08071adaa4d2835f17549e32b33407",'SPLISH! SPLASH! SPLOSH!','Mowgli and Baloo play in the river.'),
("72586beaf280ccdf3b09dc6e8c608b3511805c19823f93f16feae7bfddea90f1",'Buzz, buzz, buzz! Here comes the honey.','Yum, yum, Baloo! Your tummy is funny!'),
("3a3bd051a2f599b43261466abff0d5d1f1580310ab5dba22bc97335325bec4b8","ROAR! It's Shere Khan the tiger...",'with a thorn in his paw. Ouch, ouch, ouch!'),
("b17e9dfef4c1bbb81e20768a9ac988b36502fb773c82921cfba0dd317059e96a",'Gently, gently, Mowgli helps. All better!','Shere Khan gives a big hug. Purrrrr!'),
("77aa36d1549841443cdf52dc4a2935b4b78bc19e7153032a221b32cedf51b3d9",'Now everyone is friends! Swing, swing, swing!','Stomp, stomp! Hiss! Purrr! Bounce!'),
("62ba73159305159418d7784183f0afbee25a74a4397b48300bea933f85426eaf",'The moon comes up. Twinkle, twinkle.','Mowgli yawns. Baloo yawns. Can YOU yawn?'),
("2c2a8039f7eb4eeecee86d14f975b5c3b8604f1f3e98c6731f02106c65019273",'Snuggle up, Mowgli. Goodnight, jungle friends!','Goodnight! The End.'),
]
W,H=2400,1800
out=[]
for i,(h,l1,l2) in enumerate(pages):
    im=Image.open(f"{A}/{h}.jpg").convert("RGB").resize((W,H),Image.LANCZOS)
    ov=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    cover=i==0
    f1=ImageFont.truetype(F,190 if cover else 104); f1.set_variation_by_axes([700,100])
    f2=ImageFont.truetype(F,90 if cover else 88); f2.set_variation_by_axes([600,100])
    def fit(t,f,maxw,wt=650):
        while d.textlength(t,font=f)>maxw: s=f.size-4; v=f.get_variation_axes(); f=ImageFont.truetype(F,s); f.set_variation_by_axes([wt,100])
        return f
    f1=fit(l1,f1,W-260); f2=fit(l2,f2,W-260)
    w=max(d.textlength(l1,font=f1),d.textlength(l2,font=f2))+140
    hh=f1.size+f2.size+150
    x0=(W-w)/2; y0=H-hh-40 if i==11 else 60
    d.rounded_rectangle([x0,y0,x0+w,y0+hh],radius=70,fill=(255,253,240,225))
    col1=(214,84,30) if cover else (40,60,40)
    d.text((W/2,y0+55),l1,font=f1,fill=col1,anchor="mt")
    d.text((W/2,y0+75+f1.size),l2,font=f2,fill=(30,110,60),anchor="mt")
    im=Image.alpha_composite(im.convert("RGBA"),ov).convert("RGB")
    p=f"page_{i:02d}.jpg"; im.save(p,quality=92); out.append(im)
out[0].save("jungle_book_toddler.pdf",save_all=True,append_images=out[1:],resolution=200)
