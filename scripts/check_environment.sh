#!/usr/bin/env bash
set -u

tools=(git python jupyter blastp makeblastdb mafft iqtree2 fastqc bedtools seqtk snakemake sbatch squeue sacct)
printf '%-15s %-12s %s\n' TOOL STATUS VERSION
printf '%-15s %-12s %s\n' '---------------' '------------' '------------------------------'
for tool in "${tools[@]}"; do
  if command -v "$tool" >/dev/null 2>&1; then
    version=$($tool --version 2>&1 | head -n 1 || true)
    [[ -z "$version" ]] && version=$($tool -version 2>&1 | head -n 1 || true)
    printf '%-15s %-12s %s\n' "$tool" OK "$version"
  else
    printf '%-15s %-12s %s\n' "$tool" MISSING '-'
  fi
done
