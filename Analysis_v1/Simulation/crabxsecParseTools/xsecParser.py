import re
import argparse
import os
import subprocess as sp
import ROOT 
from multiprocessing import Pool
from decimal import *


sw = ROOT.TStopwatch()
sw.Start()

def xsecParse(filetoparse):
	
	pattern = r'After filter: final cross section = ([^(]*) pb'
	
	# Make sure file gets closed after being iterated
	with open(filetoparse, 'r') as f:
   		lines = f.readlines()

	for line in lines:
		match = re.search(pattern, line)
		if match:
			print "xsec for %s: %s" %(filetoparse, line)
			#print line
			f = open("pbcrabxsec.txt", "a")
			f.write("xsec for %s: %s" %(filetoparse, line))

#f = open("copythese.txt")
f = open("parsedis.txt")
lines = f.read().split('\n') #list containing each line
lines = lines[:-1] #to exclude last slot in lines which is white space

for line in lines:
        pattern = r'DiPhotonAnalysis/xsec/([^(]*)_pythia8/crab'
        match = re.findall(pattern, line)
	filename = "/".join((match[0], "cmsRun-stdout-1.log"))
	xsecParse(filename) 
	#print filename

#xsecParse("GluGluSpin0ToGG_W-0p014_M-1250_TuneCUEP8M1_13TeV/cmsRun-stdout-1.log")

sw.Stop()
print ("Processing Time:")
print ("Real time: " + str(sw.RealTime() / 60.0) + " minutes")
print ("CPU time: " + str(sw.CpuTime() /60.0) + " minutes")
                                                         	
