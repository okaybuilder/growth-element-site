# Brand sources (not deployed)

- `og-image.html` → `dist/assets/og-image.png` ("Grow faster. Spend less." marker design, uses `og-common.css`).
  Render with Playwright at 1200x630 and save over `dist/assets/og-image.png`; the page tags pick up the new
  version automatically.
- `favicon.py` builds `favicon.svg` with "Ge" as DM Sans Bold outlines; `render_icons.js` makes the PNG sizes.
  `favicon.ico` = 16/32/48 PNGs; `apple-touch-icon.png` = 180px full-bleed.
- `portraits.py` makes `dist/assets/etan.jpg` (black and white, low-key background to match Zorba's portrait)
  and `dist/assets/zorba.jpg` (frame trimmed) from `source-assets/`. Needs `pip install rembg[cpu]`.
- Fonts: DM Sans and Manrope (SIL Open Font License), from @fontsource.
