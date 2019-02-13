import os
import subprocess as sp
import ROOT 
import argparse
from multiprocessing import Pool

# Command line options
parser = argparse.ArgumentParser(description="cmsDriver")
parser.add_argument("-p", "--pattern", help="File Name pattern")
parser.add_argument("-s", "--step", help="cmsDriver step is True. Empty string evaluates to false")
parser.add_argument("-n", "--nEvents", default=10000, help="number of Events")  
args = parser.parse_args()

pattern = args.pattern
cmsDriver = args.step 
nEvents = args.nEvents

sw = ROOT.TStopwatch()
sw.Start()

#pattern = "STest1p8Unp1500p0_spin-0_M_500-2000"
#pattern = "MCI"
#pattern = "MCIPlus_SM"
#pattern = "MCIPlus0"
#pattern = "MCIPlus2"
#pattern = "MCI_Unp-LU500-du1p8_spin-0"
#pattern = "MCI_Unp-LU500-du1p8_spin-0_pT125"
#pattern = "MCI_Unp-LU500-du1p8_spin-0-ggON"
#pattern = "MCI_Unp-LU500-du1p8_spin-2"
#pattern = "MCI_Unp-LU500-du1p8_spin-2-ggffON"
#pattern = "MCI_Unp-LU500-du1p8_spin-2_pT125"
#pattern = "MCI_Unp-LU500-du1p8_spin-2-ggON"
#pattern = "MCI_SM_pT125"
#pattern = "MCI_Unp-LU500-du1p8_spin-0-ggffON"

def cmsDriver_GenCard(file_list):
	for filename in file_list:
		if filename.startswith("%s" %(pattern)) and filename.endswith(".py"):
		#if "ADDGravToGG_NegInt-1_LambdaT-13000" in filename and filename.endswith(".py"):
			cmsDriver_cmd = "cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/{} -s GEN --mc --no_exec --conditions auto:mc -n {}".format(filename, nEvents) 
			print cmsDriver_cmd
			process = sp.Popen(cmsDriver_cmd.split(), stdout=sp.PIPE)
			foutput, error = process.communicate()

def cmsRun_GenCard(file_list):
	for fn in file_list:
		if fn.startswith("%s" %(pattern)) and fn.endswith("_py_GEN.py"):
		#if "ADDGravToGG_NegInt-1_LambdaT-13000" in fn and fn.endswith("cfi_py_GEN.py"):
			cmsRun_cmd = "cmsRun {}".format(fn)
			logfilename = "{}.txt".format(fn[:-7])
			logfile = open(logfilename, 'w')
			print cmsRun_cmd, logfilename
			run = sp.Popen(cmsRun_cmd.split(), stdout=logfile)
			foutput, error = run.communicate()

        		#if os.path.isfile(fn): # for all files in current working directory  


def multiproc(file_list, func):
	chunks = [file_list[i::5] for i in range(5)]
	pool = Pool(processes=5)
	result = pool.map(func, chunks)
	#return sum(result) 


if cmsDriver:
	print "cmsDriver cfg step"
	#cmsDriver_GenCard(os.listdir('Configuration/GenProduction/python/ThirteenTeV/'))
	multiproc(os.listdir('Configuration/GenProduction/python/ThirteenTeV/'), cmsDriver_GenCard) 	
else:
	print "Generate step"
	#cmsRun_GenCard(os.listdir('.'))
	multiproc(os.listdir('.'), cmsRun_GenCard) 	

sw.Stop()
print ("Processing Time:")
print ("Real time: " + str(sw.RealTime() / 60.0) + " minutes")
print ("CPU time: " + str(sw.CpuTime() /60.0) + " minutes")
