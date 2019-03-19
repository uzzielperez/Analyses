import subprocess
import os
import argparse

# Command line options
parser = argparse.ArgumentParser(description="eoshelper")
parser.add_argument("-i", "--inputfile", default="processdis.txt", help="Input datasets.")
parser.add_argument("-o", "--output", default=None, help="Slightly different from the general eoshelper for plots.")
parser.add_argument("-t", "--timestamp", action="store_true", help="Choose this option if you don't know the timestamped directories.")
parser.add_argument("-f", "--formatter", action="store_true", help="Choose this flag if you know the timestamped directories and you want to create the list you want to parse")
args = parser.parse_args()


inputfile = args.inputfile
outputOpt = args.output

if args.timestamp:
	with open(inputfile, 'r') as f:
		datasetlist = f.readlines()
	outputfile = "newprocessdis.txt"
	ft = open(outputfile, "w+")
	# Looking for timestamps
	for dirdset in datasetlist:
		cmd = "eos root://cmseos.fnal.gov ls %s" %(dirdset)
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		(cdir, err) = proc.communicate()
		datadir = "%s/%s" %(dirdset[:-1], cdir[:-1])
		cmd = "eos root://cmseos.fnal.gov ls %s" %(datadir)
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		(tdir, err) = proc.communicate()
		rootdir = "%s/%s" %(datadir, tdir[:-1])
		cmd = "eos root://cmseos.fnal.gov ls %s" %(rootdir)
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		(tardir, err) = proc.communicate()
		rootdir = "%s/%s" %(rootdir, tardir[:-1])
		cmd = "eos root://cmseos.fnal.gov ls %s" %(rootdir)
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		(logdir, err) = proc.communicate()
		tardir = "%s/%s" %(rootdir, logdir[:-1])

		print tardir
		ft.write(tardir+"\n")
	ft.close()

		#mitredirector = "root://cmsxrootd.fnal.gov/"+datadir
		#tarfile = mitredirector[:-1]+"/cmsRun_1.log.tar.gz"
		#subprocess.call(cmd, shell=True)
		#os.system(cmd) # won't work with aliases


if args.formatter:
	with open(inputfile, 'r') as f:
		datasetlist = f.readlines()

	for dataset in datasetlist:
		cmd = "eos root://cmseos.fnal.gov ls %s" %(dataset)
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		(tarfiles, err) = proc.communicate()
		pathTotarfile = "%s/%s" %(dataset[:-1], tarfiles)

		# Writing all the tar files in a list
		tarfileslist = tarfiles[:-1].split()
		redirector   = "root://cmsxrootd.fnal.gov/"
		for tarfile in tarfileslist:
			pathTotarfile = "%s%s/%s" %(redirector, dataset[:-1], tarfile)
			print pathTotarfile

		if outputOpt is not None:
			print tarfile
			getrootdir = "eos root://cmseos.fnal.gov ls %s" %(rootdir)
			proc = subprocess.Popen(getrootdir, stdout=subprocess.PIPE, shell=True)
			(subrootdir, err) = proc.communicate()
			datadir = "%s/%s" %(rootdir[:-1], subrootdir)
			mitredirector = "root://cmsxrootd.fnal.gov/"+datadir
			tarfile = mitredirector[:-1]+"/cmsRun_1.log.tar.gz"
