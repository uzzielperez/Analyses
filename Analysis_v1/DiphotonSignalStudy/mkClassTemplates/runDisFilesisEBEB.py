import ROOT
import time
import subprocess
import os
import argparse
import re
from string import Template
import sys

# Command line options
parser = argparse.ArgumentParser(description="cmsDriver")
parser.add_argument("-a", "--action", default="None", help="del for Delete. run for Run.")
args = parser.parse_args()

action = args.action
# Timer
sw = ROOT.TStopwatch()
sw.Start()

DATASET = []

doADD         = False
doRSG         = True
doHeavyHiggs  = True
doUnparticles = False

numevent = 10000

#Templates
class_Ctemp = "ClassDiphotonSigX.C"
class_htemp = "ClassDiphotonSigX.h"
run_analyzetemp = "analyze.C"

if doADD:
    DATASET.append('/store/user/cuperez/DiPhotonAnalysis/signal-2018/ADDGravToGG_NegInt-0_LambdaT-10000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-10000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190207_171204/0000')
if doRSG:
    DATASET.append('/store/user/cuperez/DiPhotonAnalysis/signal-2018/RSGravitonToGammaGamma_kMpl001_M_750_TuneCP2_13TeV_pythia8/crab_RSGravitonToGammaGamma_kMpl001_M_750_TuneCP2_13TeV_pythia8__Fall17_PU2017-v1__MINIAODSIM/190207_171215/0000')
if doHeavyHiggs:
    DATASET.append('/store/user/cuperez/DiPhotonAnalysis/signal-2018/GluGluSpin0ToGammaGamma_W_0p014_M_750_TuneCP2_13TeV_pythia8/crab_GluGluSpin0ToGammaGamma_W_0p014_M_750_TuneCP2_13TeV_pythia8__Fall17_PU2017-v1__MINIAODSIM/190207_171226/0000')

for dset in DATASET:
    pattern = "store/user/cuperez/DiPhotonAnalysis/signal-2018/([^(]*)_TuneCP2_13TeV_pythia8/crab_"
    if doADD:
        pattern = "store/user/cuperez/DiPhotonAnalysis/signal-2018/([^(]*)_TuneCP2_13TeV-pythia8/crab_"
    match = re.findall(pattern, dset)
    print match
    nametag   = match[0].replace('-', '_')
    classname = "Class_%s" %(nametag)
    an_func   = "analyze_%s" %(nametag)
    outfile   = "%s" %(nametag)

    # Template Replacements
    cmssw_base = os.getenv("CMSSW_BASE")
    rep = {'ClassDiphotonSignal': classname,
           "outputfile": outfile,
           "cmssw_base": cmssw_base,
           "eosdsetdir": dset,
           "analyzefunc": an_func,
           }

    #Read and replace template file
    C_src = Template(open(class_Ctemp).read())
    C_sub = C_src.substitute(rep)

    h_src = Template(open(class_htemp).read())
    h_sub = h_src.substitute(rep)

    an_src = Template(open(run_analyzetemp).read())
    an_sub = an_src.substitute(rep)

    #write to file
    outfile_C = open("%s.C" %(classname), "w+")
    outfile_C.write(C_sub)

    outfile_h = open("%s.h" %(classname), "w+")
    outfile_h.write(h_sub)

    outfile_an = open("analyze_%s.C" %(nametag), "w+")
    outfile_an.write(an_sub)

def RunAnalyze(file_list):
	for anFile in file_list:
		if anFile.startswith("analyze_") and anFile.endswith(".C"):
			root_cmd = "root -l -q %s" %(anFile)
			os.system(root_cmd)
def DelClassFiles(file_list):
    for classFile in file_list:
        if "Class_" in classFile:
            del_cmd = "rm %s" %(classFile)
            os.system(del_cmd)
    print "deleted auxilliary files"

if action == "run":
    RunAnalyze(os.listdir('.'))
if action == "del":
    DelClassFiles(os.listdir('.'))

sw.Stop()
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time:  " + str(sw.CpuTime() / 60.0) + " minutes"
