import os
import subprocess as sp

cmsDriver_Step = False
cmsRun_Step = True

if cmsDriver_Step:
	for filename in os.listdir('Configuration/GenProduction/python/ThirteenTeV/'):	
		if "ADDGravToGG_NegInt" in filename and filename.endswith(".py"):
			cmsDriver_cmd = "cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/{} -s GEN --mc --no_exec --conditions auto:mc -n 1000".format(filename) 
			print cmsDriver_cmd
			process = sp.Popen(cmsDriver_cmd.split(), stdout=sp.PIPE)
			foutput, error = process.communicate()

if cmsRun_Step:
	for fn in os.listdir('.'):
		if "ADDGravToGG_NegInt" in fn and fn.endswith("cfi_py_GEN.py"):
			cmsRun_cmd = "cmsRun {} > {}.txt".format(fn, fn[:-14])
			print cmsRun_cmd
			run = sp.Popen(cmsRun_cmd.split(), stdout=sp.PIPE)
			foutput, error = run.communicate()

        	#if os.path.isfile(fn): # for all files in current working directory  

