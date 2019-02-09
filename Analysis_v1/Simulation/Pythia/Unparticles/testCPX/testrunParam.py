import sys
import os
import subprocess as sp
import math

du =[1.01,1.5,1.8]
LambdaU = [1500, 2000, 2500, 3000, 3500, 4000]
massrange = ["500-2000", "2000-1"]
spin = ["0", "2"]
print "Writiting generator fragments... "
idu = 0
while idu < len(du):
	for ilambdau in LambdaU:
		for mrange in massrange:
			#print "du: ", du[idu], "; LambdaU: ", ilambdau
			command = 'python testruncardgen.py -d %f -l %f -r %s -s %s' %(du[idu], ilambdau, mrange, spin[0])
			cmd = 'python testruncardgen.py -d %f -l %f -r %s -s %s' %(du[idu], ilambdau, mrange, spin[1])
			#print command, cmd
			os.system(command)
			os.system(cmd)

			du_label        = str(du[idu])
			du_label        = du_label.replace('.', 'p')

			ilambdau_label  = str(ilambdau)
			#ilambdau_label 	= ilambdau_label.replace('.', 'p')

			#genfrag = 'Unparticles_du%s_LambdaU-%s_TuneCUEP8M1_13TeV_pythia8_cfi.py' %(du_label, ilambdau_label)

			#print genfrag
	idu = idu+1
