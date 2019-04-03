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

# Timer
sw = ROOT.TStopwatch()
sw.Start()

DATASET = []

doGGJets        = False
doADDTuneCP2    = True

#Templates
class_Ctemp = "ClassDiphotonSigX.C"
class_htemp = "ClassDiphotonSigX.h"
run_analyzetemp = "analyze.C"
if doGGJets:
    DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/crab_GGJets_M-1000To2000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/190329_004413/0000')
    DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/GGJets_M-2000To4000_Pt-50_13TeV-sherpa/crab_GGJets_M-2000To4000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/190329_004425/0000')
    DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/GGJets_M-200To500_Pt-50_13TeV-sherpa/crab_GGJets_M-200To500_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/190329_004345/0000')
    DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/GGJets_M-4000To6000_Pt-50_13TeV-sherpa/crab_GGJets_M-4000To6000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/190329_004439/0000')
    DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/GGJets_M-500To1000_Pt-50_13TeV-sherpa/crab_GGJets_M-500To1000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/190329_004359/0000')
    DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/GGJets_M-6000To8000_Pt-50_13TeV-sherpa/crab_GGJets_M-6000To8000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/190329_004451/0000')
    DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/GGJets_M-60To200_Pt-50_13TeV-sherpa/crab_GGJets_M-60To200_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/190329_004331/0000')
    DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/GGJets_M-8000To13000_Pt-50_13TeV-sherpa/crab_GGJets_M-8000To13000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/190329_004503/0000')
if doADDTuneCP2:
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-10000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-10000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055518/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-10000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-10000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055530/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-10000_M-4000To10000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-10000_M-4000To10000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055543/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-10000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-10000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055555/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-11000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-11000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055607/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-11000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-11000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055617/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-11000_M-4000To11000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-11000_M-4000To11000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055629/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-11000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-11000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055639/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-13000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-13000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055650/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-13000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-13000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055700/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-13000_M-4000To13000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-13000_M-4000To13000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055711/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-13000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-13000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055723/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-4000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-4000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055734/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-4000_M-2000To3000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-4000_M-2000To3000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055745/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-4000_M-3000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-4000_M-3000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055756/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-4000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-4000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055806/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-4500_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-4500_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055817/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-4500_M-2000To3000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-4500_M-2000To3000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055830/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-4500_M-3000To4500_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-4500_M-3000To4500_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055841/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-4500_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-4500_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055852/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-5000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-5000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055903/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-5000_M-2000To3000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-5000_M-2000To3000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055914/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-5000_M-3000To5000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-5000_M-3000To5000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055925/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-5000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-5000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055937/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-5500_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-5500_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055947/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-5500_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-5500_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055957/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-5500_M-4000To5500_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-5500_M-4000To5500_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060007/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-5500_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-5500_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060018/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-6000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-6000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060028/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-6000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-6000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060039/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-6000_M-4000To6000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-6000_M-4000To6000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060050/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-6000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-6000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060101/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-6500_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-6500_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060111/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-6500_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-6500_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060123/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-6500_M-4000To6500_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-6500_M-4000To6500_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060133/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-6500_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-6500_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060145/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-7000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-7000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060155/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-7000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-7000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060205/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-7000_M-4000To7000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-7000_M-4000To7000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060216/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-7000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-7000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060226/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-7500_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-7500_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060236/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-7500_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-7500_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060248/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-7500_M-4000To7500_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-7500_M-4000To7500_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060259/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-7500_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-7500_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060310/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-8000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-8000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060321/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-8000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-8000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060331/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-8000_M-4000To8000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-8000_M-4000To8000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060342/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-8000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-8000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060358/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-9000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-9000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060408/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-9000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-9000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060419/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-9000_M-4000To9000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-9000_M-4000To9000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060429/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-9000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-9000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060439/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-10000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-10000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060450/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-10000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-10000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060501/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-10000_M-4000To10000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-10000_M-4000To10000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060513/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-10000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-10000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060523/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-11000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-11000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060534/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-11000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-11000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060545/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-11000_M-4000To11000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-11000_M-4000To11000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060556/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-11000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-11000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060608/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-13000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-13000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060628/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-13000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-13000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190401_030907/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-13000_M-4000To13000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-13000_M-4000To13000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060735/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-13000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-13000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060745/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-4000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-4000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060755/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-4000_M-2000To3000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-4000_M-2000To3000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060806/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-4000_M-3000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-4000_M-3000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060818/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-4000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-4000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060829/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-4500_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-4500_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060841/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-4500_M-2000To3000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-4500_M-2000To3000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060852/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-4500_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-4500_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060903/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-5000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-5000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060913/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-5000_M-2000To3000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-5000_M-2000To3000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060923/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-5000_M-3000To5000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-5000_M-3000To5000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060933/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-5000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-5000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060946/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-5500_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-5500_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_060957/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-5500_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-5500_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061008/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-5500_M-4000To5500_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-5500_M-4000To5500_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061019/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-5500_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-5500_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061029/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-6000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-6000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061040/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-6000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-6000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061052/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-6000_M-4000To6000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-6000_M-4000To6000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061103/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-6000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-6000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061114/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-6500_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-6500_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061124/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-6500_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-6500_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061134/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-6500_M-4000To6500_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-6500_M-4000To6500_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061145/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-6500_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-6500_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061157/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-7000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-7000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190401_025725/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-7000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-7000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061207/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-7000_M-4000To7000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-7000_M-4000To7000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061218/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-7000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-7000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061230/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-7500_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-7500_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061245/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-7500_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-7500_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061255/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-7500_M-4000To7500_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-7500_M-4000To7500_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061309/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-7500_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-7500_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190401_025758/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-8000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-8000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061319/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-8000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-8000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061329/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-8000_M-4000To8000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-8000_M-4000To8000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061340/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-8000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-8000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061350/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-8500_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-8500_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061401/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-8500_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-8500_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061413/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-8500_M-4000To8500_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-8500_M-4000To8500_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061424/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-8500_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-8500_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061434/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-9000_M-1000To2000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-9000_M-1000To2000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061444/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-9000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-9000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061455/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-9000_M-4000To9000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-9000_M-4000To9000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061505/0000')
   DATASET.append('/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-1_LambdaT-9000_M-500To1000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-1_LambdaT-9000_M-500To1000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_061518/0000')


print "Creating files..."
for dset in DATASET:
    if doGGJets:
        pattern = "store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/([^(]*)_Pt-50_13TeV-sherpa/crab_"
    if doADDTuneCP2:
        pattern = "store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/([^(]*)_TuneCP2_13TeV-pythia8/crab_"
    match = re.findall(pattern, dset)
    #print match
    nametag   = match[0].replace('-', '_')

    setMmax = False
    #if doSherpaADDang:
        #pttn =  "ADDGravToGG_MS-([^(]*)_NED"
        #newmatch = re.findall(pttn, match[0])
        #Mmax = newmatch[0]
        #setMmax = True

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
    rep = {'ClassDiphotonSignal': classname,
           "outputfile": outfile,
           "cmssw_base": cmssw_base,
           "eosdsetdir": dset,
           "analyzefunc": an_func,
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
