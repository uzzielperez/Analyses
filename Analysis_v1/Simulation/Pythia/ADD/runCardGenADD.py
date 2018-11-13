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
parser.add_argument('-l', '--LambdaT', type=float, default=4000,
 		    help='cutoff scale')
parser.add_argument('-min', '--massminimum', type=float, default=500.,
 		    help='minimum in mass bin')
parser.add_argument('-max', '--massmaximum', type=float , default=1000.,
 		    help='maximum in mass bin')
parser.add_argument('-p', '--ptcut', type=float, default=70.,
 		    help='ptcut')
parser.add_argument('-i', '--negint', type=int, default=1,
		    help='Positive Interference: 1 (contrary to documentation), and Negative Interference: 0')
parser.add_argument('-c', '--com', type=int, default=13000,
 		    help='Center of Mass Energy. At LHC (2018) currently at 13000 TeV')
args = parser.parse_args()

ned             = args.NED
lambdaT         = args.LambdaT
massMin         = args.massminimum
massMax         = args.massmaximum
pTcut           = args.ptcut
negInt          = args.negint
COM             = args.com/1000 # in TeV
RunCardTemplate = args.template 

RunCard_outName = 'ADDGravToGG_NegInt-%d_LambdaT-%d_M-%dTo%d_TuneCP5_%dTeV-pythia8_cfi.py' %(negInt, int(lambdaT), massMin, massMax, COM)
#RunCard_outName = 'ADDGravToGG_NegInt-%d_NED-%d_LambdaT-%d_M-%dTo%d_TuneCUEP8M1_%dTeV-pythia8_cfi.py' %(negInt, ned, int(lambdaT), massMin, massMax, COM)
filein = open(RunCardTemplate)

# Dictionary
d={'negInt': negInt,
   'ned':ned,
   'lambdaT':lambdaT,
   'massMin':massMin, 
   'massMax':massMax,
   'pTcut':pTcut}

os.chdir('ADDfragments')
outfile         = open(RunCard_outName, "w+")
src    = Template( filein.read())
sub    = src.substitute(d) 
outfile.write(sub)
filein.close()

print "Generated %s" %(RunCard_outName)

