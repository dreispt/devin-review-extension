# Open in Devin Review

A small browser extension that adds an **Open in Devin Review** button to GitHub
pull request pages. Clicking it opens the same PR on `devinreview.com` in a new
tab.

## Install (Firefox)

### Temporary (for testing)

1. Open `about:debugging` in Firefox.
2. Click **This Firefox** → **Load Temporary Add-on**.
3. Select `manifest.json` from this repository.

### Permanent (self-distributed)

Firefox requires all permanently installed extensions to be signed by
addons.mozilla.org (AMO), but the add-on does **not** need to be publicly
listed. This repository includes a GitHub Actions workflow that submits the
extension to AMO's **unlisted** channel on every `v*` tag and attaches the
signed `.xpi` to the GitHub release. Users install it permanently by
downloading the `.xpi` from a release.

#### One-time setup

1. Create an AMO account at <https://addons.mozilla.org/developers/>.
2. Generate API credentials at
   <https://addons.mozilla.org/developers/addon/api/key/>.
3. Add them as repository secrets (Settings → Secrets and variables → Actions):
   - `AMO_JWT_ISSUER` — the JWT issuer (your AMO email)
   - `AMO_JWT_SECRET` — the JWT secret

#### Cutting a release

1. Bump `version` in `manifest.json` (AMO rejects re-uploading an existing
   version).
2. Commit, then tag: `git tag v0.2.0 && git push origin v0.2.0`.
3. The workflow signs the extension and creates a GitHub release with the
   `.xpi` attached.

## Chrome

Chrome support is planned. The content script is browser-agnostic; a Chrome
manifest will be added (same code, `manifest_version: 3` without the Gecko
settings) once the Firefox version is validated.

## Development

No build step. Edit `content.js` / `content.css`, then reload the extension at
`about:debugging`.
