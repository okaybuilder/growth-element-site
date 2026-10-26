# Returns an SVG path for "Ge" in DM Sans Bold, with the site's -0.066667em letter-spacing.
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import sys
FONT=sys.argv[1] if len(sys.argv)>1 else None
def ge_path(font_path, size, x, baseline, spacing=-0.066667):
    f=TTFont(font_path); gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm
    s=size/upm; pen=SVGPathPen(gs); cur=0; bp=BoundsPen(gs)
    for ch in 'Ge':
        g=cmap[ord(ch)]
        t=(s,0,0,-s,x+cur*s,baseline)
        gs[g].draw(TransformPen(pen,t)); gs[g].draw(TransformPen(bp,t))
        cur+=gs[g].width+spacing*upm
    return pen.getCommands(), bp.bounds
