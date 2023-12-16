#bin/bash

dir=$'/home/kmota01/phylogenetic_analysis'
phylip=$'/home/kmota01/apps/phylip-3.697/exe'
clustalo=$'/home/kmota01/apps/clustal-omega/clustalo'
dnadist=$'/home/kmota01/apps/phylip-3.697/exe/dnadist'
neighbor=$'/home/kmota01/apps/phylip-3.697/exe/neighbor'
drawgram=$'/home/kmota01/apps/phylip-3.697/exe/drawgram'

cd $phylip

for file in $dir/src/msa_inputs/*.fasta;do
	sample=$(echo $file | awk -F '/' '{print $NF}')
	sample=$(echo $sample | sed "s/"_combined_haplotypes.fasta"/""/")
	echo $sample
	outdir=$dir/$sample
	mkdir $outdir	


	if [[ -f $outdir/$sample.phy ]] && [[ -f $outdir/infile_neighbor ]] && [[ -f $outdir/intree ]] && [[ -f $outdir/outfile ]] && [[ -f $outdir/plotfile ]];
	then
		continue
	else
		echo $sample "files dont exist!"
	fi


	#subprocesses
	a=$(clustalo -i $file -o $outdir/$sample.phy --outfmt=phylip)
	b=$(cp $outdir/$sample.phy $phylip/infile)
	c=$(echo 'Y' | $dnadist)
	d=$(rm infile && cp outfile $outdir/infile_neighbor && mv outfile infile )
	e=$(echo 'Y' | $neighbor)
	f=$(rm infile && mv outtree intree)
	g=$(echo 'Y' | $drawgram )
	h=$(mv outfile intree plotfile $outdir)
	
	#run subprocess
	for proc in [a,b,c,d,e,f,g,h];do
		echo $sample "Done"	
	done
done	
