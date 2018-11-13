import sys
import os 
import subprocess as sp 
import math


k = [0.01, 0.1, 0.2]
M = [[750,1000,1250,1500,1750,2000, 2250, 2500, 2750, 3000, 3250,3500,4000,5000],
     [750,1000,1250,1500,1750,2000,2250, 2500,3000,3500,4000,4250,4500,4750,5000,5250,5500,5750,6000, 6500, 7000, 8000],
     [750,1000,1250,1500,1750,2000,2250,2500,3000,3500,4000,4500,4750,5000,5250,5500,5750,6000, 6500, 7000, 8000]]
       
print "Writiting generator fragments... "
i = 0 
while i < len(k):
	for m in M[i]:
		#print "coupling: ", k[i], "; m0: ", m
		command = 'python runCardGenRSG.py -k %f -m %d' %(k[i], m)		
		#print command 
		process = sp.Popen(command.split(), stdout=sp.PIPE)
		output, error = process.communicate()

		coupling        = str(k[i])
		coupling        = coupling.replace('.', '')
		dataset = 'RSGravitonToGammaGamma_kMpl%s_M_%s_TuneCP2_13TeV_pythia8' %(coupling, m)
		genfrag = 'RSGravitonToGammaGamma_kMpl%s_M_%s_TuneCP2_13TeV_pythia8_cfi.py' %(coupling, m)	
		
		print genfrag 
		f = open("datasetRSG.txt", "a")
		f.write('%s\n'%(dataset))
                fi = open("generatorFragmentListRSG.txt", "a")
                fi.write('%s\n'%(genfrag))                                                    
	i = i+1


