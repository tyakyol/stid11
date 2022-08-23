from gwf import Workflow
import glob

# Templates -------------------------------------
def fastp(file, trimmed):
    inputs = [file]
    outputs = [trimmed]
    options = {
        'cores': 12,
        'memory': '64g',
        'walltime': '12:00:00'
        }
    spec = '''
fastp -i {file} -o {trimmed} -q 30 -w 12 -g
    '''.format(file=file, trimmed=trimmed)
    return inputs, outputs, options, spec


def mapgz(file, prefix):
    inputs = [file]
    outputs = []
    options = {
        'cores': 12,
        'memory': '64g',
        'walltime': '12:00:00'
        }
    spec = '''
STAR --runThreadN 12 \
--readFilesCommand zcat \
--genomeDir /home/tyakyol/InRoot/dtd_map/data/genomeDir \
--alignIntronMax 2000 \
--outSAMtype BAM SortedByCoordinate \
--outFileNamePrefix {prefix} \
--readFilesIn {file}
        '''.format(file=file, prefix=prefix)
    return inputs, outputs, options, spec


# Workflow --------------------------------------
gwf = Workflow(defaults={'account': 'InRoot'})

samples = sorted(glob.glob('data/johan/*_1.fq.gz'))
prefix = [x[11:15] for x in samples]

for n, i in enumerate(samples):
    gwf.target_from_template('trim_{}'.format(n),
    fastp(
        file=i,
        trimmed='./output/johan_0/fastp/'+prefix[n]+'.fq.gz'
    ))

    gwf.target_from_template('map_{}'.format(n),
    mapgz(
    file='./output/johan_0/fastp/'+prefix[n]+'.fq.gz',
    prefix='./output/johan_0/'+prefix[n]
    ))
