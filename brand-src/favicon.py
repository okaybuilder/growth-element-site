import sys; sys.path.insert(0,sys.argv[1]); from glyphs import ge_path
font=sys.argv[2]; out=sys.argv[3]
INK='#19271e'; PAPER='#fcfcf9'
# Centre the glyphs optically in a 64-unit tile
d,(x0,y0,x1,y1)=ge_path(font,34,0,0)
w,h=x1-x0,y1-y0; dx=(64-w)/2-x0; dy=(64-h)/2-y0+0.5
d,_=ge_path(font,34,dx,dy)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="6" fill="{INK}"/><path fill="{PAPER}" d="{d}"/></svg>'''
open(out+'/favicon.svg','w').write(svg); print(len(svg),'bytes')
