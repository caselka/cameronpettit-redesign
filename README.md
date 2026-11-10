# cameronpettit.com redesign (prototype)

A redesigned homepage for cameronpettit.com: clean, pastel and abstract, with interactive pieces themed around OSINT and security.
This is a standalone prototype. It has not been merged into the live site, which is a separate full-stack app.

## What's in the page
- **Hero shape network**: pastel shapes joined by link lines. A tap sends out a scan ring that "finds" grey shapes; the Rearrange button cycles compositions (noise, link graph, perimeter, range rings, timeline).
- **Short film**: a 14-second looping canvas animation of a small builder assembling a web page by hand before a monitor pulls it in. The builder's eye follows the pointer, it waves when the pointer is close, and it jumps on click.
- **Page mascot**: a second small creature that perches on the header, falls off when the page scrolls, gets thrown around by further scrolling, chases the pointer and trips over, flies off when clicked, and jumps back to its perch at the top of the page.
- **Services**: Build, Systemise, Secure, Measure.
- **Work list**: 12 projects that expand, with a Websites / Systems filter.
- **Contact**: details with copy buttons and a message form that posts JSON to `/api/contact` (the live site's existing endpoint).

## Files
- `dist/index.html`: complete standalone page. Open it in a browser or host it as is.
- `index.html`: the same page without the document wrapper, used for the Claude artifact preview.
- `build/src.html`: the source to edit (HTML, CSS and JS in one file).
- `build/thumbs.json`: project thumbnails as data URIs, injected at build time.
- `build/build.py`: rebuilds both outputs. Run `python3 build/build.py` after editing `build/src.html`.

## Notes
- Links to Quote Request, Privacy Policy and WebNhanh point at the live site.
- The contact form only sends when the page is served from the live site; elsewhere it shows a fallback message.
- Light theme only, by choice.
- The cybersecurity service wording should be reviewed before going live.
