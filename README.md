# Open in Devin Review

A small browser extension that adds an **Open in Devin Review** button to GitHub
pull request pages. Clicking it opens the same PR on `devinreview.com` in a new
tab.

The repo contains one self-contained extension per browser:

- `firefox/` — Firefox (Manifest V3, signed via AMO)
- `chrome/` — Chrome (Manifest V3, for Chrome Web Store)

`content.js` / `content.css` are currently duplicated in each directory because
extension files must live inside the extension root. `tools/make_icons.py`
regenerates the PNG icons for both.

## Firefox

### Temporary (for testing)

1. Open `about:debugging` in Firefox.
2. Click **This Firefox** → **Load Temporary Add-on**.
3. Select `firefox/manifest.json`.

### Permanent (self-distributed)

Firefox requires all permanently installed extensions to be signed by
addons.mozilla.org (AMO), but the add-on does **not** need to be publicly
listed. This repository includes a GitHub Actions workflow that submits the
extension in `firefox/` to AMO's **unlisted** channel on every `v*` tag and
attaches the signed `.xpi` to the GitHub release. Users install it permanently
by downloading the `.xpi` from a release.

#### One-time setup

1. Create an AMO account at <https://addons.mozilla.org/developers/>.
2. Generate API credentials at
   <https://addons.mozilla.org/developers/addon/api/key/>.
3. Add them as repository secrets (Settings → Secrets and variables → Actions):
   - `AMO_JWT_ISSUER` — the JWT issuer (your AMO email)
   - `AMO_JWT_SECRET` — the JWT secret

#### Cutting a release

1. Bump `version` in `firefox/manifest.json` **and** `chrome/manifest.json`
   (AMO rejects re-uploading an existing version).
2. Commit, then tag: `git tag v0.2.0 && git push origin v0.2.0`.
3. The workflow signs the Firefox extension and creates a GitHub release with
   the `.xpi` attached.

## Chrome

### Testing

1. Open `chrome://extensions`.
2. Enable **Developer mode**.
3. Click **Load unpacked** and select the `chrome/` directory.

### Publishing

Chrome extensions are distributed through the Chrome Web Store. This requires a
one-time $5 developer account at
<https://chrome.google.com/webstore/devconsole>. From there:

1. Click **New item**, upload a zip of the `chrome/` directory.
2. Fill in the listing (name, description, a 128px icon is already provided).
3. Submit for review.

For an unlisted/self-hosted distribution, the store also supports **unlisted**
items — anyone with the link can install, no public listing.

## Development

No build step. Edit `content.js` / `content.css` in the relevant browser
directory, then reload the extension (`about:debugging` for Firefox,
`chrome://extensions` for Chrome).
