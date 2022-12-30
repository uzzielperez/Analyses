import ROOT
import time
import subprocess
import os
import argparse
from string import Template
import math

## Command Line Options
parser = argparse.ArgumentParser(description='Run Card Settings')
parser.add_argument('-s', '--spin', help='Spin 0 or 2', type=str,
			default='2')
parser.add_argument('-d', '--du', type=float, default=1.5,
 		    help='typical du options: 1.06, 1.09, 2.1')
parser.add_argument('-l', '--LambdaU', type=int, default=3000,
 		    help='?')
parser.add_argument('-min', '--massMin', type=int, default=500,
 		    help='Min in mass bin')
parser.add_argument('-max', '--massMax', type=int , default=1000,
 		    help='maximum in mass bin')
parser.add_argument('-p', '--ptcut', type=int, default=70,
 		    help='ptcut')
parser.add_argument('-c', '--com', type=int, default=13000,
 		    help='Center of Mass Energy. At LHC (2018) currently at 13000 TeV')
args = parser.parse_args()

du 		        = args.du
LambdaU		    = args.LambdaU
spin 			= args.spin
massMin         = str(args.massMin)
massMax         = str(args.massMax)
pTcut           = str(args.ptcut)
RunCardTemplate = "UnparToGG_Spin%s_TuneCUEP8M1_temp.py" %(spin)

du_label        = str(du)
du_label        = du_label.replace('.', 'p')

lambdau_label  = str(LambdaU)
lambdau_label  = lambdau_label.replace('.', 'p')

d={'lambdaU': lambdau_label,
   'du':du_label,
   'massMin':massMin,
   'massMax':massMax,
   'pTcut':pTcut}

RunCard_outName = 'UnparToGG_Spin%s_du%s_LambdaU-%s_pT%s_M%s-%s_TuneCUEP8M1_13TeV_pythia8_cfi.py' %(spin, du_label, lambdau_label, pTcut, massMin, massMax)
if massMax == "-1":
	RunCard_outName = 'UnparToGG_Spin%s_du%s_LambdaU-%s_pT%s_M%s_TuneCUEP8M1_13TeV_pythia8_cfi.py' %(spin, du_label, lambdau_label, pTcut, massMin)

filein = open(RunCardTemplate)

if not os.path.exists('Unpar2016fragments'):
   os.makedirs('Unpar2016fragments')

os.chdir('Unpar2016fragments')
outfile         = open(RunCard_outName, "w+")
src    = Template(filein.read())
sub    = src.substitute(d)
outfile.write(sub)
filein.close()
print "Generated %s" %(RunCard_outName)
