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
parser.add_argument("-a", "--action", default="del", help="del for Delete. run for Run.")
args = parser.parse_args()

action = args.action
# Timer
sw = ROOT.TStopwatch()
sw.Start()

DATASET = []

doMCspin2_du1p5 = True
doMCspin2_du1p9 = True
doMCspin2_du1p1 = True

doMC_SM = False
doMCspin0_du1p5 = False
doMCspin0_du1p9 = False
doMCspin0_du1p1 = False

numevents = 10000

#Templates
class_Ctemp = "ClassTemplateisEBEB.C"
class_htemp = "ClassTemplateisEBEB.h"
run_analyzetemp = "analyzeTemplate.C"

xsecdict = {}
if doMC_SM:
    du_tag = ""
    DATASET.append("TestSM_pT70_M-500-1000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSM_pT70_M-1000-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSM_pT70_M-2000-4000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSM_pT70_M-4000_py_GEN.root/demo/fgenTree")
    xsecdict_temp = {
        "SM_pT70_M-500-1000_py" :  1.346e-01+-5.733e-04,
        "SM_pT70_M-1000-2000_py" :  1.362e-02+-6.123e-05,
        "SM_pT70_M-2000-4000_py" :  6.747e-04+-3.089e-06,
        "SM_pT70_M-4000_py" :  8.623e-06+-4.134e-08,
    }
    xsecdict.update(xsecdict_temp)
# Spin 2
if doMCspin2_du1p5:
    du_tag = ""
    DATASET.append("TestUnparToGG_Spin2_du1p5_LambdaU-3000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p5_LambdaU-2500_pT70_M2500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p5_LambdaU-2000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p5_LambdaU-3000_pT70_M3000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p5_LambdaU-2500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p5_LambdaU-3000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p5_LambdaU-2500_pT70_M1000-2500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p5_LambdaU-3000_pT70_M2000-3000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p5_LambdaU-2000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p5_LambdaU-2000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    xsecdict_temp = {
        "UnparToGG_Spin2_du1p5_LambdaU-3000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.361e-02+-6.051e-05,
        "UnparToGG_Spin2_du1p5_LambdaU-2500_pT70_M2500_TuneCP2_13TeV_pythia8_cfi_py" :  2.325e-04+-1.096e-06,
        "UnparToGG_Spin2_du1p5_LambdaU-2000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.344e-01+-5.775e-04,
        "UnparToGG_Spin2_du1p5_LambdaU-3000_pT70_M3000_TuneCP2_13TeV_pythia8_cfi_py" :  7.253e-05+-3.431e-07,
        "UnparToGG_Spin2_du1p5_LambdaU-2500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.338e-01+-5.724e-04,
        "UnparToGG_Spin2_du1p5_LambdaU-3000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.335e-01+-5.727e-04,
        "UnparToGG_Spin2_du1p5_LambdaU-2500_pT70_M1000-2500_TuneCP2_13TeV_pythia8_cfi_py" :  1.401e-02+-6.480e-05,
        "UnparToGG_Spin2_du1p5_LambdaU-3000_pT70_M2000-3000_TuneCP2_13TeV_pythia8_cfi_py" :  6.314e-04+-2.741e-06,
        "UnparToGG_Spin2_du1p5_LambdaU-2000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py" :  8.735e-04+-4.211e-06,
        "UnparToGG_Spin2_du1p5_LambdaU-2000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.376e-02+-6.126e-05,
    }
    xsecdict.update(xsecdict_temp)
if doMCspin2_du1p9:
    du_tag = ""
    DATASET.append("TestUnparToGG_Spin2_du1p9_LambdaU-2500_pT70_M1000-2500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p9_LambdaU-2000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p9_LambdaU-3500_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p9_LambdaU-2500_pT70_M2500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p9_LambdaU-2500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p9_LambdaU-3500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p9_LambdaU-3500_pT70_M3500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p9_LambdaU-3500_pT70_M2000-3500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p9_LambdaU-2000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p9_LambdaU-2000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    xsecdict_temp = {
       "UnparToGG_Spin2_du1p9_LambdaU-2500_pT70_M1000-2500_TuneCP2_13TeV_pythia8_cfi_py" :  1.433e-02+-6.599e-05,
       "UnparToGG_Spin2_du1p9_LambdaU-2000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.046e-03+-4.935e-06,
       "UnparToGG_Spin2_du1p9_LambdaU-3500_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.368e-02+-6.123e-05,
       "UnparToGG_Spin2_du1p9_LambdaU-2500_pT70_M2500_TuneCP2_13TeV_pythia8_cfi_py" :  2.712e-04+-1.284e-06,
       "UnparToGG_Spin2_du1p9_LambdaU-2500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.355e-01+-5.772e-04,
       "UnparToGG_Spin2_du1p9_LambdaU-3500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.335e-01+-5.736e-04,
       "UnparToGG_Spin2_du1p9_LambdaU-3500_pT70_M3500_TuneCP2_13TeV_pythia8_cfi_py" :  2.776e-05+-1.321e-07,
       "UnparToGG_Spin2_du1p9_LambdaU-3500_pT70_M2000-3500_TuneCP2_13TeV_pythia8_cfi_py" :  6.822e-04+-2.985e-06,
       "UnparToGG_Spin2_du1p9_LambdaU-2000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.421e-02+-6.339e-05,
       "UnparToGG_Spin2_du1p9_LambdaU-2000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.350e-01+-5.744e-04,
    }
    xsecdict.update(xsecdict_temp)
