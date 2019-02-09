import re
import argparse
import os
import subprocess as sp
import ROOT
from multiprocessing import Pool
from decimal import *

parser = argparse.ArgumentParser(description='Cross Section File')
parser.add_argument('-p', '--pattern', help='File Pattern to parse', type=str, default='')
args = parser.parse_args()

patternstr = args.pattern
#patternstr = "MCI_Unp-LU500-du1p8_spin-0-ggON_pT125_M_2000_TuneCP2_py"
#patternstr = "MCI_Unp-LU500-du1p8_spin-0"
#patternstr = "MCIPlus"
#patternstr = "MCIPlus2_Unp-LU500-du1p8_spin-2-ggON"

sw = ROOT.TStopwatch()
sw.Start()

def xsecParse(filetoparse):
	pattern = (r'sum\s+(.*)')
	unit   = (r'Accepted\s+(.*)')
	new_file = []

	# Make sure file gets closed after being iterated
	with open(filetoparse, 'r') as f:
   		lines = f.readlines()

	for line in lines:
		match = re.findall(pattern, line)
		unitstring = re.findall(unit, line)
		if match:
			match[0].split(" ")
			matchstring = str(match[0])
			matchstring = matchstring.split(" ")
			#print matchstring
			error = matchstring[-2]
			xsec = matchstring[-4]

	xsec_info = xsec + " +- " +  error
	xsec_pb, error_pb = Decimal(xsec)*(10**9), Decimal(error)*(10**9)
	xsec_info_pb = str('{:.3e}'.format(float(xsec_pb))) + "+-" + str('{:.3e}'.format(float(error_pb)))

	#print xsec_info, " mb; ", xsec_info_pb, " pb", unitstring
	filename ="pb_%s_Filexsec.txt" %(patternstr) 
	print filetoparse,": " ,xsec_info_pb
	f = open("pb_%s_Filexsec.txt" %(patternstr), "a")
	f.write('%s, %s\n'%(filetoparse, xsec_info_pb))
	
	xsecListFile = open("pb_%s_xsecInfo.txt" %(patternstr), "a")
	xsecListFile.write('%s\n'%(xsec_info_pb))
	catcmd = "cat pb_%s_Filexsec.txt" %(patternstr)
	#os.system(catcmd)
def ParseFileList(file_list):
	for outfile in file_list:
		if outfile.startswith("%s" %(patternstr)) and outfile.endswith(".txt"):
			#print outfile
			xsecParse(outfile)

ParseFileList(os.listdir('.'))

sw.Stop()
print ("Processing Time:")
print ("Real time: " + str(sw.RealTime() / 60.0) + " minutes")
print ("CPU time: " + str(sw.CpuTime() /60.0) + " minutes")
