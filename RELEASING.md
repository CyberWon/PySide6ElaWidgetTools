# Releasing the PySide6 binding

The PyPI workflow builds binary wheels for macOS and Windows, checks them with
`twine`, and publishes them through [PyPI Trusted
Publishing](https://docs.pypi.org/trusted-publishers/). No PyPI username or
API token is stored in GitHub.

## First-time setup

1. Push this workflow to the repository's default branch.
2. Create a GitHub environment named `pypi`. Leave it empty unless you want
   manual approval for every release.
3. On PyPI, open **Account settings -> Publishing** and add a pending
   publisher with these values:

   | Field | Value |
   | --- | --- |
   | PyPI project name | `ElaWidgetTools` |
   | Owner | `CyberWon` |
   | Repository | `PySide6ElaWidgetTools` |
   | Workflow filename | `release-pypi.yml` |
   | Environment name | `pypi` |

4. Run **Release PyPI** from GitHub Actions with `publish` disabled once to
   validate all wheels without uploading.

## Cutting a release

1. Update the version in `ElaWidgetTools/CMakeLists.txt` and any release notes.
2. Commit and push the changes to `main`.
3. Create an immutable release tag:

   ```bash
   git tag pypi-v2.0.0
   git push origin pypi-v2.0.0
   ```

4. The tag-triggered workflow builds macOS Python 3.10/3.12 wheels and Windows
   Python 3.9-3.12 wheels, runs smoke tests and `twine check`, then uploads
   them to PyPI.

Wheel metadata pins `PySide6==6.10.3`. When upgrading Qt/PySide6, update the
workflow environment and this dependency together.
