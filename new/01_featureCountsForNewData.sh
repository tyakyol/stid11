#!/bin/bash
#SBATCH --partition normal
#SBATCH --mem 8g
#SBATCH -c 8
#SBATCH --account InRoot
#SBATCH -t 12:00:00

featureCounts -T 8 -s 0 \
-a ../anno_extract/20210713_LjGifu1.3_annotation.gtf \
-o ./output/featurecounts/johan_0.txt \
./output/johan_0/*.bam
