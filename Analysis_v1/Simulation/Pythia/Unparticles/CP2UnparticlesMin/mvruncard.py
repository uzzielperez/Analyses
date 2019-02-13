import os
import subprocess as sp
import ROOT 
import argparse
from multiprocessing import Pool

# Command line options
parser = argparse.ArgumentParser(description="cmsDriver")
parser.add_argument("-p", "--pattern", help="File Name pattern")
parser.add_argument("-d", "--directory", help="config or src")
args = parser.parse_args()

pattern = args.pattern
directory = args.directory

sw = ROOT.TStopwatch()
sw.Start()

def moveCard(folder, pattern):
	file_list = os.listdir(folder) 
 	for filename in file_list:
		if filename.startswith("%s" %(pattern)) and filename.endswith(".txt"):
			cmd = "mv /uscms_data/d3/cuperez/CMSSW_9_3_8/src/{}  /uscms_data/d3/cuperez/CMSSW_9_3_8/src/fin".format(filename)
			os.system(cmd)
			print "moved %s to fin/" %(filename)
		if filename.startswith("%s" %(pattern)) and filename.endswith(".py"):
			if "Configuration" in folder:			
				cmd = "mv /uscms_data/d3/cuperez/CMSSW_9_3_8/src/Configuration/GenProduction/python/ThirteenTeV/{}  /uscms_data/d3/cuperez/CMSSW_9_3_8/src/Configuration/GenProduction/python/ThirteenTeV/fin".format(filename)
			else:
				cmd = "mv /uscms_data/d3/cuperez/CMSSW_9_3_8/src/{}  /uscms_data/d3/cuperez/CMSSW_9_3_8/src/fin".format(filename)
			os.system(cmd)
			print "moved %s to fin/" %(filename)

if directory == "config":
	moveCard('/uscms_data/d3/cuperez/CMSSW_9_3_8/src/Configuration/GenProduction/python/ThirteenTeV/', pattern)
else: 
	moveCard('/uscms_data/d3/cuperez/CMSSW_9_3_8/src/', pattern)

sw.Stop()
print ("Processing Time:")
print ("Real time: " + str(sw.RealTime() / 60.0) + " minutes")
print ("CPU time: " + str(sw.CpuTime() /60.0) + " minutes")
