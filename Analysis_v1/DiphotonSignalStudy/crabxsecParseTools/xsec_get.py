import os
import sys
import re 
import subprocess
import os
import argparse

# Command line options
parser = argparse.ArgumentParser(description="eoshelper")
parser.add_argument("-i", "--inputfile", default="parsedis.txt", help="Input datasets.")
parser.add_argument("-o", "--output", default=None, help="Print with redirector or /store/.../timestamp/{rootdir}")
args = parser.parse_args()

inputfile = args.inputfile
outputOpt = args.output

f = open(inputfile)
lines = f.read().split('\n') #list containing each line
lines = lines[:-1] #to exclude last slots in lines which is white space

for line in lines:	
	print "NEW: ",line
	pattern = r'DiPhotonAnalysis/xsec/([^(]*)_pythia8/crab' 
	if "ADD" in line:
		pattern = r'DiPhotonAnalysis/xsec/([^(]*)-pythia8/crab' 
	match = re.findall(pattern, line)	
	#print match
	dataset = match[0]
	tarredsets = ".".join((dataset, "tar.gz")) 
	
	# Copy the output 
	cmd = 'xrdcp %s %s' %(line, tarredsets)
	print cmd
	os.system(cmd)	
	mkdircmd = 'mkdir %s' %(dataset)
	os.system(mkdircmd)
	
	# Untar 
	tarcmd = 'tar -xvf %s -C %s' %(tarredsets, dataset)
	os.system(tarcmd)  
	print tarcmd
	#print "copying %s" %(fileout)
	#os.system(cmd)

