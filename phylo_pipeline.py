#python3

import os
import subprocess

dir = '/home/kmota01/apis_melifera' 
phylip = '/home/kmota01/apps/phylip-3.697/exe'
dnadist = '/home/kmota01/apps/phylip-3.697/exe/dnadist' 
neighbor = '/home/kmota01/apps/phylip-3.697/exe/neighbor'
drawgram = '/home/kmota01/apps/phylip-3.697/exe/drawgram'
clustalo = '/home/kmota01/apps/clustal-omega/clustalo'

os.chdir(phylip)
for file in os.listdir(dir+'/src/msa_inputs/'):
    if file.endswith('.fasta'):

        sample = file.replace('_combined_haplotypes.fasta', '')
        output_dir = dir + '/result/' + sample + '/'

        if not os.path.exists(dir+'/result/'+sample):
            os.makedirs(dir+'/result/'+sample)
        if os.path.isfile(output_dir + sample + '.phy'):
            os.remove(output_dir + sample + '.phy')
        if os.path.isfile(output_dir + 'outfile'):
            os.remove(output_dir + 'outfile')
        if os.path.isfile(output_dir + 'intree'):
            os.remove(output_dir + 'intree')
        if os.path.isfile(output_dir + 'plotfile'):
            os.remove(output_dir + 'plotfile')


#        print(dir+'/src/msa_inputs/' + file)
#        print(output_dir+sample+'.phy')
        run_msa = subprocess.run([clustalo,'-i',dir + '/src/msa_inputs/' + file,'-o',output_dir + sample + '.phy','--outfmt=phylip'],shell=True)
        print(run_msa)
#        move_infile = subprocess.run(['move',output_dir + sample + '.phy',phylip + '/infile'],shell=True,input=run_msa.stdout,stdout=subprocess.PIPE)
#        print(move_infile.stdout.decode("utf-8"))
#
#        run_dnadist = subprocess.run(['echo','Y','|',dnadist],shell=True,input=move_infile.stdout,stdout=subprocess.PIPE)
#        print(run_dnadist.stdout.decode("utf-8"))
#
#        move1_infile = subprocess.run(['move','infile', output_dir + sample + '.phy'],shell=True,input=run_dnadist.stdout,stdout=subprocess.PIPE)
#        print(move1_infile.stdout.decode("utf-8"))
#
#        rename_outfile = subprocess.run(['move','outfile', output_dir + 'infile'], shell=True,input=move1_infile.stdout,stdout=subprocess.PIPE)
#        print(rename_outfile.stdout.decode("utf-8"))
#
#        cp_infile = subprocess.run(['copy',output_dir + 'infile',phylip],shell=True,input=rename_outfile.stdout,stdout=subprocess.PIPE)
#        print(cp_infile.stdout.decode("utf-8"))
#
#        run_neighbor = subprocess.run(['echo','Y','|',neighbor], shell=True,input=cp_infile.stdout,stdout=subprocess.PIPE)
#        print(run_neighbor.stdout.decode("utf-8"))
#
#        rename_outtree = subprocess.run(['move','outtree','intree'], shell=True,input=run_neighbor.stdout, stdout=subprocess.PIPE)
#        print(rename_outtree.stdout.decode("utf-8"))
#
#        run_drawgram = subprocess.run(['echo','Y','|', drawgram], shell=True,input=run_neighbor.stdout,stdout=subprocess.PIPE)
#        print(run_drawgram.stdout.decode("utf-8"))
#
#        mv_outfile = subprocess.run(['move','outfile',output_dir], shell=True,input=run_drawgram.stdout,stdout=subprocess.PIPE)
#        print(mv_outfile.stdout.decode("utf-8"))
#
#        mv_outtree = subprocess.run(['move','intree',output_dir], shell=True,input=mv_outfile.stdout, stdout=subprocess.PIPE)
#        print(mv_outtree.stdout.decode("utf-8"))
#
#        mv_plotfile = subprocess.run(['move','plotfile',output_dir], shell=True,input=mv_outtree.stdout, stdout=subprocess.PIPE)
#        print(mv_plotfile.stdout.decode("utf-8"))
#
#        del_infile = subprocess.run(['del','infile'], shell=True,input=mv_plotfile.stdout,stdout=subprocess.PIPE)
#        print(del_infile.stdout.decode("utf-8"))
#
#
#
#
#
#
#
#
#
#
