#python3

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('work_dir',help='enter whole path to your reference haplotypes')
parser.add_argument('input',help='enter the name of the input file of the references haplotypes')
args = parser.parse_args()

#work_dir='/home/kmota01/phylogenetic_analysis'
#input='apis_melifera_haplotypes.fasta'

clustalo_work_dir=''

with open(args.work_dir+'/src/reference_haplotypes/'+args.input,'r') as infile:
    ref_haplotype = infile.read()
    samples = [f for f in os.listdir(args.work_dir+'/src/samples') if f.endswith('.fasta')]
    for sample in samples:
        with open(args.work_dir+'/src/samples/'+sample,'r') as sample_file:
            sample_seq = sample_file.read()
            with open(args.work_dir+'/msa_inputs/'+sample.replace('.fasta','')+'_combined_haplotypes.fasta','w+') as outfile:
                outfile.write(sample_seq+2*'\n'+ref_haplotype)


