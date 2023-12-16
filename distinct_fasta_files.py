#python3

#This script generates distinct fasta files from a multiple-sequence fasta file

work_dir = 'C:/Users/kacci/OneDrive/Computer/University_of_Malta/BioGeMT/Collab/Marion_Mangion/src/'

dict = {}
list= []

with open(work_dir + 'all_samples.txt','r') as infile:
    for line in infile.read().splitlines():
        if line.strip():
            line = line.split(':')
            dict[line[0]] = line[1]

for keys,values in dict.items():
    with open(work_dir+keys+'.fasta','w+') as outfile:
        outfile.write('>' + keys+'\n'+values)


