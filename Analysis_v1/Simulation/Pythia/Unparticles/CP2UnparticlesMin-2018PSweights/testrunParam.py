import sys
import os 
import subprocess as sp 
import math
import argparse

## Command Line Options
parser = argparse.ArgumentParser(description='Run Card Settings')
parser.add_argument('-s', '--spin', help='Spin0 or 2 determines template.', type=str,
                    default="2")
args = parser.parse_args()

spin = args.spin
du = [1.1, 1.5, 1.9]

if spin == "2":
	du_LambdaU_dict = {1.1: [2000, 3000, 3500],
			   1.5: [2000, 2500, 3000],
			   1.9: [2000, 2500, 3500]}
if spin == "0":
	du_LambdaU_dict = {1.1: [4000, 8000, 9500],
			   1.5: [2000, 2500, 3500],
			   1.9: [2000, 2500, 3500]}


massrange = ["500-2000", "2000-1"]

print "Writiting generator fragments... "
idu = 0 
while idu < len(du):
	print du[idu], du_LambdaU_dict[du[idu]]
	LambdaU = du_LambdaU_dict[du[idu]]
	for ilambdau in LambdaU:
		for mrange in massrange:
			#print "du: ", du[idu], "; LambdaU: ", ilambdau	
			cmd = 'python testruncardgen.py -s %s -d %f -l %f -r %s' %(spin, du[idu], ilambdau, mrange)
			print cmd
			os.system(cmd)

			du_label        = str(du[idu])
			du_label        = du_label.replace('.', 'p')	
			ilambdau_label  = str(ilambdau)

	idu = idu+1


