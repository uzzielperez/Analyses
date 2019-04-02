import ROOT 
import time
import subprocess
import os
import argparse
from string import Template 

## Command Line Options
parser = argparse.ArgumentParser(description='Run Card Settings')
parser.add_argument('-t', '--template', help='Choose Run Card template.', type=str,
			default='PSWeightsTemplate.py')
parser.add_argument('-min', '--massminimum', default=500,
 		    help='minimum in mass bin')
parser.add_argument('-max', '--massmaximum', default=1000,
 		    help='maximum in mass bin')
parser.add_argument('-p', '--ptcut', type=float, default=70,
 		    help='ptcut')
parser.add_argument('-c', '--com', type=int, default=13000,
 		    help='Center of Mass Energy. At LHC (2018) currently at 13000 TeV')
parser.add_argument('--fall18', action="store_true")
parser.add_argument('--fall17', action="store_true")

args = parser.parse_args()

massMin         = args.massminimum
massMax         = args.massmaximum
pTcut           = args.ptcut
COM             = args.com/1000 # in TeV
#RunCardTemplate = args.template 

RunCard_outName = 'GG_M-%sTo%s_Pt%s_TuneCP2_13TeV-pythia8_cfi.py' %(massMin, massMax, pTcut)

# Dictionary
d={'massMin':massMin, 
   'massMax':massMax,
   'pTcut':pTcut}

if args.fall18:
	outputdir = 'GG2018'
	RunCardTemplate = 'PSWeightsTemplate.py'
if args.fall17:
	outputdir = 'GG2017'
	RunCardTemplate = 'TuneCP2Template.py'	

filein = open(RunCardTemplate)

if not os.path.exists(outputdir):
        os.mkdir(outputdir)	
os.chdir(outputdir)

outfile         = open(RunCard_outName, "w+")
src    = Template( filein.read())
sub    = src.substitute(d) 
outfile.write(sub)
filein.close()

print "Generated %s" %(RunCard_outName)

