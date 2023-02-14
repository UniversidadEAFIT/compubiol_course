#!/bin/bash

#SBATCH --partition=learning                    # Partition
#SBATCH --nodes=1								# learning solo tiene 1
#SBATCH --ntasks=16                              # Number of tasks (processes) en learning hasta 32
#SBATCH --time=5:00                            # Walltime
#SBATCH --job-name=blastn       		# Job name
#SBATCH --output=%x_%j.out 			# Stdout (%x-jobName, %j-jobId)
#SBATCH --error=%x_%j.err  			# Stderr (%x-jobName, %j-jobId)
#SBATCH --mail-type=ALL		                # Mail notification
#SBATCH --mail-user=sgomezt1@eafit.edu.co       # User Email



##### ENVIRONMENT CREATION #####
source activate myenv

module load python-3.9.9-gcc-11.2.0-k7juzmi

module load miniconda3-4.10.3-gcc-11.2.0-vcglj27

blastn -query referencia.fasta -subject genoma.fna -word_size 11 -outfmt 6 > resultado_blast.tsv





