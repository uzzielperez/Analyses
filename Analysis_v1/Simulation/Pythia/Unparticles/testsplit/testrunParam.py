import sys
import os 
import subprocess as sp 
import math

#du = [1.06, 1.09, 2.1]
#LambdaU = [0.4, 1, 4, 15000, 100000]

#du = [1.4, 2.0]
#LambdaU = [10, 1]

#du = [1.06, 1.04, 1.02, 1.0, 0.5, 0.2]
#LambdaU = [10, 1]

#du = [1.01, 1.10, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
#LambdaU = [800, 1000, 2000]
#LambdaU = [1000, 1250, 1500, 1750, 2000]
#du = [1.8]
#LambdaU = [2000, 2250, 2500, 2750]
#LambdaU = [3000, 3250, 3500, 3750, 4000, 4250, 4500]
#LambdaU = [4750, 5000, 5250, 5500, 5750, 6000]
#LambdaU = [1000, 1250, 1500, 1750, 2250, 2750]

#du = [1.01, 1.1,  1.2, 1.3, 1.4]
#LambdaU = [1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 6000]

#du = [1.5, 1.6, 1.7, 1.9]
LambdaU = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5500]
 
massrange = ["500-2000", "2000-1"]

print "Writiting generator fragments... "
idu = 0 
while idu < len(du):
	for ilambdau in LambdaU:
		for mrange in massrange:
			#print "du: ", du[idu], "; LambdaU: ", ilambdau
			command = 'python testruncardgen.py -d %f -l %f -r %s' %(du[idu], ilambdau, mrange)		
			print command
			os.system(command) 

			du_label        = str(du[idu])
			du_label        = du_label.replace('.', 'p')
		
			ilambdau_label  = str(ilambdau)
			#ilambdau_label 	= ilambdau_label.replace('.', 'p')

			genfrag = 'Unparticles_du%s_LambdaU-%s_TuneCUEP8M1_13TeV_pythia8_cfi.py' %(du_label, ilambdau_label)	
		
			print genfrag 
	idu = idu+1


