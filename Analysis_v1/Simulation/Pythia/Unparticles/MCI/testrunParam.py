import sys
import os 
import subprocess as sp 
import math


du = [1.1, 1.5, 1.6, 1.8]
LambdaU = [1000, 2000, 3000, 4000, 4500, 5000]
massrange = ["500-2000", "2000-1"]
#spin = ["0", "2"]

print "Writiting generator fragments... "
idu = 0 
while idu < len(du):
	for ilambdau in LambdaU:
		for mrange in massrange:
			#print "du: ", du[idu], "; LambdaU: ", ilambdau
			
			cmd0 = 'python testruncardgen.py -s %s -d %f -l %f -r %s' %("0", du[idu], ilambdau, mrange)
			cmd2 = 'python testruncardgen.py -s %s -d %f -l %f -r %s' %("2", du[idu], ilambdau, mrange)		
			print cmd0," ", cmd2
			os.system(cmd0)
			os.system(cmd2) 

			du_label        = str(du[idu])
			du_label        = du_label.replace('.', 'p')	
			ilambdau_label  = str(ilambdau)

	idu = idu+1


