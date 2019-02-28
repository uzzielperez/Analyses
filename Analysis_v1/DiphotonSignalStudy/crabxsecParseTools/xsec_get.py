import os
import sys
import re 
import argparse
from Parsefunctions import *

# Command line options
parser = argparse.ArgumentParser(description="cmsDriver")
parser.add_argument("-d", "--delete", action="store_true", help="run or delete")
parser.add_argument("-r", "--run", action="store_true")
parser.add_argument("-v", "--verbose", help="print evertything", action="store_true")
parser.add_argument("-p", "--parse", action="store_true")
parser.add_argument("-a", "--average", action="store_true")
parser.add_argument("-f", "--format", action="store_true")
args = parser.parse_args()



print "-d for delete, -r to get CRAB cmsRun stdout logs, -v for debugging, -p to parse xsecs, -a to get weighted average of xsecs per dataset"

#f = open("copythese.txt")
f = open("parsedis.txt")
lines = f.read().split('\n') #list containing each line
lines = lines[:-1] #to exclude last slots in lines which is white space

if args.delete:
	print "Cleaning directory.."
	print "Run python xsec_get.py -r to get cross sections (-v for verbose)"
	
for line in lines:
	
	pattern = r'DiPhotonAnalysis/xsec/([^(]*)_pythia8/crab' 
	if "ADD" in line:
		pattern = r'DiPhotonAnalysis/xsec/([^(]*)-pythia8/crab' 
	match = re.findall(pattern, line)	
	dataset = match[0]
        tagpattern = 'cmsRun_([^(]*).log.tar.gz'
	tag = re.findall(tagpattern, line)
	tarredsets = ".".join((dataset+tag[0], "tar.gz")) 

	# Copy the output 
	cmd = 'xrdcp %s %s' %(line, tarredsets)
	tarcmd = 'tar -xvf %s -C %s' %(tarredsets, dataset)

	if args.run:
		os.system(cmd)
		if not os.path.exists(dataset):	
			mkdircmd = 'mkdir %s' %(dataset)
			os.system(mkdircmd)	
		os.system(tarcmd)  
	if args.delete:
		os.system("rm -rf %s*" %(dataset))	
#	if args.verbose:	
#		print cmd
#		print tarcmd

if args.parse:
	print "Parsing Files"
	f = open("InfoXsecPb.txt", "w+")
	for dirdset in os.listdir('.'):
		if "Grav" in dirdset and "tar.gz" not in dirdset:
			print dirdset
			f.write("DATASET NAME: "+ dirdset+"\n")
			os.chdir(dirdset)
			for logfile in os.listdir('.'):	
				if "cmsRun-stdout" in logfile:
					info = xsecParse(logfile, dirdset)
					print info
					f.write(info+"\n")
			os.chdir("..")
	f.close()

if args.average:
	print "Calculating Average Cross-sections from parsed log files"
	#createDsetXsecDictiontary("InfoXsecPb.txt")
	for dirdset in os.listdir('.'):
		if ("Grav" in dirdset or "GluGlu" in dirdset) and "tar.gz" not in dirdset:
			if args.verbose:
				print dirdset
			os.chdir(dirdset)
			Ntotal, xsws, dws = 0., 0., 0.
			for logfile in os.listdir('.'):	
				if "cmsRun-stdout" in logfile:
					info = xsecParse(logfile, dirdset)
					#print info
					pattern1 = r"log: ([^(]*); Nevents"
					pattern2 = r"Nevents: ([^(]*)"
					match1 = re.findall(pattern1, info)[0].split(' +- ')
					match2 = re.findall(pattern2, info)[0]
					xsec, delta = match1
					nevts = match2
					xsec_weightedSum  = float(xsec)*float(nevts)
					delta_weightedSum = float(delta)*float(nevts)
					if args.verbose:
						print xsec, delta, nevts  
					Ntotal = Ntotal + float(nevts)
					xsws = xsws + xsec_weightedSum 
					dws  = dws  + delta_weightedSum
			xsec_ave = format(xsws/Ntotal, "10.3e")
			delt_ave = format(dws/Ntotal, "10.3e")	
			if args.verbose:
				print "Ntotal: ", Ntotal, ";Average xsec +- deltaxsec:", xsec_ave, delt_ave 
		   	hardcode_txt = 'if(sample.Contains("%s_pythia8")) xsec = %s;' %(dirdset, xsec_ave)
			if "ADD" in dirdset:
				 hardcode_txt = 'if(sample.Contains("%s-pythia8")) xsec = %s;' %(dirdset, xsec_ave)
			print hardcode_txt	
			os.chdir("..")

