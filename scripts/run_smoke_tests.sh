#!/usr/bin/env bash
set -Eeuo pipefail
cd "$(dirname "$0")/.."

python scripts/validate_repo.py

while IFS= read -r -d '' script; do
  bash -n "$script"
done < <(find scripts -type f \( -name '*.sh' -o -name '*.slurm' \) -print0)

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

scripts/module04/fasta_batch_stats.sh \
  -i data/module04/inputs \
  -o "$tmp/stats.tsv" \
  -l "$tmp/run.log"
[[ $(wc -l < "$tmp/stats.tsv") -eq 4 ]]
grep -q $'alpha\tfasta\t3\t' "$tmp/stats.tsv"
grep -q $'alpha\tfasta\t.*\t1$' "$tmp/stats.tsv"

if scripts/module04/fasta_batch_stats.sh -i data/module04/bad_inputs -o "$tmp/bad.tsv" >/dev/null 2>&1; then
  echo 'ERROR: el caso inválido debió fallar' >&2
  exit 1
fi

python scripts/module09/build_promoters.py \
  --genome data/module09/mini_genome.fasta \
  --gff data/module09/mini_annotations.gff3 \
  --length 200 \
  --output "$tmp/promoters.bed"
[[ $(wc -l < "$tmp/promoters.bed") -eq 3 ]]
grep -q $'^chr1\t0\t20\tgeneA\t\.\t+$' "$tmp/promoters.bed"
grep -q $'^chr1\t1450\t1650\tgeneB\t\.\t-$' "$tmp/promoters.bed"

echo 'SMOKE TESTS OK'
