#!/usr/bin/env bash
set -Eeuo pipefail

OUTDIR=${1:-results/module08/fastqc}
shift || true
FILES=("$@")
if (($# == 0)); then
  FILES=(data/module08/good.fastq data/module08/adapter_low_quality.fastq)
fi
command -v fastqc >/dev/null 2>&1 || { echo 'ERROR: FastQC no está disponible' >&2; exit 127; }
mkdir -p "$OUTDIR"
for f in "${FILES[@]}"; do [[ -s "$f" ]] || { echo "ERROR: entrada inválida: $f" >&2; exit 66; }; done
fastqc --outdir "$OUTDIR" --extract "${FILES[@]}"
echo "Reportes en $OUTDIR"
