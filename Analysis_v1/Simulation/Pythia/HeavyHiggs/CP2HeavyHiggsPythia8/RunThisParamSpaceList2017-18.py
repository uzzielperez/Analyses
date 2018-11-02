import sys
import os 
import subprocess as sp 
import math

width = ['0p014', '1p4', '5p6']
M = [[750,1000,1250,1500,1750,2000, 2250, 2500, 2750, 3000, 3250,3500,4000,4500,5000],
     [750,1000,1250,1500,1750,2000,2250, 2500,3000,3500,4000,4250,4500,4750,5000],
     [750,1000,1250,1500,1750,2000,2250,2500,3000,3500,4000,4500,4750,5000]]
       
print "Writing generator fragments... "
i = 0 
while i < len(width):
	for m in M[i]:
		#print "coupling: ", k[i], "; m0: ", m
		command = 'python runCardGenHeavyHiggs.py -w %s -m %d' %(width[i], m)		
		#print command 
		#process = sp.Popen(command.split(), stdout=sp.PIPE)
		#output, error = process.communicate()
		os.system(command)
		
		genfrag = 'GluGluSpin0ToGammaGamma_W_%s_M_%d_TuneCP2_13TeV_pythia8_cfi.py' %(width[i], m)	
		dataset = 'GluGluSpin0ToGammaGamma_W_%s_M_%d_TuneCP2_13TeV_pythia8' %(width[i], m)	

		#print genfrag 
		f = open("datasetHeavyHiggs.txt", "a")
		f.write('%s\n'%(dataset))
                fi = open("generatorFragmentListHeavyHiggs.txt", "a")
                fi.write('%s\n'%(genfrag))                                                    
	i = i+1


