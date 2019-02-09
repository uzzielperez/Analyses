import sys
import os 
import subprocess as sp 
import math

width = '5p6'
M = [750,1000,1250,1500,1750,2000,2250,2500,3000,3500,4000,4500,4750,5000]
      
print "Writing generator fragments... "
for m in M:
	command = 'python runCardGenHeavyHiggs.py -w %s -m %d' %(width, m)		
	os.system(command)
		
	genfrag = 'GluGluSpin0ToGammaGamma_W_%s_M_%d_TuneCP5_13TeV_pythia8_cfi.py' %(width, m)	
	dataset = 'GluGluSpin0ToGammaGamma_W_%s_M_%d_TuneCP5_13TeV_pythia8' %(width, m)	

	f = open("datasetHeavyHiggs.txt", "a")
	f.write('%s\n'%(dataset))
        fi = open("generatorFragmentListHeavyHiggs.txt", "a")
        fi.write('%s\n'%(genfrag))                                                    


