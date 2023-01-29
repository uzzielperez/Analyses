import os
import subprocess as sp
import ROOT

from multiprocessing import Pool

sw = ROOT.TStopwatch()
sw.Start()

cmsDriver_Step = True
cmsRun_Step    = False

def cmsDriver_GenCard(file_list):
	for filename in file_list:
		#Unparticles_du%d_LambdaU-%d_TuneCUEP8M1_13TeV_pythia8.py
		if "Unparticles" in filename and filename.endswith(".py"):
			cmsDriver_cmd = "cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/{} -s GEN --mc --no_exec --conditions auto:mc -n 100".format(filename)
			print cmsDriver_cmd
			process = sp.Popen(cmsDriver_cmd.split(), stdout=sp.PIPE)
			foutput, error = process.communicate()

def cmsRun_GenCard(file_list):
	for fn in file_list:
		if "Unparticles" in fn and fn.endswith("cfi_py_GEN.py"):
			cmsRun_cmd = "cmsRun {}".format(fn)
			logfilename = "{}.txt".format(fn[:-14])
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


if cmsDriver_Step:
	print "Running cmsDriver Step"

	#cmsDriver_GenCard(os.listdir('Configuration/GenProduction/python/ThirteenTeV/'))
	#multiproc(os.listdir('Configuration/GenProduction/python/ThirteenTeV/'), cmsDriver_GenCard)

	# print os.listdir('Configuration/GenProduction/python/ThirteenTeV/')
	#cmsDriver_GenCard(os.listdir('Configuration/GenProduction/python/ThirteenTeV/'))
	cmsDriver_cmd = "cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/{} -s GEN --mc --no_exec --conditions auto:mc -n 100".format("UnparToGG_Spin2_du1p9_LambdaU-3500_pT70_M3000_TuneCUEP8M1_13TeV_pythia8_cfi.py")
	process = sp.Popen(cmsDriver_cmd.split(), stdout=sp.PIPE)
	foutput, error = process.communicate()
	
if cmsRun_Step:
	#cmsRun_GenCard(os.listdir('.'))
	multiproc(os.listdir('.'), cmsRun_GenCard)

sw.Stop()
print ("Processing Time:")
print ("Real time: " + str(sw.RealTime() / 60.0) + " minutes")
print ("CPU time: " + str(sw.CpuTime() /60.0) + " minutes")
