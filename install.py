"""Install the packaged math-modeling-figures skill with Python 3.9+."""
import argparse
import hashlib
import io
import os
from pathlib import Path, PurePosixPath
import tempfile
import urllib.request
import zipfile

NAME = "math-modeling-figures"
REVISION = "f9e9adc75d3e8c918ca55e7639e4a49326fb294a"
URL = f"https://raw.githubusercontent.com/Drancy-Den/picture-sikill/{REVISION}/{NAME}.zip"
SHA256 = "1f13fd88fd5881074f23cd63fd6b10e7e1f1f8729dc5c553b440439aa06ff63b"


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
    print("Invoke $math-modeling-figures in your next Codex turn.")


if __name__ == "__main__":
    main()
