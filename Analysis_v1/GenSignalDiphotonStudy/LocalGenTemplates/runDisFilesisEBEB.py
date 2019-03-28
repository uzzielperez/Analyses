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
#parser.add_argument("-a", "--action", default="None", help="del for Delete. run for Run.")
parser.add_argument("-d", "--delete", action="store_true", help="Clean directory and delete copied files")
parser.add_argument("-r", "--run", action="store_true", help="Run Analyze")
parser.add_argument("-c", "--cuts", default=None, help="Minv Cut")
#parser.add_argument("-r", "--run", action="store_true")
args = parser.parse_args()

#action = args.action
# Timer
sw = ROOT.TStopwatch()
sw.Start()

DATASET = []
numevents = 10000

doGGPythia2017  = False
doGGPythia2018  = True
doSM            = False
doSMPythia      = False
doADDTuneCUEP8M1 = False
#Templates
class_Ctemp = "ClassSMPythia.C"
class_htemp = "ClassSMPythia.h"
run_analyzetemp = "analyze.C"

xsecdict = {}

if doGGPythia2017:
    tag = "2017"
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/outlocal/GG_M-6000To8000_Pt50_TuneCP2_13TeV-pythia8_cfi_2017_py_GEN.root")
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/outlocal/GG_M-4000To6000_Pt50_TuneCP2_13TeV-pythia8_cfi_2017_py_GEN.root")
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/outlocal/GG_M-1000To2000_Pt50_TuneCP2_13TeV-pythia8_cfi_2017_py_GEN.root")
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/outlocal/GG_M-2000To4000_Pt50_TuneCP2_13TeV-pythia8_cfi_2017_py_GEN.root")
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/outlocal/GG_M-8000To13000_Pt50_TuneCP2_13TeV-pythia8_cfi_2017_py_GEN.root")
    xsecdict_temp = {
        "GG_M-6000To8000_Pt50_TuneCP2_13TeV-pythia8_cfi_2017"  :  3.367e-07+-1.497e-09,
        "GG_M-4000To6000_Pt50_TuneCP2_13TeV-pythia8_cfi_2017"  :  9.489e-06+-4.149e-08,
        "GG_M-1000To2000_Pt50_TuneCP2_13TeV-pythia8_cfi_2017"  :  1.577e-02+-7.006e-05,
        "GG_M-2000To4000_Pt50_TuneCP2_13TeV-pythia8_cfi_2017"  :  7.688e-04+-3.484e-06,
        "GG_M-8000To13000_Pt50_TuneCP2_13TeV-pythia8_cfi_2017" :  9.469e-09+-4.623e-11,
    }
    xsecdict.update(xsecdict_temp)

if doGGPythia2018:
    tag = "2018"
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/outlocal/GG_M-6000To8000_Pt50_TuneCP2_13TeV-pythia8_cfi_py_GEN.root")
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/outlocal/GG_M-4000To6000_Pt50_TuneCP2_13TeV-pythia8_cfi_py_GEN.root")
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/outlocal/GG_M-1000To2000_Pt50_TuneCP2_13TeV-pythia8_cfi_py_GEN.root")
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/outlocal/GG_M-2000To4000_Pt50_TuneCP2_13TeV-pythia8_cfi_py_GEN.root")
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/outlocal/GG_M-8000To13000_Pt50_TuneCP2_13TeV-pythia8_cfi_py_GEN.root")
    xsecdict_temp = {
        "GG_M-4000To6000_Pt50_TuneCP2_13TeV-pythia8_cfi_py" :  9.550e-06+-4.183e-08,
        "GG_M-1000To2000_Pt50_TuneCP2_13TeV-pythia8_cfi_py" :  1.558e-02+-6.959e-05,
        "GG_M-500To1000_Pt50_TuneCP2_13TeV-pythia8_cfi_py" :  1.604e-01+-6.792e-04,
        "GG_M-2000To4000_Pt50_TuneCP2_13TeV-pythia8_cfi_py" :  7.662e-04+-3.500e-06,
        "GG_M-6000To8000_Pt50_TuneCP2_13TeV-pythia8_cfi_py" :  3.360e-07+-1.498e-09,
        "GG_M-8000To13000_Pt50_TuneCP2_13TeV-pythia8_cfi_py" :  9.455e-09+-4.653e-11,
    }
    xsecdict.update(xsecdict_temp)


if doSMPythia:
    DATASET.append("TestSM_pT70_M-500-1000_py_GEN.root")
    DATASET.append("TestSM_pT70_M-1000-2000_py_GEN.root")
    DATASET.append("TestSM_pT70_M-2000-4000_py_GEN.root")
    DATASET.append("TestSM_pT70_M-4000_py_GEN.root")
    xsecdict_temp = {
        "SM_pT70_M-500-1000" :  1.346e-01+-5.733e-04,
        "SM_pT70_M-1000-2000" :  1.362e-02+-6.123e-05,
        "SM_pT70_M-2000-4000" :  6.747e-04+-3.089e-06,
        "SM_pT70_M-4000" :  8.623e-06+-4.134e-08,
    }
    xsecdict.update(xsecdict_temp)
