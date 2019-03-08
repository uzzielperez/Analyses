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

doSM          = True
doADD         = False
doUnparticles = False

def chaindis():
    if args.cuts is not None:
        MinvCut     =  args.cuts # Basic cut is 500 GeV
        print "Applying invariant mass cut > %s" %(MinvCut)
    if doSM:
        # DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-60To200_Pt-50_13TeV-sherpa/crab_GGJets_M-60To200_Pt-50_13TeV-sherpa__Fall17_PU2017-v1__MINIAODSIM/190304_071350/0000")
        # DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-200To500_Pt-50_13TeV-sherpa/crab_GGJets_M-200To500_Pt-50_13TeV-sherpa__Fall17_PU2017-v1__MINIAODSIM/190304_071315/0000")
        DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-500To1000_Pt-50_13TeV-sherpa/crab_GGJets_M-500To1000_Pt-50_13TeV-sherpa__Fall17_PU2017-v1__MINIAODSIM/190304_071326/0000")
        DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/crab_GGJets_M-1000To2000_Pt-50_13TeV-sherpa__Fall17_PU2017-v1__MINIAODSIM/190304_071303/0000")
        DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-2000To4000_Pt-50_13TeV-sherpa/crab_GGJets_M-2000To4000_Pt-50_13TeV-sherpa__Fall17_PU2017-v2__MINIAODSIM/190304_071408/0000")
        DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-4000To6000_Pt-50_13TeV-sherpa/crab_GGJets_M-4000To6000_Pt-50_13TeV-sherpa__Fall17_PU2017-v2__MINIAODSIM/190304_071420/0000")
        DATASET.append("/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/GGJets_M-6000To8000_Pt-50_13TeV-sherpa/crab_GGJets_M-6000To8000_Pt-50_13TeV-sherpa__Fall17_PU2017-v1__MINIAODSIM/190304_071338/0000")

        # DATASET.append("/store/user/cawest/GGJets_M-60To200_Pt-50_13TeV-sherpa/crab_GGJets_M-60To200_Pt-50_13TeV-sherpa__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14/180531_184256/0000")
        # DATASET.append("/store/user/cawest/GGJets_M-200To500_Pt-50_13TeV-sherpa/crab_GGJets_M-200To500_Pt-50_13TeV-sherpa__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1/180531_184217/0000")
        # DATASET.append("/store/user/cawest/GGJets_M-500To1000_Pt-50_13TeV-sherpa/crab_GGJets_M-500To1000_Pt-50_13TeV-sherpa__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v/180531_184235/0000")
        # DATASET.append("/store/user/cawest/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/crab_GGJets_M-1000To2000_Pt-50_13TeV-sherpa__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_/180531_184157/0000")
        # DATASET.append("/store/user/cawest/GGJets_M-2000To4000_Pt-50_13TeV-sherpa/crab_GGJets_M-2000To4000_Pt-50_13TeV-sherpa__Fall17_PU2017-v2__MINIAODSIM/190131_195335/0000")
        # DATASET.append("/store/user/cawest/GGJets_M-4000To6000_Pt-50_13TeV-sherpa/crab_GGJets_M-4000To6000_Pt-50_13TeV-sherpa__Fall17_PU2017-v2__MINIAODSIM/180925_195312/0000")
        # DATASET.append("/store/user/cawest/GGJets_M-6000To8000_Pt-50_13TeV-sherpa/crab_GGJets_M-6000To8000_Pt-50_13TeV-sherpa__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_/180531_182940/0000")
        # DATASET.append("/store/user/cawest/GGJets_M-8000To13000_Pt-50_13TeV-sherpa/crab_GGJets_M-8000To13000_Pt-50_13TeV-sherpa__Fall17_PU2017-v1__MINIAODSIM/190131_195356/0000")
    if doADD:
        #DATASET.append('/store/user/cuperez/DiPhotonAnalysis/signal-2018/ADDGravToGG_NegInt-0_LambdaT-10000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-10000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190207_171204/0000')
        DATASET.append('/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/ADDGravToGG_NegInt-1_LambdaT-13000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-13000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190304_071943/0000')
        DATASET.append('/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/ADDGravToGG_NegInt-1_LambdaT-13000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-13000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190304_071907/0000')
        DATASET.append('/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/ADDGravToGG_NegInt-1_LambdaT-13000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-13000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190304_071921/0000')
        DATASET.append('/store/user/cuperez/DiPhotonAnalysis/ExoANDiphoton/ADDGravToGG_NegInt-1_LambdaT-13000_M-4000To13000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-13000_M-4000To13000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190304_071932/0000')

    return DATASET
sw.Stop()
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time:  " + str(sw.CpuTime() / 60.0) + " minutes"
