#!/bin/bash

#SBATCH --partition=learning                   # Partition
#SBATCH --nodes=1
#SBATCH --ntasks=1                              # Number of tasks (processes)
#SBATCH --time=01:00:00                           # Walltime
#SBATCH --job-name=test_gpu       		# Job name
#SBATCH --output=%x_%j.out 			# Stdout (%x-jobName, %j-jobId)
#SBATCH --error=%x_%j.err  			# Stderr (%x-jobName, %j-jobId)
#SBATCH --mail-type=ALL		                # Mail notification
#SBATCH --mail-user=legiraldom@eafit.edu.co       # User Email

module load python/3.6.0_miniconda-4.3.11_gcc-11.2.0

source activate Miblast
makeblastdb -in M.roreri.fna -title M.roreri -dbtype nucl -out databases/reference
blastn -db databases/reference -query Amanita_muscaria.fasta -evalue 1e3 -word_size 11 -outfmt 6 -perc_identity 90 > Resultado_blasting

