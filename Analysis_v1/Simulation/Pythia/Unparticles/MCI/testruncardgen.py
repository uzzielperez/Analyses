import ROOT 
import time
import subprocess
import os
import argparse
from string import Template 
import math 

## Command Line Options
parser = argparse.ArgumentParser(description='Run Card Settings')
parser.add_argument('-s', '--spin', help='Spin0 or 2 determines template.', type=str)
parser.add_argument('-d', '--du', type=float, default=2.1,
 		    help='typical du options: 1.06, 1.09, 2.1')
parser.add_argument('-l', '--LambdaU', type=float, default=15000,
 		    help='?')
parser.add_argument('-r', '--rangeMass', default="500-2000",
 		    help='Please put dash between min and max. If max is less than min there is no upper limit.')
parser.add_argument('-c', '--com', type=int, default=13000,
 		    help='Center of Mass Energy. At LHC (2018) currently at 13000 TeV')
args = parser.parse_args()

du 		= args.du
LambdaU		= args.LambdaU
spin	        = args.spin

minMass, maxMass = args.rangeMass.split("-")
# Dictionary
d={'LambdaU':LambdaU,
   'du':du,
   'minMass': minMass,
   'maxMass': maxMass}

massrange = args.rangeMass
if float(minMass) > float(maxMass):
	massrange = minMass

if spin == "2":
	RunCardTemplate = "TemplateSpin2.py"
if spin == "0":
	RunCardTemplate = "TemplateSpin0.py"

du_label        = str(du)
du_label        = du_label.replace('.', 'p')

lambdau_label  = str(LambdaU)
lambdau_label  = lambdau_label.replace('.', 'p')

RunCard_outName = 'FinMCIUnp_LU%s_du%s_spin-%s_M_%s.py' %(lambdau_label, du_label, spin, massrange) 
filein = open(RunCardTemplate)

os.chdir('testfrag')
outfile = open(RunCard_outName, "w+")
src    = Template(filein.read())
sub    = src.substitute(d) 
outfile.write(sub)
filein.close()
print "Generated %s" %(RunCard_outName), "from %s" %(RunCardTemplate)

