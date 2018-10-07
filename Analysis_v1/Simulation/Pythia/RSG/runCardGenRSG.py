import ROOT 
import time
import subprocess
import os
import argparse
from string import Template 
import math 

## Command Line Options
parser = argparse.ArgumentParser(description='Run Card Settings')
parser.add_argument('-t', '--template', help='Choose Run Card template.', type=str,
			default='Template_CP5_13TeV_pythia8_cfi.py')
parser.add_argument('-k', '--coupling', type=float, default=0.2,
 		    help='coupling options: 0.01, 0.1, 0.2')
parser.add_argument('-m', '--mass', type=float, default=750,
 		    help='mass of first excited state of RSG')
parser.add_argument('-c', '--com', type=int, default=13000,
 		    help='Center of Mass Energy. At LHC (2018) currently at 13000 TeV')
args = parser.parse_args()

x_1 		= 3.83 #is the first zero of the J_1 Bessel function and
kMpl            = math.sqrt(2)*x_1*args.coupling
m0              = args.mass
COM             = args.com/1000 # in TeV
RunCardTemplate = args.template 
coupling  	= str(args.coupling)
coupling        = coupling.replace('.', '')  

#RSGravitonToGammaGamma_kMpl02_M_750_TuneCUEP8M1_13TeV_pythia8_cfi.py
RunCard_outName = 'RSGravitonToGammaGamma_kMpl%s_M_%d_TuneCP5_%dTeV_pythia8_cfi.py' %(coupling, m0, COM) 
filein = open(RunCardTemplate)

# Dictionary
d={'kMpl':kMpl,
   'm0':m0}

os.chdir('RSGfragments')
outfile         = open(RunCard_outName, "w+")
src    = Template(filein.read())
sub    = src.substitute(d) 
outfile.write(sub)
filein.close()
print "Generated %s" %(RunCard_outName)

