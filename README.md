# Open in Devin Review

A small browser extension that adds an **Open in Devin Review** button to GitHub
pull request pages. Clicking it opens the same PR on `devinreview.com` in a new
tab.

## Install (Firefox)

### Temporary (for testing)

1. Open `about:debugging` in Firefox.
2. Click **This Firefox** → **Load Temporary Add-on**.
3. Select `manifest.json` from this repository.

### Permanent

Firefox does not yet support self-hosted extension installs. For permanent
installation, the extension needs to be signed and listed on [addons.mozilla.org](https://addons.mozilla.org),
or distributed via an enterprise policy. The current manifest includes the
required `browser_specific_settings.gecko.id` so it can be signed as-is.

## Chrome

Chrome support is planned. The content script is browser-agnostic; a Chrome
manifest will be added (same code, `manifest_version: 3` without the Gecko
settings) once the Firefox version is validated.

## Development

No build step. Edit `content.js` / `content.css`, then reload the extension at
`about:debugging`.
