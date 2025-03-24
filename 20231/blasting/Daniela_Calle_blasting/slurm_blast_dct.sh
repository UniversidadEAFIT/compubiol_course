#!/bin/bash

#SBATCH --partition=learning                   # Partition
#SBATCH --nodes=1
#SBATCH --ntasks=1                              # Number of tasks (processes)
#SBATCH --time=01:00:00                           # Walltime
#SBATCH --job-name=test_gpu       		# Job name
#SBATCH --output=%x_%j.out 			# Stdout (%x-jobName, %j-jobId)
#SBATCH --error=%x_%j.err  			# Stderr (%x-jobName, %j-jobId)
#SBATCH --mail-type=ALL		                # Mail notification
#SBATCH --mail-user=sgiraldos@eafit.edu.co       # User Email


##### ENVIRONMENT CREATION #####
module load python/3.6.0_miniconda-4.3.11_gcc-11.2.0
source activate blast

##### JOB COMMANDS #### 
blastn -query gene.fasta -subject GCA_001466705.1_ASM146670v1_genomic.fna -outfmt 6 -word_size 11 -perc_identity 90  -out resultado.tsv

