import subprocess
import os

inputfile = "processdis.txt"

with open(inputfile, 'r') as f:
	datasetlist = f.readlines()

for dataset in datasetlist:
	cmd = "eos root://cmseos.fnal.gov ls %s" %(dataset)
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	(subdir, err) = proc.communicate()
	rootdir = "%s/%s" %(dataset[:-1], subdir)
	#print rootdir

	getrootdir = "eos root://cmseos.fnal.gov ls %s" %(rootdir)
	proc = subprocess.Popen(getrootdir, stdout=subprocess.PIPE, shell=True)
        (subrootdir, err) = proc.communicate()
	datadir = "%s/%s" %(rootdir[:-1], subrootdir)

	print datadir[:-1]

	
