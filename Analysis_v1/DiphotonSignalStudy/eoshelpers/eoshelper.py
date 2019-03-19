import subprocess
import os
import argparse

# Command line options
parser = argparse.ArgumentParser(description="eoshelper")
parser.add_argument("-i", "--inputfile", default="processdis.txt", help="Input datasets.")
parser.add_argument("-o", "--output", default=None, help="Print with redirector or /store/.../timestamp/{rootdir}")
parser.add_argument("-t", "--timestamp", action="store_true", help="Choose this option if you don't know the timestamped directories.")
parser.add_argument("-f", "--formatter", action="store_true", help="Choose this flag if you know the timestamped directories and you want to create the list you want to parse")
args = parser.parse_args()


inputfile = args.inputfile
outputOpt = args.output
if args.formatter:
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
		mitredirector = "root://cmsxrootd.fnal.gov/"+datadir

		if outputOpt is None:
			print datadir[:-1]
		else:
			print mitredirector[:-1]

if args.timestamp:
	inputfile = "timestampdis.txt"
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
		(rf, err) = proc.communicate()
		rootdir = "%s/%s" %(rootdir, rf[:-1])
		print rootdir
		# cmd = "eos root://cmseos.fnal.gov ls %s" %(rootdir)
		# proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		# (logdir, err) = proc.communicate()
		# tardir = "%s/%s" %(rootdir, logdir[:-1])


		ft.write(rootdir+"\n")
	ft.close()
