import ROOT 
import time
import subprocess
import os
import argparse
from string import Template 

## Command Line Options
parser = argparse.ArgumentParser(description='Run Card Settings')
parser.add_argument('-t', '--template', help='Choose Run Card template.', type=str,
			default='TemplatePythia8ADDcfi.py')
parser.add_argument('-n', '--NED', type=int, default=4,
 		    help='Number of extra dimensions.')
parser.add_argument('-l', '--LambdaT', type=int, default=4000,
 		    help='cutoff scale')
parser.add_argument('-min', '--massminimum', type=float, default=500.,
 		    help='minimum in mass bin')
parser.add_argument('-max', '--massmaximum', type=float , default=1000.,
 		    help='maximum in mass bin')
parser.add_argument('-p', '--ptcut', type=float, default=70.,
 		    help='ptcut')
parser.add_argument('-c', '--com', type=int, default=13000,
 		    help='Center of Mass Energy. At LHC (2018) currently at 13000 TeV')
args = parser.parse_args()

ned             = args.NED
lambdaT         = args.LambdaT
massMin         = args.massminimum
massMax         = args.massmaximum
pTcut           = args.ptcut
COM             = args.com/1000 # in TeV
RunCardTemplate = args.template 

RunCard_outName = 'ADDGravToGG_NED-%d_LambdaT-%d_M-%dTo%d_Pt%d_%dTeV-pythia8.py' %(ned, lambdaT, massMin, massMax, pTcut, COM)
outfile         = open(RunCard_outName, "w+")

# Dictionary
d={'ned':ned,
   'lambdaT':lambdaT,
   'massMin':massMin, 
   'massMax':massMax,
   'pTcut':pTcut}

filein = open(RunCardTemplate)
src    = Template( filein.read())
sub    = src.substitute(d) 
outfile.write(sub)

print "Generated %s" %(RunCard_outName)
