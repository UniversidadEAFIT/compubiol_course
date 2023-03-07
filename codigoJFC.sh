#!/bin/bash

#SBATCH --partition=learning                   # Partition
#SBATCH --nodes=1
#SBATCH --ntasks=1                              # Number of tasks (processes)
#SBATCH --time=1:00:00                           # Walltime
#SBATCH --job-name=test_gpu                     # Job name
#SBATCH --output=%x_%j.out                      # Stdout (%x-jobName, %j-jobId)
#SBATCH --error=%x_%j.err                       # Stderr (%x-jobName, %j-jobId)
#SBATCH --mail-type=ALL                         # Mail notification
#SBATCH --mail-user=jfrancoc@eafit.edu.co       # User Email


##### ENVIRONMENT CREATION #####
module load miniconda3-4.10.3-gcc-11.2.0-vcglj27


##### JOB COMMANDS #### 
source activate blast
makeblastdb -in GCA_001466705.1_ASM146670v1_genomic.fna -title nuevoh -dbtype nucl -out databases/reference
blastn -db databases/reference -query ref.fasta -evalue 1e-3 -word_size 11 -outfmt 6

