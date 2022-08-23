#!/bin/bash
#SBATCH --partition normal
#SBATCH --mem 8g
#SBATCH -c 8
#SBATCH -t 12:00:00

featureCounts -T 8 -s 1 \
-a ../anno_extract/20210713_LjGifu1.3_annotation.gtf \
-o ./featurecounts.txt \
./fastp/bam/*.bam
