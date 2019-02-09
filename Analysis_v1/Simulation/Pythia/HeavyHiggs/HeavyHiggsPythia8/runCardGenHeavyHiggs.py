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
			default='TemplateHeavyHiggs_TuneCP5_13TeV_pythia8_cfi.py')
parser.add_argument('-w', '--width', type=str, default='5p6',
 		    help='width options: 0p014, 1p4, 5p6')
parser.add_argument('-m', '--mass', type=float, default=750,
 		    help='mass of first excited state of RSG')
parser.add_argument('-c', '--com', type=int, default=13000,
 		    help='Center of Mass Energy. At LHC (2018) currently at 13000 TeV')
args = parser.parse_args()

width 		= args.width
mWidth={'0p014': 1.4*(10**(-4)), '1p4': 1.4*(10**(-2)) , '5p6': 5.6*(10**(-2))} 
m0              = args.mass
COM             = args.com/1000 # in TeV
RunCardTemplate = args.template 
#coupling  	= str(args.coupling)
#coupling        = coupling.replace('.', '')  
gamma_x 	= mWidth[width]*m0

#GluGluSpin0ToGammaGamma_W_5p6_M_750_TuneCP5_13TeV_pythia8_cfi.py 
RunCard_outName = 'GluGluSpin0ToGammaGamma_W_%s_M_%d_TuneCP5_%dTeV_pythia8_cfi.py' %(width, m0, COM) 

filein = open(RunCardTemplate)

# Dictionary
d={'mWidth': gamma_x
   ,'m0':m0}
os.chdir('HeavyHiggsfragments')
outfile  = open(RunCard_outName, "w+")
src    = Template(filein.read())
sub    = src.substitute(d) 
outfile.write(sub)
filein.close()


print "Generated %s, Gamma/m: %f"  %(RunCard_outName, gamma_x/m0)

