# Growth Element website: deployment notes

Netlify settings: base directory empty, build command empty, publish directory `dist`.
`netlify.toml` already sets this. `dist/index.html` is the site root.

## Regenerating pages

`consolidate.py` generates `dist/index.html`, `dist/calc.html`, `dist/review.html` and
`dist/content.json`. Edit the generator, not the generated HTML, then run it and commit
both. Don't run `build.py` (older concepts; not included here).

```
python3 consolidate.py                                              # review build (v7 default)
GE_BOOKING_URL=https://... python3 consolidate.py                   # review build, real booking links
GE_MODE=launch GE_SITE_URL=https://<domain> GE_BOOKING_URL=https://... python3 consolidate.py
```

Launch mode removes noindex from the homepage and calculator, removes the footer
"Review this draft" link, adds canonical and Open Graph metadata, writes robots.txt and
sitemap.xml, and stops review-page copy edits from affecting the public pages. It refuses
to run without a booking URL, so the brief-only modal can't ship publicly.

`review.html` and the older concept pages stay deployed but unlinked and noindex. Delete
them from `dist/` if they shouldn't be reachable at all.

## Content rules to preserve

- Calculator dollar figures are the value of freed time, not guaranteed cash savings.
- Don't claim the site books calls or sends leads unless the booking link does that.
- No credentials in this repository.
