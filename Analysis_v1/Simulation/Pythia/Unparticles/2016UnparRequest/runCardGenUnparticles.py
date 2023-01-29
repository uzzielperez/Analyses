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
			default='TemplateUnparticlesTuneCUEP8M1.py')
parser.add_argument('-d', '--du', type=float, default=2.1,
 		    help='typical du options: 1.06, 1.09, 2.1')
parser.add_argument('-l', '--LambdaU', type=float, default=15000,
 		    help='?')
parser.add_argument('-c', '--com', type=int, default=13000,
 		    help='Center of Mass Energy. At LHC (2018) currently at 13000 TeV')
args = parser.parse_args()

du 		= args.du
LambdaU		= args.LambdaU
RunCardTemplate = args.template


du_label        = str(du)
du_label        = du_label.replace('.', 'p')

lambdau_label  = str(LambdaU)
lambdau_label  = lambdau_label.replace('.', 'p')

RunCard_outName = 'Unparticles_du%s_LambdaU-%s_TuneCUEP8M1_13TeV_pythia8.py' %(du_label, lambdau_label) 
RunCard_outName = 'UnparToGG_Spin2_du1p9_LambdaU-3500_pT70_M2000-3000_TuneCP2_13TeV_pythia8_cfi.py' %(du_label, lambdau_label)  
filein = open(RunCardTemplate)

# Dictionary
d={'LambdaU':LambdaU,
   'du':du}

os.chdir('Unparticlesfragments')
outfile         = open(RunCard_outName, "w+")
src    = Template(filein.read())
sub    = src.substitute(d) 
outfile.write(sub)
filein.close()
print "Generated %s" %(RunCard_outName)

