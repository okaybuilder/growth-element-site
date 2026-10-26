Growth Element v7 — Netlify handoff

Published review: https://growth-element-three-directions.zorbag.chatgpt.site
Source commit: 683b5c347f4465a89ce45a295452fe18299df390

Both founder portraits and the resized hero/header logo are included.

Deployment: unzip, then deploy the dist folder using Netlify's manual deploy. index.html must be at the deployment root. No build command is needed. For a repository deployment set publish directory to dist.

Before public launch: connect the booking buttons to the real booking calendar. The current modal only prepares a brief and does not send or book. Remove the noindex,nofollow robots meta from the homepage and calculator when ready for search indexing. Review page/comments are browser-local; remove the footer review link for launch if desired. Check the final domain and both desktop/mobile layouts after deployment.

consolidate.py generates the current pages. Do not run build.py; it generates the older concepts. CSS and JS are in dist/consolidated.css and dist/consolidated.js. Originals for both portraits are packaged as assets. No API keys or server setup required.
