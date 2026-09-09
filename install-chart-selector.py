"""Install the packaged math-modeling-chart-selector skill with Python 3.9+."""
import argparse
import hashlib
import io
import os
from pathlib import Path, PurePosixPath
import tempfile
import urllib.request
import zipfile

NAME = "math-modeling-chart-selector"
REVISION = "main"
URL = f"https://raw.githubusercontent.com/Drancy-Den/picture-sikill/{REVISION}/{NAME}.zip"
SHA256 = "f8e788cb9bc3090394f9ce5a80565b5186cf4e4faf2b31c84382ec372f8d3ac9"


def install(data, skills_dir):
    if hashlib.sha256(data).hexdigest() != SHA256:
        raise ValueError("Package checksum mismatch; no files installed.")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        members = {}
        for info in archive.infolist():
            path = PurePosixPath(info.filename)
            if path.is_absolute() or ".." in path.parts or "\\" in info.filename:
                raise ValueError("Invalid package path.")
            if path.parts and path.parts[0] == NAME and not info.is_dir():
                relative = Path(*path.parts[1:])
                members[relative] = archive.read(info)
        if Path("SKILL.md") not in members:
            raise ValueError("Package has no SKILL.md.")
    destination = skills_dir / NAME
    if destination.exists():
        existing = {p.relative_to(destination) for p in destination.rglob("*") if p.is_file()}
        if existing == set(members) and all((destination / p).read_bytes() == b for p, b in members.items()):
            print(f"Already installed and verified: {destination}")
            return
        raise FileExistsError(f"Existing installation differs: {destination}. Back it up and move it before reinstalling.")
    skills_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="skill-install-", dir=skills_dir) as staging:
        prepared = Path(staging) / NAME
        for relative, content in members.items():
            target = prepared / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        prepared.rename(destination)
    print(f"Installed {len(members)} files: {destination}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, help="Use a previously downloaded ZIP (same checksum required).")
    parser.add_argument("--dest", type=Path, help="Skills parent directory; default: $CODEX_HOME/skills or ~/.codex/skills.")
    args = parser.parse_args()
    skills_dir = args.dest or Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills"
    local = args.archive or Path(__file__).with_name(f"{NAME}.zip")
    if local.is_file():
        data = local.read_bytes()
    elif args.archive:
        parser.error(f"Archive not found: {local}")
    else:
        print("Downloading pinned skill package from GitHub...")
        with urllib.request.urlopen(URL, timeout=60) as response:
            data = response.read()
    install(data, skills_dir.expanduser().resolve())
    print("Invoke $math-modeling-chart-selector in your next Codex turn.")


if __name__ == "__main__":
    main()
