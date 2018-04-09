import ROOT 
import time
import subprocess
import os
import argparse
from string import Template 

## Command Line Options
parser = argparse.ArgumentParser(description='Run Card Settings')
parser.add_argument('-t', '--template', help='Choose Run Card template.', type=str,
			default='TemplateRun.dat_signal')
parser.add_argument('-kk', '--kk_convention', type=int, default=1,
                    help='See documentation.')
parser.add_argument('-n', '--NED', type=int, default=4,
 		    help='Number of extra dimensions.')
parser.add_argument('-ms', '--M_S', type=int, default=4000,
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

#-----------
# Run Card Settings Overwrite 
kkconv = args.kk_convention
ned = args.NED
ms = args.M_S
massMin = args.massminimum
massMax = args.massmaximum
pTcut = args.ptcut
COM = args.com/1000 # in TeV
#------------
# Read from Template and Generate New Run Card
RunCardTemplate = args.template #TemplateRun.dat_signal 

# This is the naming convention we agreed upon
RunCard_out = 'Run.dat_ADDGravToGG_KK-%d_NED-%d_MS-%d_M-%dTo%d_%dTeV-sherpa' %(kkconv, ned, ms, massMin, massMax, COM)
#RunCard_out = 'Run.dat_ADDGravToGG_KK-%d_NED-%d_MS-%d_M-%dTo%d_Pt%d_%dTeV-sherpa' %(kkconv, ned, ms, massMin, massMax, pTcut, COM)
outfile = open(RunCard_out, "w+")

# Dictionary
d= {'kkconv':kkconv, 
    'ned':ned,
    'ms':ms,
    'massMin':massMin, 
    'massMax':massMax,
    'pTcut':pTcut}

filein = open(RunCardTemplate)
src = Template( filein.read())
sub = src.substitute(d) 
outfile.write(sub)

print "Generated %s" %(RunCard_out)
