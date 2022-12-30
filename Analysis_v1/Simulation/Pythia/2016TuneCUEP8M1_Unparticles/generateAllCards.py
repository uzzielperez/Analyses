import ROOT
import time
import subprocess
import os
import argparse
from string import Template
import math
import sys

parser = argparse.ArgumentParser(description='Run Card Settings')
parser.add_argument('-s', '--spin', help='Spin 0 or 2', type=str,
			default='2')
# parser.add_argument('-d', '--du', type=float, default=1.5,
#  		    help='typical du options: 1.1, 1.5, 1.9')
# parser.add_argument('-l', '--LambdaU', type=int, default=3000,
#  		    help='?')
parser.add_argument('-min', '--massMin', type=int, default=500,
 		    help='Min in mass bin')
parser.add_argument('-max', '--massMax', type=int , default=1000,
 		    help='maximum in mass bin')
parser.add_argument('-p', '--ptcut', type=int, default=70,
 		    help='ptcut')
parser.add_argument('-c', '--com', type=int, default=13000,
 		    help='Center of Mass Energy. At LHC (2018) currently at 13000 TeV')
args = parser.parse_args()

# du 		        = args.du
# lambdaU		    = args.LambdaU
spin 			= args.spin
massMin         = args.massMin
massMax         = args.massMax
pTcut           = args.ptcut

dus = [1.1, 1.5, 1.9]

if spin == "0":
	du_lambdaU_map = { 1.1 : {4000, 8000, 10000},
	                   1.5 : {2000, 2500, 3500},
	                   1.9 : {2000, 2500, 3500}}



if spin == "2":
	du_lambdaU_map = { 1.1 : {2000, 2500, 3000},
					   1.5 : {2000, 2500, 3000},
					   1.9 : {2000, 2500, 3500}}

massRanges = { 4000 : [500, 1000, 2000, 4000, -1],
			   8000 : [500, 1000, 2000, 4000, -1],
			   10000 : [500, 1000, 2000, 4000, -1],
			   2000 : [500, 1000, 2000, -1],
			   2500 : [500, 1000, 2000, -1],
			   3000 : [500, 1000, 2000, 3000, -1],
			   3500 : [500, 1000, 2000, 3000, -1]}

for du in dus:
	# print du

	for lambdaU in du_lambdaU_map[du]:
		i = 0
		# print lambdaU
		while i < ( len(massRanges[lambdaU])-1 ) :
			massMin = massRanges[lambdaU][i]
			massMax = massRanges[lambdaU][i+1]
			# print massMin, massMax

			command = 'python runCardGenUnparticles.py -s %s -d %f -l %d -min %d -max %d -p %s' %(spin, du, lambdaU, massMin, massMax, pTcut)
			os.system(command)

			i = i + 1
