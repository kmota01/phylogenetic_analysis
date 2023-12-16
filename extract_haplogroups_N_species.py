from fasta2dictionary import fasta_dictionary
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('work_dir',help='enter whole path to your reference haplotypes')
parser.add_argument('input',help='enter the name of the input file of the references haplotypes')
#parser.add_argument('output',help='enter the name of the desired output')
args = parser.parse_args()

#work_dir='/home/kmota01/phylogenetic_analysis/src/reference_haplotypes'
#input='apis_melifera_haplotypes_ORIGINAL.fasta'

with open(args.work_dir+'/'+args.input,'r') as file:

    dict,dict_fasta = {},{}
    dict = fasta_dictionary(file)

    haplogroup_pattern=r"[A-Z]\d+['\"]?"
    haplogroup_list,species_list = [],[]
    for keys,values in dict.items():
        if re.fullmatch(haplogroup_pattern,keys.split()[4]):
            header=keys
            haplogroup=keys.split()[4]
            species='_'.join(keys.split()[1:3])
            haplogroup_list.append(haplogroup)
            species_list.append(species)
        elif re.fullmatch(haplogroup_pattern,keys.split()[5]):
            header=keys
            haplogroup=keys.split()[5]
            species='_'.join(keys.split()[1:4])
            haplogroup_list.append(haplogroup)
            species_list.append(species)
        
        dict_fasta[species + ' ' + haplogroup]=values       

        with open(args.work_dir + '/' + species + '_' + haplogroup + '.fasta', 'w') as outfile:
            outfile.writelines(header+'\n'+values)


#     with open(args.work_dir + '/args.output', 'w') as outfile:
#         for haplo,keys,values in zip(species_list,dict.keys(),dict.values()):
#             new_key = keys.replace(keys[1:11],haplo+' '+keys[1:11])
#             print(new_key+'\n'+values)
#             outfile.writelines(new_key+'\n'+values)
#