if doADDTuneCUEP8M1:
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/Nout/ADDGravToGG_NegInt-1_LambdaT-6000_M-2000To4000_TuneCUEP8M1_13TeV-pythia8_cfi_py_GEN.root")
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/Nout/ADDGravToGG_NegInt-1_LambdaT-6000_M-500To1000_TuneCUEP8M1_13TeV-pythia8_cfi_py_GEN.root")
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/Nout/ADDGravToGG_NegInt-1_LambdaT-6000_M-4000To6000_TuneCUEP8M1_13TeV-pythia8_cfi_py_GEN.root")
    DATASET.append("/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/Nout/ADDGravToGG_NegInt-1_LambdaT-6000_M-1000To2000_TuneCUEP8M1_13TeV-pythia8_cfi_py_GEN.root")
    xsecdict_temp = {
        "ADDGravToGG_NegInt-1_LambdaT-6000_M-2000To4000_TuneCUEP8M1" :  1.011e-03+-5.126e-06,
        "ADDGravToGG_NegInt-1_LambdaT-6000_M-500To1000_TuneCUEP8M1" :  1.023e-01+-4.310e-04,
        "ADDGravToGG_NegInt-1_LambdaT-6000_M-4000To6000_TuneCUEP8M1" :  1.541e-04+-9.273e-07,
        "ADDGravToGG_NegInt-1_LambdaT-6000_M-1000To2000_TuneCUEP8M1" :  1.045e-02+-4.609e-05,
    }
    xsecdict.update(xsecdict_temp)

if doSM:
    # DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-60To200_Pt-50_13TeV-sherpa/crab_GGJets_M-60To200_Pt-50_13TeV-sherpa__Fall17_PU2017-v1__MINIAODSIM/190304_071350/0000")
    # DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-200To500_Pt-50_13TeV-sherpa/crab_GGJets_M-200To500_Pt-50_13TeV-sherpa__Fall17_PU2017-v1__MINIAODSIM/190304_071315/0000")
    DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-500To1000_Pt-50_13TeV-sherpa/crab_GGJets_M-500To1000_Pt-50_13TeV-sherpa__Fall17_PU2017-v1__MINIAODSIM/190304_071326/0000")
    DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/crab_GGJets_M-1000To2000_Pt-50_13TeV-sherpa__Fall17_PU2017-v1__MINIAODSIM/190304_071303/0000")
    DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-2000To4000_Pt-50_13TeV-sherpa/crab_GGJets_M-2000To4000_Pt-50_13TeV-sherpa__Fall17_PU2017-v2__MINIAODSIM/190304_071408/0000")
    DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-4000To6000_Pt-50_13TeV-sherpa/crab_GGJets_M-4000To6000_Pt-50_13TeV-sherpa__Fall17_PU2017-v2__MINIAODSIM/190304_071420/0000")
    DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-6000To8000_Pt-50_13TeV-sherpa/crab_GGJets_M-6000To8000_Pt-50_13TeV-sherpa__Fall17_PU2017-v1__MINIAODSIM/190304_071338/0000")


print "Creating files..."
for dset in DATASET:
    pattern = "/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/([^(]*)_13TeV-sherpa/crab"
    if doGGPythia2017:
            pattern = "/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/outlocal/([^(]*)_py_GEN.root"
    if doGGPythia2018:
            pattern = "/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/outlocal/([^(]*)_GEN.root"
    if doSMPythia:
        pattern = "Test([^(]*)_py_GEN.root"
    if doSMPythia:
        pattern = "Test([^(]*)_py_GEN.root"
    if doADDTuneCUEP8M1:
	    pattern = "/uscms_data/d3/cuperez/DiphotonEXO/CMSSW_10_2_1/src/Nout/([^(]*)_13TeV-pythia8_cfi_py_GEN.root"
    match = re.findall(pattern, dset)
    #print match
    nametag   = match[0].replace('-', '_')
    xsecval = xsecdict[match[0]]
    #print match[0], xsecval

    if args.cuts is not None:
        nametag = nametag + "mgg_"+str(MinvCut)
        if setMmax:
            nametag = nametag + "_%s" %(Mmax)

    print nametag
    classname = "Class_%s" %(nametag)
    an_func   = "analyze_%s" %(nametag)
    outfile   = "%s" %(nametag)

    # Template Replacements
    cmssw_base = os.getenv("CMSSW_BASE")
    rep = {'ClassDiphoton': classname,
           "outputfile": outfile,
           "xsecvalue": xsecval,
           "cmssw_base": cmssw_base,
           "eosdsetdir": dset,
           "analyzefunc": an_func,
           "numevents": numevents,
           }

    if args.cuts is not None:
        rep['MinvCut'] = MinvCut
        if setMmax:
            rep['Mmax'] = Mmax

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
        if "analyze_" in classFile:
            del_cmd = "rm %s" %(classFile)
            os.system(del_cmd)
    print "deleted auxilliary files"

if args.run:
    RunAnalyze(os.listdir('.'))
if args.delete:
    DelClassFiles(os.listdir('.'))

sw.Stop()
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time:  " + str(sw.CpuTime() / 60.0) + " minutes"