if doMCspin2_du1p1:
    du_tag = ""
    DATASET.append("TestUnparToGG_Spin2_du1p1_LambdaU-3500_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p1_LambdaU-3000_pT70_M3000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p1_LambdaU-3000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p1_LambdaU-3500_pT70_M3500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p1_LambdaU-3000_pT70_M2000-3000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p1_LambdaU-3500_pT70_M2000-3500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p1_LambdaU-2000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p1_LambdaU-2000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p1_LambdaU-3500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p1_LambdaU-3000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin2_du1p1_LambdaU-2000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    xsecdict_temp = {
        "UnparToGG_Spin2_du1p1_LambdaU-3500_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.261e-02+-5.771e-05,
        "UnparToGG_Spin2_du1p1_LambdaU-3000_pT70_M3000_TuneCP2_13TeV_pythia8_cfi_py" :  9.739e-05+-4.068e-07,
        "UnparToGG_Spin2_du1p1_LambdaU-3000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.257e-02+-5.775e-05,
        "UnparToGG_Spin2_du1p1_LambdaU-3500_pT70_M3500_TuneCP2_13TeV_pythia8_cfi_py" :  2.897e-05+-1.073e-07,
        "UnparToGG_Spin2_du1p1_LambdaU-3000_pT70_M2000-3000_TuneCP2_13TeV_pythia8_cfi_py" :  5.893e-04+-2.732e-06,
        "UnparToGG_Spin2_du1p1_LambdaU-3500_pT70_M2000-3500_TuneCP2_13TeV_pythia8_cfi_py" :  5.890e-04+-2.719e-06,
        "UnparToGG_Spin2_du1p1_LambdaU-2000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.450e-02+-7.112e-05,
        "UnparToGG_Spin2_du1p1_LambdaU-2000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.857e-03+-1.034e-05,
        "UnparToGG_Spin2_du1p1_LambdaU-3500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.302e-01+-5.586e-04,
        "UnparToGG_Spin2_du1p1_LambdaU-3000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.286e-01+-5.498e-04,
        "UnparToGG_Spin2_du1p1_LambdaU-2000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.276e-01+-5.545e-04,
    }
    xsecdict.update(xsecdict_temp)

# Spin 0
if doMCspin0_du1p9:
    du_tag = ""
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-2000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-2000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-2000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-3500_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-2500_pT70_M2500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-2500_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-3500_pT70_M3500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-2500_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-3500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-2000_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-2500_pT70_M1000-2500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-2500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-3500_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-3500_pT70_M2000-3500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p9_LambdaU-3500_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    xsecdict_temp = {
        "UnparToGG_Spin0_du1p9_LambdaU-2000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.384e-02+-6.173e-05,
        "UnparToGG_Spin0_du1p9_LambdaU-2000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py" :  9.183e-04+-4.931e-06,
        "UnparToGG_Spin0_du1p9_LambdaU-2000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.354e-01+-5.801e-04,
        "UnparToGG_Spin0_du1p9_LambdaU-3500_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py" :  6.889e-04+-3.469e-06,
        "UnparToGG_Spin0_du1p9_LambdaU-2500_pT70_M2500_TuneCP2_13TeV_pythia8_cfi_py" :  2.467e-04+-1.294e-06,
        "UnparToGG_Spin0_du1p9_LambdaU-2500_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py" :  7.525e-04+-3.858e-06,
        "UnparToGG_Spin0_du1p9_LambdaU-3500_pT70_M3500_TuneCP2_13TeV_pythia8_cfi_py" :  2.607e-05+-1.331e-07,
        "UnparToGG_Spin0_du1p9_LambdaU-2500_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.500e-01+-7.203e-04,
        "UnparToGG_Spin0_du1p9_LambdaU-3500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.347e-01+-5.769e-04,
        "UnparToGG_Spin0_du1p9_LambdaU-2000_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.492e-01+-7.164e-04,
        "UnparToGG_Spin0_du1p9_LambdaU-2500_pT70_M1000-2500_TuneCP2_13TeV_pythia8_cfi_py" :  1.410e-02+-6.509e-05,
        "UnparToGG_Spin0_du1p9_LambdaU-2500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.348e-01+-5.800e-04,
        "UnparToGG_Spin0_du1p9_LambdaU-3500_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.495e-01+-7.179e-04,
        "UnparToGG_Spin0_du1p9_LambdaU-3500_pT70_M2000-3500_TuneCP2_13TeV_pythia8_cfi_py" :  6.710e-04+-3.012e-06,
        "UnparToGG_Spin0_du1p9_LambdaU-3500_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.365e-02+-6.089e-05,
    }
    xsecdict.update(xsecdict_temp)
