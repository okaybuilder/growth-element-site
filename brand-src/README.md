# Brand sources (not deployed)

- `og-image-a.html` → `dist/assets/og-image.png` (current share image). `og-image-b.html` is the alternative.
  Render: `node render.js og-image-a` (needs Playwright), then copy the PNG to `dist/assets/og-image.png`.
- `favicon.py` builds `favicon.svg` with "Ge" as DM Sans Bold outlines; `render_icons.js` makes the PNG sizes.
  `favicon.ico` = 16/32/48 PNGs; `apple-touch-icon.png` = 180px full-bleed.
- `portraits.py` makes `dist/assets/etan.jpg` (black and white, low-key background to match Zorba's portrait)
  and `dist/assets/zorba.jpg` (frame trimmed) from `source-assets/`. Needs `pip install rembg[cpu]`.
- Fonts: DM Sans and Manrope (SIL Open Font License), from @fontsource.
