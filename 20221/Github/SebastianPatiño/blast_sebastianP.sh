#!/bin/bash

#SBATCH --partition=learning                    # Partition
#SBATCH --nodes=1								# learning solo tiene 1
#SBATCH --ntasks=1                              # Number of tasks (processes) en learning hasta 32
#SBATCH --time=2:00:00                          # Walltime
#SBATCH --job-name=blastn       		# Job name
#SBATCH --output=%x_%j.out 			# Stdout (%x-jobName, %j-jobId)
#SBATCH --error=%x_%j.err  			# Stderr (%x-jobName, %j-jobId)
#SBATCH --mail-type=ALL		                # Mail notification
#SBATCH --mail-user=spatinob@eafit.edu.co       # User Email
#SBATCH --cpus-per-task=1


##### ENVIRONMENT CREATION #####
python-3.9.9-gcc-11.2.0-k7juzmi
miniconda3-4.10.3-gcc-11.2.0-vcglj27
source activate Localblast
#### 
export LD_LIBRARY_PATH=/lib64:$LD_LIBRARY_PATH

##### JOB COMMANDS #### 
blastn -query sequence.fasta -subject GCA_001466705.1_ASM146670v1_genomic.fna -word_size 12 -out test_output.tsv -outfmt 7 