if doMCspin0_du1p5:
    du_tag = ""
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-2000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-2000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-2000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-2000_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-2500_pT70_M1000-2500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-2500_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-2500_pT70_M2500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-2500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-2500_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-3500_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-3500_pT70_M2000-3500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-3500_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-3500_pT70_M3500_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-3500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p5_LambdaU-3500_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    xsecdict_temp = {
        "UnparToGG_Spin0_du1p5_LambdaU-2000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.412e-02+-6.415e-05,
        "UnparToGG_Spin0_du1p5_LambdaU-2000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py" :  9.747e-04+-5.294e-06,
        "UnparToGG_Spin0_du1p5_LambdaU-2000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.350e-01+-5.822e-04,
        "UnparToGG_Spin0_du1p5_LambdaU-2000_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.493e-01+-7.162e-04,
        "UnparToGG_Spin0_du1p5_LambdaU-2500_pT70_M1000-2500_TuneCP2_13TeV_pythia8_cfi_py" :  1.443e-02+-6.754e-05,
        "UnparToGG_Spin0_du1p5_LambdaU-2500_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py" :  8.097e-04+-4.228e-06,
        "UnparToGG_Spin0_du1p5_LambdaU-2500_pT70_M2500_TuneCP2_13TeV_pythia8_cfi_py" :  2.661e-04+-1.394e-06,
        "UnparToGG_Spin0_du1p5_LambdaU-2500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.352e-01+-5.771e-04,
        "UnparToGG_Spin0_du1p5_LambdaU-2500_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.488e-01+-7.113e-04,
        "UnparToGG_Spin0_du1p5_LambdaU-3500_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.364e-02+-6.041e-05,
        "UnparToGG_Spin0_du1p5_LambdaU-3500_pT70_M2000-3500_TuneCP2_13TeV_pythia8_cfi_py" :  6.893e-04+-3.096e-06,
        "UnparToGG_Spin0_du1p5_LambdaU-3500_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py" :  7.134e-04+-3.637e-06,
        "UnparToGG_Spin0_du1p5_LambdaU-3500_pT70_M3500_TuneCP2_13TeV_pythia8_cfi_py" :  2.795e-05+-1.423e-07,
        "UnparToGG_Spin0_du1p5_LambdaU-3500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.348e-01+-5.779e-04,
        "UnparToGG_Spin0_du1p5_LambdaU-3500_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.479e-01+-7.120e-04,
    }
if doMCspin0_du1p1:
    du_tag = ""
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-4000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-9500_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-8000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-4000_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-8000_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-4000_pT70_M4000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-8000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-9500_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-4000_pT70_M2000-4000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-4000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-8000_pT70_M4000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-9500_pT70_M2000-4000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-8000_pT70_M2000-4000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-8000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-4000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-9500_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-9500_pT70_M4000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    DATASET.append("TestUnparToGG_Spin0_du1p1_LambdaU-9500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py_GEN.root/demo/fgenTree")
    xsecdict_temp = {
        "UnparToGG_Spin0_du1p1_LambdaU-4000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.312e-03+-7.152e-06,
        "UnparToGG_Spin0_du1p1_LambdaU-9500_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py" :  7.605e-04+-3.901e-06,
        "UnparToGG_Spin0_du1p1_LambdaU-8000_pT70_M2000_TuneCP2_13TeV_pythia8_cfi_py" :  7.995e-04+-4.121e-06,
        "UnparToGG_Spin0_du1p1_LambdaU-4000_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.622e-01+-7.828e-04,
        "UnparToGG_Spin0_du1p1_LambdaU-8000_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.511e-01+-7.253e-04,
        "UnparToGG_Spin0_du1p1_LambdaU-4000_pT70_M4000_TuneCP2_13TeV_pythia8_cfi_py" :  3.224e-05+-1.835e-07,
        "UnparToGG_Spin0_du1p1_LambdaU-8000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.413e-02+-6.437e-05,
        "UnparToGG_Spin0_du1p1_LambdaU-9500_pT70_M500-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.494e-01+-7.171e-04,
        "UnparToGG_Spin0_du1p1_LambdaU-4000_pT70_M2000-4000_TuneCP2_13TeV_pythia8_cfi_py" :  1.266e-03+-6.415e-06,
        "UnparToGG_Spin0_du1p1_LambdaU-4000_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.740e-02+-8.481e-05,
        "UnparToGG_Spin0_du1p1_LambdaU-8000_pT70_M4000_TuneCP2_13TeV_pythia8_cfi_py" :  1.309e-05+-6.861e-08,
        "UnparToGG_Spin0_du1p1_LambdaU-9500_pT70_M2000-4000_TuneCP2_13TeV_pythia8_cfi_py" :  7.521e-04+-3.501e-06,
        "UnparToGG_Spin0_du1p1_LambdaU-8000_pT70_M2000-4000_TuneCP2_13TeV_pythia8_cfi_py" :  7.856e-04+-3.697e-06,
        "UnparToGG_Spin0_du1p1_LambdaU-8000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.375e-01+-5.899e-04,
        "UnparToGG_Spin0_du1p1_LambdaU-4000_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.448e-01+-6.410e-04,
        "UnparToGG_Spin0_du1p1_LambdaU-9500_pT70_M1000-2000_TuneCP2_13TeV_pythia8_cfi_py" :  1.401e-02+-6.380e-05,
        "UnparToGG_Spin0_du1p1_LambdaU-9500_pT70_M4000_TuneCP2_13TeV_pythia8_cfi_py" :  1.164e-05+-5.996e-08,
        "UnparToGG_Spin0_du1p1_LambdaU-9500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi_py" :  1.354e-01+-5.842e-04,
    }
    xsecdict.update(xsecdict_temp)

