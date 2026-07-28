#!/usr/bin/env bash
set -Eeuo pipefail

PROGRAM=${0##*/}
INPUT_DIR=''
OUTPUT_TSV=''
LOG_FILE=''

usage() {
  cat <<'EOF'
Uso:
  fasta_batch_stats.sh -i INPUT_DIR -o OUTPUT_TSV [-l LOG_FILE]

Procesa archivos FASTA (.fa, .fasta, .fna) y FASTQ (.fq, .fastq) sin comprimir.
Genera estadísticas por archivo y cuenta identificadores duplicados.

Códigos de salida:
  0  éxito
  64 argumentos inválidos
  65 archivo vacío o formato inválido
  66 no se encontraron entradas
EOF
}

log() {
  local level=$1; shift
  local line
  line="[$(date '+%Y-%m-%d %H:%M:%S')] [$level] $*"
  printf '%s\n' "$line" >&2
  if [[ -n "$LOG_FILE" ]]; then
    printf '%s\n' "$line" >> "$LOG_FILE"
  fi
}

die() {
  local code=$1; shift
  log ERROR "$*"
  exit "$code"
}

on_error() {
  local rc=$?
  log ERROR "Fallo inesperado en la línea ${BASH_LINENO[0]} (código $rc)."
  exit "$rc"
}
trap on_error ERR

while getopts ':i:o:l:h' opt; do
  case "$opt" in
    i) INPUT_DIR=$OPTARG ;;
    o) OUTPUT_TSV=$OPTARG ;;
    l) LOG_FILE=$OPTARG ;;
    h) usage; exit 0 ;;
    :) die 64 "La opción -$OPTARG requiere un valor." ;;
    \?) die 64 "Opción desconocida: -$OPTARG" ;;
  esac
done

[[ -n "$INPUT_DIR" && -n "$OUTPUT_TSV" ]] || { usage >&2; exit 64; }
[[ -d "$INPUT_DIR" ]] || die 64 "No existe el directorio: $INPUT_DIR"
mkdir -p "$(dirname "$OUTPUT_TSV")"
if [[ -n "$LOG_FILE" ]]; then
  mkdir -p "$(dirname "$LOG_FILE")"
  : > "$LOG_FILE"
fi

for dep in awk sort; do
  command -v "$dep" >/dev/null 2>&1 || die 64 "Dependencia no disponible: $dep"
done

shopt -s nullglob
files=("$INPUT_DIR"/*.fa "$INPUT_DIR"/*.fasta "$INPUT_DIR"/*.fna "$INPUT_DIR"/*.fq "$INPUT_DIR"/*.fastq)
((${#files[@]} > 0)) || die 66 "No se encontraron archivos FASTA/FASTQ en $INPUT_DIR"

tmp=$(mktemp "${OUTPUT_TSV}.tmp.XXXXXX")
cleanup() { rm -f "$tmp"; }
trap cleanup EXIT
printf 'sample\tformat\trecords\ttotal_bases\tmin_length\tmax_length\tmean_length\tduplicate_ids\n' > "$tmp"

for file in "${files[@]}"; do
  [[ -s "$file" ]] || die 65 "Archivo vacío: $file"
  base=${file##*/}
  sample=${base%.*}
  ext=${base##*.}
  log INFO "Procesando $base"

  case "$ext" in
    fa|fasta|fna)
      stats=$(awk '
        function add_record() {
          if (current_id == "") return
          records++
          total += length_seq
          if (records == 1 || length_seq < min) min = length_seq
          if (length_seq > max) max = length_seq
          seen[current_id]++
          length_seq = 0
        }
        /^>/ {
          add_record()
          current_id = substr($0, 2)
          sub(/[[:space:]].*$/, "", current_id)
          if (current_id == "") invalid = 1
          next
        }
        {
          gsub(/[[:space:]]/, "", $0)
          if ($0 !~ /^[A-Za-z*.-]+$/) invalid = 1
          length_seq += length($0)
        }
        END {
          add_record()
          for (id in seen) if (seen[id] > 1) duplicates++
          if (invalid || records == 0) exit 65
          printf "%d\t%d\t%d\t%d\t%.2f\t%d", records, total, min, max, total/records, duplicates+0
        }
      ' "$file") || die 65 "FASTA inválido: $file"
      printf '%s\tfasta\t%s\n' "$sample" "$stats" >> "$tmp"
      ;;
    fq|fastq)
      stats=$(awk '
        NR % 4 == 1 {
          if (substr($0,1,1) != "@") invalid=1
          id=substr($0,2); sub(/[[:space:]].*$/, "", id); seen[id]++
        }
        NR % 4 == 2 {
          seq_len=length($0); records++; total+=seq_len
          if (records==1 || seq_len<min) min=seq_len
          if (seq_len>max) max=seq_len
        }
        NR % 4 == 3 { if (substr($0,1,1) != "+") invalid=1 }
        NR % 4 == 0 { if (length($0) != seq_len) invalid=1 }
        END {
          if (NR % 4 != 0) invalid=1
          for (id in seen) if (seen[id]>1) duplicates++
          if (invalid || records==0) exit 65
          printf "%d\t%d\t%d\t%d\t%.2f\t%d", records,total,min,max,total/records,duplicates+0
        }
      ' "$file") || die 65 "FASTQ inválido: $file"
      printf '%s\tfastq\t%s\n' "$sample" "$stats" >> "$tmp"
      ;;
    *) die 65 "Extensión no soportada: $file" ;;
  esac
done

{ head -n 1 "$tmp"; tail -n +2 "$tmp" | sort -t $'\t' -k1,1; } > "${tmp}.sorted"
mv "${tmp}.sorted" "$OUTPUT_TSV"
log INFO "Resumen escrito en $OUTPUT_TSV"
trap - EXIT
rm -f "$tmp"
