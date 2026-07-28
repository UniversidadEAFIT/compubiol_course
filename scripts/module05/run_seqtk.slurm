#!/usr/bin/env bash
#SBATCH --job-name=seqtk_demo
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=00:10:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err
# Ajuste según la documentación institucional vigente:
# #SBATCH --account=SU_CUENTA
# #SBATCH --partition=SU_PARTICION

set -Eeuo pipefail

INPUT_FASTQ=${INPUT_FASTQ:?Defina INPUT_FASTQ con una ruta válida}
OUTPUT_FASTQ=${OUTPUT_FASTQ:-results/subsample.fastq}
N_READS=${N_READS:-1000}
SEED=${SEED:-100}
CONDA_ENV=${CONDA_ENV:-compubiol-2026}

mkdir -p "$(dirname "$OUTPUT_FASTQ")" logs

if command -v conda >/dev/null 2>&1; then
  source "$(conda info --base)/etc/profile.d/conda.sh"
  conda activate "$CONDA_ENV"
fi

command -v seqtk >/dev/null 2>&1 || { echo 'ERROR: seqtk no está disponible' >&2; exit 127; }
[[ -s "$INPUT_FASTQ" ]] || { echo "ERROR: entrada inexistente o vacía: $INPUT_FASTQ" >&2; exit 66; }

printf '[INFO] host=%s job=%s input=%s n=%s seed=%s\n' \
  "$(hostname)" "${SLURM_JOB_ID:-interactive}" "$INPUT_FASTQ" "$N_READS" "$SEED"

seqtk sample -s"$SEED" "$INPUT_FASTQ" "$N_READS" > "$OUTPUT_FASTQ"
[[ -s "$OUTPUT_FASTQ" ]] || { echo 'ERROR: salida vacía' >&2; exit 65; }
printf '[INFO] output=%s reads=%s\n' "$OUTPUT_FASTQ" "$(( $(wc -l < "$OUTPUT_FASTQ") / 4 ))"