for dset in DATASET:
    if "SM" in dset:
        pattern = "Test([^(]*)_pT([^(]*)_M-([^(]*)_py"
        match = re.findall(pattern, dset)
        PH, pTcut, massrange = match[0]
        #print PH, massrange
    if "Unp" in dset:
        pattern = "TestUnparToGG_Spin([^(]*)_du([^(]*)_LambdaU-([^(]*)_pT([^(]*)_M([^(]*)_TuneCP2_13TeV_pythia8_cfi_py_GEN.root"
        #pattern = "TestUnparToGG_Spin([^(]*)_du([^(]*)_LambdaU([^(]*)_pT([^(]*)_M([^(]*)_TuneCP2_13TeV_pythia8_cfi_py_GEN.root"
        match = re.findall(pattern, dset)
        PH = "Unp"
        spin, du, LambdaU, pTcut, massrange = match[0]

    print match

    # Get Cross-section
    keypattern = "Test([^(]*)_GEN.root"
    matchkey = re.findall(keypattern, dset)
    xseckey = matchkey[0]
    mrange = massrange.replace('-', '_')

    if "SM" in dset:
        classname = "Class_%s_pT%s_M%s" %(PH, pTcut, mrange)
        #print classname
        an_func = "analyze_%s" %(classname)
        xsecval = xsecdict[xseckey]
        outfile = "%s_pT%s_M%s.root" %(PH, pTcut, mrange)
        #rep = {'ClassANGGJets': classname, "xsecvalue": xsecval, "outputfile": outfile, "spin": spin, "inputTree": dset, "analyzefunc": an_func}
    if "Unp" in dset:
        classname = "Class%s_spin%s_du%s_LU%s_pT%s_M%s" %(PH, spin, du, LambdaU, pTcut, mrange)
        classname = classname.replace('-', '_')
        an_func = "analyze_%s" %(classname)
        outfile = "%s_spin%s_du%s_LU%s_pT%s_M%s.root" %(PH, spin, du, LambdaU, pTcut, mrange)
        xsecval = xsecdict[xseckey]
        #print classname

    # Template Replacements
    cmssw_base = os.getenv("CMSSW_BASE")
    #print cmssw_base
    rep = {'ClassANGGJets': classname,
           "xsecvalue": xsecval,
           "outputfile": outfile,
           "cmssw_base": cmssw_base,
           "inputTree": dset,
           "analyzefunc": an_func,
           "numevents": numevents,
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

    outfile_an = open("analyze_%s.C" %(classname), "w+")
    outfile_an.write(an_sub)

def RunAnalyze(file_list):
	for anFile in file_list:
		if anFile.startswith("analyze_Class") and anFile.endswith(".C"):
			root_cmd = "root -l -q %s" %(anFile)
			os.system(root_cmd)
def DelClassFiles(file_list):
    for classFile in file_list:
        if "Class_SM" in classFile:
            del_cmd = "rm %s" %(classFile)
            os.system(del_cmd)
        if "ClassUnp" in classFile:
            del_cmd = "rm %s" %(classFile)
            #print del_cmd
            os.system(del_cmd)
    print "deleted auxilliary files"

if action == "run":
    RunAnalyze(os.listdir('.'))
if action == "del":
    DelClassFiles(os.listdir('.'))

sw.Stop()
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time:  " + str(sw.CpuTime() / 60.0) + " minutes"
