from fasta2dictionary import fasta_dictionary
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('work_dir',help='enter whole path to your reference haplotypes')
parser.add_argument('input',help='enter the name of the input file of the references haplotypes')
parser.add_argument('output',help='enter the name of the desired output')
args = parser.parse_args()

#work_dir='/home/kmota01/phylogenetic_analysis/src/reference_haplotypes'
#input='apis_melifera_haplotypes_ORIGINAL.fasta'
#output='reference_seq.fasta'

sel_list=['A8','A9','A2','A1','A4','C1','M7']
haplogroup_list=[f for f in os.listdir(args.work_dir) if f.startswith('A')]

if os.path.exists(args.work_dir+'/'+args.output):
    os.remove(args.work_dir+'/'+args.output)

for haplogroup in sel_list:
    for file in haplogroup_list:
        file=file.replace('.fasta','')
        if any(haplogroup==file for file in file.split('_')):
#            print(haplogroup,file)
            with open(args.work_dir+'/'+args.output,'a') as refile:
                with open(args.work_dir+'/'+file+'.fasta','r') as infile:
                    refile.writelines(infile)
                    refile.writelines(2*'\n')
                    
