#!/bin/bash

#SBATCH --partition=learning                   # Partition
#SBATCH --nodes=1
#SBATCH --ntasks=1                              # Number of tasks (processes)
#SBATCH --time=0-01:00:00                           # Walltime
#SBATCH --job-name=test_gpu                     # Job name
#SBATCH --output=%x_%j.out                      # Stdout (%x-jobName, %j-jobId)
#SBATCH --error=%x_%j.err                       # Stderr (%x-jobName, %j-jobId)
#SBATCH --mail-type=ALL                         # Mail notification
#SBATCH --mail-user=dagomezs1@eafit.edu.co       # User Email


##### ENVIRONMENT CREATION #####
module load miniconda3-4.10.3-gcc-11.2.0-vcglj27


##### JOB COMMANDS #### 
source activate miblast
makeblastdb -in sequence.fna -title hongo  -dbtype nucl -out databases/reference
blastn -db databases/reference -query tubulin.fasta -evalue 1e-3 -word_size 11 -outfmt 6
