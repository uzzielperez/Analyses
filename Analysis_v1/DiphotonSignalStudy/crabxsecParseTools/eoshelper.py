import subprocess
import os
import argparse

# Command line options
parser = argparse.ArgumentParser(description="eoshelper")
parser.add_argument("-i", "--inputfile", default="processdis.txt", help="Input datasets.")
parser.add_argument("-o", "--output", default=None, help="Slightly different from the general eoshelper for plots.")
args = parser.parse_args()


inputfile = args.inputfile
outputOpt = args.output

with open(inputfile, 'r') as f:
	datasetlist = f.readlines()

for dataset in datasetlist:
	cmd = "eos root://cmseos.fnal.gov ls %s" %(dataset)
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	(tarfiles, err) = proc.communicate()
	pathTotarfile = "%s/%s" %(dataset[:-1], tarfiles)
	
	# Writing all the tar files in a list 
	tarfileslist = tarfiles[:-1].split()
	for tarfile in tarfileslist:
		pathTotarfile = "%s/%s" %(dataset[:-1], tarfile)
		print pathTotarfile

	if outputOpt is not None:	
		print tarfile
		getrootdir = "eos root://cmseos.fnal.gov ls %s" %(rootdir)
		proc = subprocess.Popen(getrootdir, stdout=subprocess.PIPE, shell=True)
		(subrootdir, err) = proc.communicate()
		datadir = "%s/%s" %(rootdir[:-1], subrootdir)
		mitredirector = "root://cmsxrootd.fnal.gov/"+datadir 
		tarfile = mitredirector[:-1]+"/cmsRun_1.log.tar.gz"


	
