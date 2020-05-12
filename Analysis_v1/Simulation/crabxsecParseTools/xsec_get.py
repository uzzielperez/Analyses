import os
import sys
import re

#f = open("copythese.txt")
f = open("parsedis.txt")
lines = f.read().split('\n') #list containing each line
lines = lines[:-1] #to exclude last slots in lines which is white space

for line in lines:
	print "NEW: ",line
	pattern = r'Triphoton/xsec/([^(]*)_pythia8/crab'
	# pattern = r'DiPhotonAnalysis/xsec/([^(]*)_pythia8/crab'
	match = re.findall(pattern, line)
	#print match
	dataset = match[0]
	if os.path.exists(dataset):
		dataset = dataset + "2"
	tarredsets = ".".join((dataset, "tar.gz"))

	# Copy the output
	cmd = 'xrdcp %s %s' %(line, tarredsets)
	print cmd
	os.system(cmd)
	dataset_dir = dataset
	if (os.path.isdir(dataset_dir)):
		# if the directory name already exists
		# append 2
		dataset_dir = dataset + "2"
	else:
		dataset_dir = dataset
	mkdircmd = 'mkdir %s' %(dataset_dir)
	os.system(mkdircmd)

	# Untar
	tarcmd = 'tar -xvf %s -C %s' %(tarredsets, dataset_dir)
	os.system(tarcmd)
	print tarcmd
	#print "copying %s" %(fileout)
	#os.system(cmd)
