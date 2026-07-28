#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

import nbformat
import yaml

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

required = [
    "README.md", "environment.yml", "mkdocs.yml", "CONTRIBUTING.md",
    "notebooks/03_linux/03_intro_linux.ipynb",
    "notebooks/04_bash_robusto/04_bash_manejo_errores.ipynb",
    "notebooks/06_alineamiento_blast/06_alineamiento_blast_mafft.ipynb",
]
for rel in required:
    if not (ROOT / rel).exists():
        ERRORS.append(f"Falta archivo requerido: {rel}")

for yml in [ROOT / "environment.yml", ROOT / "environment-minimal.yml", ROOT / "mkdocs.yml"]:
    try:
        yaml.safe_load(yml.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"YAML inválido {yml.relative_to(ROOT)}: {exc}")

absolute_path = re.compile(r"/(Users|home)/[A-Za-z0-9._-]+/")
secret = re.compile(r"(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|BEGIN (RSA|OPENSSH) PRIVATE KEY)")
for path in sorted((ROOT / "notebooks").rglob("*.ipynb")):
    try:
        nb = nbformat.read(path, as_version=4)
        nbformat.validate(nb)
    except Exception as exc:
        ERRORS.append(f"Notebook inválido {path.relative_to(ROOT)}: {exc}")
        continue
    for idx, cell in enumerate(nb.cells, 1):
        if cell.cell_type == "code":
            if cell.get("execution_count") is not None:
                ERRORS.append(f"Execution count presente: {path.relative_to(ROOT)} celda {idx}")
            if cell.get("outputs"):
                ERRORS.append(f"Salida persistente: {path.relative_to(ROOT)} celda {idx}")
            if absolute_path.search(cell.source):
                ERRORS.append(f"Ruta personal absoluta: {path.relative_to(ROOT)} celda {idx}")
            if secret.search(cell.source):
                ERRORS.append(f"Posible secreto: {path.relative_to(ROOT)} celda {idx}")

for path in ROOT.rglob("*"):
    if path.is_file() and ".git" not in path.parts and path.stat().st_size > 5 * 1024 * 1024:
        ERRORS.append(f"Archivo mayor de 5 MB: {path.relative_to(ROOT)}")

# Validate local Markdown links. External URLs, anchors and mail links are skipped.
link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
for path in sorted(ROOT.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    for raw_target in link_pattern.findall(text):
        target = raw_target.strip().split()[0].strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            ERRORS.append(f"Enlace sale del repositorio: {path.relative_to(ROOT)} -> {target}")
            continue
        if not resolved.exists():
            ERRORS.append(f"Enlace local roto: {path.relative_to(ROOT)} -> {target}")

for path in sorted((ROOT / "scripts").rglob("*")):
    if path.is_file() and path.suffix in {".sh", ".py", ".slurm"} and not (path.stat().st_mode & 0o111):
        ERRORS.append(f"Script sin permiso de ejecución: {path.relative_to(ROOT)}")

if ERRORS:
    print("VALIDACIÓN FALLIDA", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print("VALIDACIÓN OK")
