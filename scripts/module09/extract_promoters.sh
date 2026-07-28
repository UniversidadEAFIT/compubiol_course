#!/usr/bin/env bash
set -Eeuo pipefail

GENOME=${1:-data/module09/mini_genome.fasta}
GFF=${2:-data/module09/mini_annotations.gff3}
LENGTH=${3:-200}
OUTDIR=${4:-results/module09}

command -v python >/dev/null 2>&1 || { echo 'ERROR: Python no disponible' >&2; exit 127; }
command -v bedtools >/dev/null 2>&1 || { echo 'ERROR: bedtools no disponible' >&2; exit 127; }
[[ -s "$GENOME" ]] || { echo "ERROR: FASTA inválido: $GENOME" >&2; exit 66; }
[[ -s "$GFF" ]] || { echo "ERROR: GFF3 inválido: $GFF" >&2; exit 66; }
mkdir -p "$OUTDIR"

python scripts/module09/build_promoters.py \
  --genome "$GENOME" --gff "$GFF" --length "$LENGTH" \
  --output "$OUTDIR/promoters.bed"

bedtools getfasta \
  -fi "$GENOME" \
  -bed "$OUTDIR/promoters.bed" \
  -s -nameOnly \
  -fo "$OUTDIR/promoters.fasta"

[[ -s "$OUTDIR/promoters.fasta" ]] || { echo 'ERROR: FASTA de promotores vacío' >&2; exit 65; }
echo "OK: $OUTDIR/promoters.bed"
echo "OK: $OUTDIR/promoters.fasta"
