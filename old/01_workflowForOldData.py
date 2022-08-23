from gwf import Workflow
from templates import *
import glob

gwf = Workflow(defaults={'account': 'InRoot'})

samples_1 = sorted(glob.glob('/home/tyakyol/InRoot/johan_rnaseq/reads/*_1.fq.gz'))


for n, i in enumerate(samples_1):
    gwf.target_from_template('correct_{}'.format(n),
    fastp(
        file1=i,
        corrected='./fastp' + i[39:]
    ))

    gwf.target_from_template('map_{}'.format(n),
    map_pr_gz(
    file1='./fastp' + i[39:]
    ))
