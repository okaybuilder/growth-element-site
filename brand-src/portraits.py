import sys, io, numpy as np
from PIL import Image, ImageFilter, ImageOps
from rembg import remove, new_session
src='/home/claude/handoff/dist/assets/'; out=sys.argv[1]
# --- Zorba: trim baked-in grey frame, resize, compress
z=Image.open(src+'zorba.jpg').convert('L'); a=np.asarray(z).astype(int)
mask=np.abs(a-23)>3; ys,xs=np.where(mask)
# robust bbox: rows/cols where enough pixels differ from frame grey
rows=np.where(mask.mean(axis=1)>0.5)[0]; cols=np.where(mask.mean(axis=0)>0.5)[0]
box=(cols.min()+2,rows.min()+2,cols.max()-1,rows.max()-1); print('zorba crop',box)
zc=z.crop(box)
# --- Etan: B&W low-key to match Zorba
e=Image.open(src+'etan.png').convert('RGB')
W,H=e.size
sess=new_session('u2net_human_seg')
m=remove(e,session=sess,only_mask=True).convert('L').filter(ImageFilter.GaussianBlur(6))
# luminance with a little red weighting for skin
arr=np.asarray(e).astype(float)/255
L=0.40*arr[...,0]+0.45*arr[...,1]+0.15*arr[...,2]
mk=np.asarray(m).astype(float)/255
# subject: contrast curve; background: pushed to near-black like Zorba's
def curve(x,lo,hi,g):
    x=np.clip((x-lo)/(hi-lo),0,1); return x**g
subj=curve(L,0.06,0.97,1.15)
bg=curve(L,0.0,1.0,1.6)*0.10
Y=subj*mk+bg*(1-mk)
# soft directional falloff (light from upper left, like Zorba's)
yy,xx=np.mgrid[0:H,0:W]; cx,cy=W*0.48,H*0.40
r=np.sqrt(((xx-cx)/(W*0.62))**2+((yy-cy)/(H*0.75))**2)
Y=Y*np.clip(1.08-0.38*r**2,0.55,1.0)
# bring the light hoodie down so the face leads, like Zorba's low-key frame
t=np.clip((yy/H-0.60)/0.40,0,1); Y=Y*(1-0.42*t**1.2)
img=Image.fromarray((np.clip(Y,0,1)*255).astype('uint8'),'L')
# portrait crop 4:5 centred on face, same framing logic as the site's object-position
fh=H; fw=int(fh*0.8); x0=int(W*0.5-fw/2)
ec=img.crop((x0,0,x0+fw,fh))
def save(im,name,w):
    h=round(im.height*w/im.width); im=im.resize((w,h),Image.LANCZOS)
    for q in (84,80,76,72):
        b=io.BytesIO(); im.save(b,'JPEG',quality=q,optimize=True,progressive=True)
        if b.tell()<=120_000: break
    open(f'{out}/{name}','wb').write(b.getvalue()); print(name,im.size,'q',q,round(b.tell()/1024),'KB')
save(ec,'etan.jpg',640); save(zc,'zorba.jpg',640)
img.convert('RGB').resize((W//4,H//4)).save(out+'/etan_full_preview.jpg',quality=85)
