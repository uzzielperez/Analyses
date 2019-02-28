import re
import argparse
import os
import subprocess as sp
import ROOT 
from multiprocessing import Pool
from decimal import *


sw = ROOT.TStopwatch()
sw.Start()

def xsecParse(filetoparse, tag=None):
	
	pattern  = r'After filter: final cross section = ([^(]*) pb'
	Neventspattern = r'- Number of Events:  ([^(]*)'
	
	# Make sure file gets closed after being iterated
	with open(filetoparse, 'r') as f:
   		lines = f.readlines()

	for line in lines:
		match   = re.search(pattern, line)
		Nevents = re.search(Neventspattern, line)
		
		if match:
			xsec = re.findall(pattern, line)[0]
			xsec_out = "xsec for %s: %s" %(filetoparse, xsec)
		if Nevents:
			Nevents = re.findall(Neventspattern, line)[0]
			Neventsout =  "Nevents: %s" %(Nevents)

	TextfileInfo = xsec_out + "; " + Neventsout 
	#	print fileInfo[:-1]
	return TextfileInfo[:-1]			

def createDsetXsecDictiontary(filetoparse):
	Total = 0 
	dsetpattern = r'DATASET NAME: ([^(]*)'	
	xsecpattern = r'xsec for ([^(]*): ([^(]*)'
	nvtspattern = r'Nevents: ([^(]*)'
	
	# Make sure file gets closed after being iterated
	with open(filetoparse, 'r') as f:
   		lines = f.readlines()

	for line in lines:
		dsetmatch = re.search(dsetpattern, line)
		xsecmatch = re.search(xsecpattern, line)
		nvtsmatch = re.search(nvtspattern, line)
	
		if dsetmatch:
			DATASET = re.findall(dsetpattern, line)[0]
			print DATASET[:-1]			
		if xsecmatch:
			xsecInfo = re.findall(xsecpattern, line)[0][0]
			xsec_uncertainty = r".log: ([^(]*) +- ([^(]*); Nevents"
			xsecDeltaMatch = re.findall(xsec_uncertainty, xsecInfo)	
			#xsec, Delta = xsecDeltaMatch[0]
			#print xsec, "pm", Delta
		if nvtsmatch:
			nvts = re.findall(nvtspattern, line)[0]
			print nvts[:-1]
			Total = Total + int(nvts)
	print "Total Events: %s, Average xsec: " %(Total)

sw.Stop()
print ("Processing Time:")
print ("Real time: " + str(sw.RealTime() / 60.0) + " minutes")
print ("CPU time: " + str(sw.CpuTime() /60.0) + " minutes")
                                                         
