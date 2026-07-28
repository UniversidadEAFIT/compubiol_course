#!/usr/bin/env bash
set -Eeuo pipefail

QUERY=${1:-data/module06/query.faa}
DATABASE=${2:-data/module06/protein_db.faa}
OUTDIR=${3:-results/module06}
MIN_IDENT=${MIN_IDENT:-35}
MIN_QCOV=${MIN_QCOV:-60}
MAX_EVALUE=${MAX_EVALUE:-1e-3}

for tool in makeblastdb blastp mafft python; do
  command -v "$tool" >/dev/null 2>&1 || { echo "ERROR: falta $tool" >&2; exit 127; }
done
[[ -s "$QUERY" ]] || { echo "ERROR: consulta inválida: $QUERY" >&2; exit 66; }
[[ -s "$DATABASE" ]] || { echo "ERROR: base inválida: $DATABASE" >&2; exit 66; }
mkdir -p "$OUTDIR/db"

makeblastdb -in "$DATABASE" -dbtype prot -parse_seqids -out "$OUTDIR/db/teaching" > "$OUTDIR/makeblastdb.log"

{
  printf 'qseqid\tsseqid\tpident\tlength\tqlen\tslen\tqcovs\tevalue\tbitscore\n'
  blastp \
    -query "$QUERY" \
    -db "$OUTDIR/db/teaching" \
    -evalue 10 \
    -seg yes \
    -outfmt '6 qseqid sseqid pident length qlen slen qcovs evalue bitscore'
} > "$OUTDIR/blast_all.tsv"

awk -F '\t' -v OFS='\t' -v id="$MIN_IDENT" -v cov="$MIN_QCOV" -v ev="$MAX_EVALUE" '
  NR==1 || ($3+0 >= id && $7+0 >= cov && $8+0 <= ev)
' "$OUTDIR/blast_all.tsv" > "$OUTDIR/blast_filtered.tsv"

python scripts/module06/select_fasta.py \
  --query "$QUERY" --database "$DATABASE" \
  --hits "$OUTDIR/blast_filtered.tsv" \
  --output "$OUTDIR/candidates.faa"

mafft --auto "$OUTDIR/candidates.faa" > "$OUTDIR/homologs_aligned.faa" 2> "$OUTDIR/mafft.log"

echo "OK: $OUTDIR/blast_all.tsv"
echo "OK: $OUTDIR/blast_filtered.tsv"
echo "OK: $OUTDIR/homologs_aligned.faa"
