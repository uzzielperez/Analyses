import subprocess
import os
import re 
with open("scratchdatasetlist.txt", 'r') as f:
	datasetlist = f.readlines()

outdir = "root://cmseos.fnal.gov//eos/uscms/store/user/cuperez/DiPhotonAnalysis/EGammaData/EGamma/"

for dataset in datasetlist:
	outfile = dataset.split('crab_EGamma__', 1)[-1][:-1]
	outfile = outfile.replace("/", "-")
	cmd = "skim.exe %s %sskimmed.root" %(dataset, outfile)
	print cmd
	#os.system(cmd)
