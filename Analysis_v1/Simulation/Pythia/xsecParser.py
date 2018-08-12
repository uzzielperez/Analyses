import re
import argparse
import os
import subprocess as sp
import ROOT 
from multiprocessing import Pool

parser = argparse.ArgumentParser(description='Cross Section File')
parser.add_argument('-i', '--inputfile', help='Choose inputfile.', type=str, default='datasetlist2017-18.txt')
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


def CWDParsePythiaOutputFiles(file_list):
	for outFile in file_list:
		if "ADDGravToGG_NegInt" in outFile and outFile.endswith(".txt"):
			print "Parsing ", outFile
			xsecParse(outFile)

def ParseFileList(file_list):
	with open(file_list, 'r') as f: 
   		files = f.readlines() 
 
	for outfile in files:
		text_to_parse = ".".join((outfile[:-1], "txt"))
		print text_to_parse
		xsecParse(text_to_parse)

#CWDParsePythiaOutputFiles(os.listdir('.'))
ParseFileList(filename)

sw.Stop()
print ("Processing Time:")
print ("Real time: " + str(sw.RealTime() / 60.0) + " minutes")
print ("CPU time: " + str(sw.CpuTime() /60.0) + " minutes")
                                                         	
