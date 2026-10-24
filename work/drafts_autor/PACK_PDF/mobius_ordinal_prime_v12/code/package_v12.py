"""Build and verify a v12 ZIP, with release SHA-256 manifests."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIRS = {"code", "figures", "data", "outputs", "docs", "submission",
        "chapters", "checksums"}


def included(path):
    rel = path.relative_to(ROOT)
    if any(part.startswith(".") or part == "__pycache__" for part in rel.parts):
        return False
    if path.suffix in {".aux", ".log", ".out", ".toc", ".pyc", ".synctex"}:
        return False
    return rel.parts[0] in DIRS or (
        len(rel.parts) == 1 and path.suffix in {".tex", ".pdf", ".md", ".cff", ".txt"})


def files():
    return sorted(p for p in ROOT.rglob("*") if p.is_file() and included(p))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest(paths, target):
    target.write_text("".join(digest(p)+"  "+p.relative_to(ROOT).as_posix()+"\n"
                              for p in paths), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=ROOT.parent / (ROOT.name+"_package.zip"))
    args = parser.parse_args()
    (ROOT / "checksums").mkdir(exist_ok=True)
    manifest(sorted((ROOT/"data").glob("*.npy")),
             ROOT/"checksums"/"DATA_SHA256.txt")
    manifest(sorted(p for p in (ROOT/"submission").iterdir() if p.is_file()),
             ROOT/"checksums"/"SUBMISSION_SHA256.txt")
    overall = ROOT/"checksums"/"SHA256SUMS.txt"
    manifest([p for p in files() if p != overall], overall)
    entries = files()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED,
                         compresslevel=6, allowZip64=True) as archive:
        for path in entries:
            archive.write(path, ROOT.name+"/"+path.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(args.output) as archive:
        bad = archive.testzip()
        assert bad is None, bad
        text = archive.read(ROOT.name+"/checksums/SHA256SUMS.txt").decode()
        checked = 0
        for line in text.splitlines():
            sha, path = line.split("  ", 1)
            assert hashlib.sha256(archive.read(ROOT.name+"/"+path)).hexdigest() == sha
            checked += 1
        for stem in ["mobius_ordinal_prime_transform_S_SS_v12",
                     "alpha_research_program_v12"]:
            pdf = archive.read(ROOT.name+"/"+stem+".pdf")
            assert pdf.startswith(b"%PDF-") and pdf.rstrip().endswith(b"%%EOF")
            tex = archive.read(ROOT.name+"/"+stem+".tex").decode()
            assert "Version 12" in tex
        submission = archive.read(
            ROOT.name+"/submission/mobius_ordinal_prime_transform_S_SS_v12.tex").decode()
        assert r"\input{chapters/" not in submission
        assert r"\label{thm:a12-determinants}" in submission
        assert r"\label{thm:a12-energy-zero}" in submission
        assert r"\label{eq:a12-GW-finite}" in submission
    report = {"zip": str(args.output.resolve()), "entries": len(entries),
              "sha256_verified_entries": checked, "crc_check_passed": True,
              "bytes": args.output.stat().st_size,
              "sha256": digest(args.output)}
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
