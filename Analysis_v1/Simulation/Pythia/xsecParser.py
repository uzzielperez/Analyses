import re
import argparse
import os
import subprocess as sp
import ROOT 
from multiprocessing import Pool

parser = argparse.ArgumentParser(description='Cross Section File')
parser.add_argument('-i', '--inputfile', help='Choose inputfile.', type=str,
			default='outCO-2.txt')
args = parser.parse_args()

filename = args.inputfile


sw = ROOT.TStopwatch()
sw.Start()

def xsecParse(filetoparse):
	pattern = (r'sum\s+(.*)')
	new_file = []

	# Make sure file gets closed after being iterated
	with open(filetoparse, 'r') as f:
   		lines = f.readlines()

	for line in lines:
		match = re.findall(pattern, line)
		if match:
			match[0].split(" ")
			matchstring = str(match[0])
			matchstring = matchstring.split(" ")
			#print matchstring
			error = matchstring[-2]
			xsec = matchstring[-4]

	xsec_info = xsec + " +- " +  error
	print xsec_info

	f = open("FileInfoxsec.txt", "a")
	f.write('%s: %s\n'%(filetoparse, xsec_info))
	xsecListFile = open("xsecInfo.txt", "a") 
	xsecListFile.write('%s\n'%(xsec_info))


def ParsePythiaOutputFiles(file_list):
	for outFile in file_list:
		if "ADDGravToGG_NegInt" in outFile and outFile.endswith(".txt"):
			print "Parsing ", outFile
			xsecParse(outFile)

def multiproc(file_list, func):
	chunks = [file_list[i::5] for i in range(5)]
	pool = Pool(processes=5)
	result = pool.map(func, chunks)
	#return sum(result) 


#cmsRun_GenCard(os.listdir('.'))
#multiproc(os.listdir('.'), cmsRun_GenCard) 	
#xsecParse(filename)
ParsePythiaOutputFiles(os.listdir('.'))

sw.Stop()
print ("Processing Time:")
print ("Real time: " + str(sw.RealTime() / 60.0) + " minutes")
print ("CPU time: " + str(sw.CpuTime() /60.0) + " minutes")
                                                         	
