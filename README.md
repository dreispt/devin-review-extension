# Open in Devin Review

A tiny browser extension that adds an **Open in Devin Review** button to GitHub
pull request pages. One click opens the same PR on
[devinreview.com](https://devinreview.com) in a new tab — no copy-pasting URLs.

Works in Firefox and Chrome.

## Firefox

### Quick install (permanent)

1. Download the latest `.xpi` file from the
   [Releases](https://github.com/dreispt/devin-review-extension/releases)
   page.
2. Open it with Firefox (or drag it onto `about:addons`).
3. Confirm the install when prompted.

### Temporary install (for testing)

1. Download or clone this repository.
2. Open `about:debugging` in Firefox.
3. Click **This Firefox** → **Load Temporary Add-on**.
4. Select `firefox/manifest.json`.

> Temporary add-ons are removed when Firefox restarts. Use the `.xpi` above
> for a permanent install.

## Chrome

### Quick install (for testing)

Chrome doesn't offer direct `.zip` installs, so for now:

1. Download or clone this repository.
2. Open `chrome://extensions`.
3. Turn on **Developer mode** (top right).
4. Click **Load unpacked** and select the `chrome/` folder.

A Chrome Web Store listing is planned — check back here for a one-click
install link.

## Usage

Open any GitHub pull request (e.g. `github.com/owner/repo/pull/123`). A blue
**Open in Devin Review** button appears in the bottom-right corner. Click it to
open the PR on Devin Review in a new tab.

## For developers

The repo contains one self-contained extension per browser:

- `firefox/` — Firefox version
- `chrome/` — Chrome version
- `tools/` — icon generator (`python3 tools/make_icons.py`)

Releases are cut by tagging a version (e.g. `git tag v0.2.0 && git push origin
v0.2.0`); a GitHub Action signs the Firefox build via addons.mozilla.org and
attaches the `.xpi` to the release automatically.
