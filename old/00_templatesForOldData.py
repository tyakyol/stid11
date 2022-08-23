def fastp(file1, corrected):
    inputs = [file1]
    outputs = [corrected]
    options = {
        'cores': 12,
        'memory': '64g',
        'walltime': '12:00:00'
        }
    spec = '''
fastp -i {file1} -o {corrected} -q 30 -w 12 -g
    '''.format(file1=file1, corrected=corrected)
    return inputs, outputs, options, spec


def map_pr_gz(file1):
    inputs = [file1]
    outputs = []
    options = {
        'cores': 12,
        'memory': '64g',
        'walltime': '48:00:00'
        }
    prefix = file1
    spec = '''
STAR --runThreadN 12 \
--readFilesCommand zcat \
--genomeDir /home/tyakyol/InRoot/dtd_map/data/genomeDir \
--alignIntronMax 2000 \
--outSAMtype BAM SortedByCoordinate \
--outFileNamePrefix {prefix} \
--readFilesIn {file1}
        '''.format(file1=file1, prefix=prefix)
    return inputs, outputs, options, spec
