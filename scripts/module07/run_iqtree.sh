#!/usr/bin/env bash
set -Eeuo pipefail

ALIGNMENT=${1:-data/module07/homologs_aligned.faa}
OUTDIR=${2:-results/module07}
THREADS=${THREADS:-AUTO}
mkdir -p "$OUTDIR"
[[ -s "$ALIGNMENT" ]] || { echo "ERROR: alineamiento inválido: $ALIGNMENT" >&2; exit 66; }

if command -v iqtree2 >/dev/null 2>&1; then
  IQTREE=iqtree2
elif command -v iqtree >/dev/null 2>&1; then
  IQTREE=iqtree
else
  echo 'ERROR: IQ-TREE no está disponible' >&2
  exit 127
fi

cp "$ALIGNMENT" "$OUTDIR/alignment.faa"
"$IQTREE" -s "$OUTDIR/alignment.faa" -m MFP -B 1000 --alrt 1000 -T "$THREADS" --prefix "$OUTDIR/course_tree"
echo "Árbol: $OUTDIR/course_tree.treefile"
