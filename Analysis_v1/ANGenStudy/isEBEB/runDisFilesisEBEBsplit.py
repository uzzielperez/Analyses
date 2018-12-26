import ROOT
import time
import subprocess
import os
import argparse
import re
from string import Template
import sys

# Timer
sw = ROOT.TStopwatch()
sw.Start()

#filepath = "/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out"
DATASET = []

do1p93Test = False
doMCTest = False
doMCPlusTest = False
doMCIPresent = True

#Templates
class_Ctemp = "ClassTemplateisEBEB.C"
class_htemp = "ClassTemplateisEBEB.h"
run_analyzetemp = "analyzeTemplate.C"

#pattern = r'TestSTest%sUnp([^(]*)p0_spin-([^(]*)_M_([^(]*)_py_GEN' %(du_tag)
#pattern = r'TestMCI_Unp-LU500-du1p8_spin-2-ggffON_pT125_M_500-2000_TuneCP2_py_GEN'

xsecdict = {}
if doMCIPresent:
    du_tag = "mci"
    DATASET.append("TestFinMCISM_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCISM_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p1_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p1_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p1_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p1_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p5_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p5_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p5_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p5_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p6_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p6_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p6_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p6_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p8_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p8_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p8_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU2000p0_du1p8_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p6_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p1_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p5_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p8_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p8_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p1_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p5_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p1_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestFinMCIUnp_LU5000p0_du1p1_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p5_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p8_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p5_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p8_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p6_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p6_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU5000p0_du1p6_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p1_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p1_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p1_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p1_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p5_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p5_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p5_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p5_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p6_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p6_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p6_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p6_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p8_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p8_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p8_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestFinMCIUnp_LU1000p0_du1p8_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")

    xsecdict_temp = {"FinMCISM_M_2000_py" :  4.803e-04+-2.432e-06,
    "FinMCISM_M_500-2000_py" :  1.195e-01+-5.634e-04,
    "FinMCIUnp_LU2000p0_du1p1_spin-2_M_2000_py": 2.175e-03+-1.265e-05,
    "FinMCIUnp_LU2000p0_du1p8_spin-0_M_500-2000_py": 1.197e-01+-5.616e-04,
    "FinMCIUnp_LU2000p0_du1p6_spin-0_M_2000_py": 6.273e-04+-3.390e-06,
    "FinMCIUnp_LU2000p0_du1p1_spin-2_M_500-2000_py": 1.206e-01+-5.821e-04,
    "FinMCIUnp_LU2000p0_du1p6_spin-2_M_2000_py": 6.586e-04+-3.275e-06,
    "FinMCIUnp_LU2000p0_du1p1_spin-0_M_500-2000_py": 1.867e-01+-9.392e-04,
    "FinMCIUnp_LU2000p0_du1p5_spin-0_M_500-2000_py": 1.217e-01+-5.798e-04,
    "FinMCIUnp_LU2000p0_du1p5_spin-2_M_2000_py": 6.885e-04+-3.447e-06,
    "FinMCIUnp_LU2000p0_du1p1_spin-0_M_2000_py": 3.265e-03+-1.982e-05,
    "FinMCIUnp_LU2000p0_du1p8_spin-2_M_500-2000_py": 1.205e-01+-5.661e-04,
    "FinMCIUnp_LU2000p0_du1p6_spin-2_M_500-2000_py": 1.205e-01+-5.668e-04,
    "FinMCIUnp_LU2000p0_du1p6_spin-0_M_500-2000_py": 1.194e-01+-5.661e-04,
    "FinMCIUnp_LU2000p0_du1p5_spin-2_M_500-2000_py": 1.208e-01+-5.753e-04,
    "FinMCIUnp_LU2000p0_du1p5_spin-0_M_2000_py": 7.203e-04+-3.991e-06,
    "FinMCIUnp_LU2000p0_du1p8_spin-0_M_2000_py": 5.854e-04+-3.071e-06,
    "FinMCIUnp_LU2000p0_du1p8_spin-2_M_2000_py": 6.711e-04+-3.313e-06,
    "FinMCIUnp_LU5000p0_du1p6_spin-0_M_2000_py":  4.835e-04+-2.449e-06,
    "FinMCIUnp_LU5000p0_du1p1_spin-2_M_500-2000_py":  1.175e-01+-5.598e-04,
    "FinMCIUnp_LU5000p0_du1p5_spin-2_M_500-2000_py":  1.198e-01+-5.652e-04,
    "FinMCIUnp_LU5000p0_du1p8_spin-0_M_2000_py":  4.855e-04+-2.458e-06,
    "FinMCIUnp_LU5000p0_du1p8_spin-0_M_500-2000_py":  1.203e-01+-5.712e-04,
    "FinMCIUnp_LU5000p0_du1p1_spin-0_M_2000_py":  7.505e-04+-4.103e-06,
    "FinMCIUnp_LU5000p0_du1p5_spin-0_M_500-2000_py":  1.199e-01+-5.690e-04,
    "FinMCIUnp_LU5000p0_du1p1_spin-0_M_500-2000_py":  1.263e-01+-6.057e-04,
    "FinMCIUnp_LU5000p0_du1p1_spin-2_M_2000_py":  4.456e-04+-2.296e-06,
    "FinMCIUnp_LU5000p0_du1p5_spin-2_M_2000_py":  4.769e-04+-2.418e-06,
    "FinMCIUnp_LU5000p0_du1p8_spin-2_M_2000_py":  4.881e-04+-2.473e-06,
    "FinMCIUnp_LU5000p0_du1p5_spin-0_M_2000_py":  4.822e-04+-2.443e-06,
    "FinMCIUnp_LU5000p0_du1p8_spin-2_M_500-2000_py":  1.193e-01+-5.675e-04,
    "FinMCIUnp_LU5000p0_du1p6_spin-2_M_2000_py":  4.852e-04+-2.413e-06,
    "FinMCIUnp_LU5000p0_du1p6_spin-2_M_500-2000_py":  1.193e-01+-5.676e-04,
    "FinMCIUnp_LU5000p0_du1p6_spin-0_M_500-2000_py":  1.203e-01+-5.710e-04,
    "FinMCIUnp_LU1000p0_du1p6_spin-2_M_2000_py" :  1.248e-02+-7.112e-05,
    "FinMCIUnp_LU1000p0_du1p8_spin-0_M_2000_py" :  6.067e-03+-3.613e-05,
    "FinMCIUnp_LU1000p0_du1p5_spin-2_M_2000_py" :  1.372e-02+-7.981e-05,
    "FinMCIUnp_LU1000p0_du1p1_spin-2_M_500-2000_py" :  4.097e-01+-1.963e-03,
    "FinMCIUnp_LU1000p0_du1p5_spin-0_M_2000_py" :  6.030e-03+-3.809e-05,
    "FinMCIUnp_LU1000p0_du1p6_spin-0_M_500-2000_py" :  1.319e-01+-6.331e-04,
    "FinMCIUnp_LU1000p0_du1p5_spin-2_M_500-2000_py" :  1.411e-01+-6.517e-04,
    "FinMCIUnp_LU1000p0_du1p8_spin-2_M_2000_py" :  1.629e-02+-8.981e-05,
    "FinMCIUnp_LU1000p0_du1p1_spin-0_M_500-2000_py" :  5.389e-01+-2.929e-03,
    "FinMCIUnp_LU1000p0_du1p8_spin-0_M_500-2000_py" :  1.262e-01+-5.978e-04,
    "FinMCIUnp_LU1000p0_du1p6_spin-2_M_500-2000_py" :  1.361e-01+-6.268e-04,
    "FinMCIUnp_LU1000p0_du1p6_spin-0_M_2000_py" :  5.106e-03+-3.170e-05,
    "FinMCIUnp_LU1000p0_du1p1_spin-2_M_2000_py" :  4.545e-02+-2.845e-04,
    "FinMCIUnp_LU1000p0_du1p1_spin-0_M_2000_py" :  2.180e-02+-1.366e-04,
    "FinMCIUnp_LU1000p0_du1p5_spin-0_M_500-2000_py" :  1.388e-01+-6.704e-04,
    "FinMCIUnp_LU1000p0_du1p8_spin-2_M_500-2000_py" :  1.341e-01+-6.133e-04,

    # FinMCIUnp_LU3000p0_du1p6_spin-0_M_2000_py.txt :  5.014e-04+-2.558e-06
    # FinMCIUnp_LU3000p0_du1p8_spin-0_M_2000_py.txt :  4.940e-04+-2.493e-06
    # FinMCIUnp_LU3000p0_du1p5_spin-0_M_2000_py.txt :  5.203e-04+-2.700e-06
    # FinMCIUnp_LU3000p0_du1p5_spin-0_M_500-2000_py.txt :  1.197e-01+-5.650e-04
    # FinMCIUnp_LU3000p0_du1p1_spin-2_M_2000_py.txt :  6.308e-04+-3.329e-06
    # FinMCIUnp_LU3000p0_du1p1_spin-0_M_2000_py.txt :  1.446e-03+-8.335e-06
    # FinMCIUnp_LU3000p0_du1p5_spin-2_M_500-2000_py.txt :  1.187e-01+-5.650e-04
    # FinMCIUnp_LU3000p0_du1p8_spin-2_M_2000_py.txt :  5.026e-04+-2.507e-06
    # FinMCIUnp_LU3000p0_du1p1_spin-0_M_500-2000_py.txt :  1.438e-01+-7.019e-04
    # FinMCIUnp_LU3000p0_du1p6_spin-2_M_2000_py.txt :  4.970e-04+-2.486e-06
    # FinMCIUnp_LU3000p0_du1p5_spin-2_M_2000_py.txt :  4.957e-04+-2.517e-06
    # FinMCIUnp_LU3000p0_du1p1_spin-2_M_500-2000_py.txt :  1.155e-01+-5.531e-04
    # FinMCIUnp_LU3000p0_du1p6_spin-0_M_500-2000_py.txt :  1.201e-01+-5.743e-04
    # FinMCIUnp_LU3000p0_du1p8_spin-2_M_500-2000_py.txt :  1.198e-01+-5.666e-04
    # FinMCIUnp_LU3000p0_du1p6_spin-2_M_500-2000_py.txt :  1.202e-01+-5.709e-04
    # FinMCIUnp_LU3000p0_du1p8_spin-0_M_500-2000_py.txt :  1.199e-01+-5.694e-04
    }
    xsecdict.update(xsecdict_temp)
if doMCPlusTest:
    du_tag = ""
    DATASET.append("TestMCIPlus2_Unp-LU4500-du1p01_spin-2-ggON_pT125_M_1000_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCIPlus2_Unp-LU4500-du1p01_spin-2-ggON_pT125_M_1500_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCIPlus0_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_1000_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCIPlus0_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_1500_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCIPlus2_Unp-LU500-du1p8_spin-2-ggON_pT125_M_1000_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCIPlus2_Unp-LU500-du1p8_spin-2-ggON_pT125_M_1500_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCIPlus_SM_pT125_M_1000_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCIPlus_SM_pT125_M_1500_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCIPlus_SM_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")

    xsecdict_temp = {"MCIPlus_SM_pT125_M_2000_TuneCP2_py":	5.312e-04+-2.734e-06,
    "MCIPlus_SM_pT125_M_1000_TuneCP2_py":	1.068e-02+-5.607e-05,
    "MCIPlus0_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_1000_TuneCP2_py":	1.175e-02+-6.217e-05,
    "MCIPlus2_Unp-LU500-du1p8_spin-2-ggON_pT125_M_1000_TuneCP2_py" :  1.282e-02+-6.459e-05, #1.282e-02+-6.459e-05
    "MCIPlus2_Unp-LU4500-du1p01_spin-2-ggON_pT125_M_1000_TuneCP2_py" : 9.450e-03 +- 5.049e-05,

    "MCIPlus_SM_pT125_M_1500_TuneCP2_py":	2.073e-03+-1.081e-05,
    "MCIPlus0_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_1500_TuneCP2_py":	2.943e-03+-1.584e-05,
    "MCIPlus2_Unp-LU500-du1p8_spin-2-ggON_pT125_M_1500_TuneCP2_py" :  3.629e-03+-1.921e-05, #3.629e-03+-1.921e-05
    "MCIPlus2_Unp-LU4500-du1p01_spin-2-ggON_pT125_M_1500_TuneCP2_py" : 9.450e-03 +- 5.049e-05,
    }
    xsecdict.update(xsecdict_temp)
if doMCTest:
    du_tag = ""
    DATASET.append("TestMCI_SM_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCI_SM_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0-ggON_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-2-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-2-ggON_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-2-ggffON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-2-ggffON_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-2_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-2_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    xsecdict_temp = {"MCI_SM_pT125_M_500-2000_TuneCP2_py":	9.799e-02+-4.831e-04,
                     "MCI_Unp-LU500-du1p8_spin-2-ggON_pT125_M_500-2000_TuneCP2_py":	9.947e-02+-4.855e-04,
                     "MCI_Unp-LU500-du1p8_spin-2-ggffON_pT125_M_500-2000_TuneCP2_py":	1.959e-01+-9.612e-04,
                     "MCI_Unp-LU500-du1p8_spin-2_pT125_M_500-2000_TuneCP2_py":	9.517e-02+-4.627e-04,
                     "MCI_Unp-LU500-du1p8_spin-0_pT125_M_500-2000_TuneCP2_py":	5.584e-03+-3.052e-05,
                     "MCI_Unp-LU500-du1p8_spin-0-ggON_pT125_M_500-2000_TuneCP2_py":	5.584e-03+-3.052e-05,
                     "MCI_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_500-2000_TuneCP2_py":	9.977e-02+-4.908e-04,
                     "MCI_SM_pT125_M_2000_TuneCP2_py":	  5.312e-04+-2.734e-06,
                     "MCI_Unp-LU500-du1p8_spin-2-ggON_pT125_M_2000_TuneCP2_py":	1.662e-03+-9.437e-06,
                     "MCI_Unp-LU500-du1p8_spin-2-ggffON_pT125_M_2000_TuneCP2_py":	2.186e-03+-1.208e-05,
                     "MCI_Unp-LU500-du1p8_spin-2_pT125_M_2000_TuneCP2_py":	1.650e-03+-9.361e-06,
                     "MCI_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_2000_TuneCP2_py":	1.151e-03+-6.490e-06,
                     "MCI_Unp-LU500-du1p8_spin-0_pT125_M_2000_TuneCP2_py":	6.191e-04+-3.766e-06,
                     "MCI_Unp-LU500-du1p8_spin-0-ggON_pT125_M_2000_TuneCP2_py":	6.199e-04+-3.742e-06,
                     }
    xsecdict.update(xsecdict_temp)
for dset in DATASET:
    if "SM" in dset:
        ## TestMCIPlus_SM_pT125_M_2000
        pattern = "TestFinMCISM_M_([^(]*)_py_GEN"
        match = re.findall(pattern, dset)
        massrange = match[0]
        #keypattern = "Test([^(]*)_GEN"
	#matchkey = re.findall(keypattern, dset)
        #print dset, " ", match, " ", matchkey

        #print massrange
        #print PH, massrange
    if "Unp" in dset:
        #pattern = "TestMCI_([^(]*)-LU([^(]*)-du([^(]*)_spin-([^(]*)([^(]*)_pT125_M_([^(]*)_TuneCP2_py_GEN"
        pattern = "TestFinMCIUnp_LU([^(]*)p0_du([^(]*)_spin-([^(]*)_M_([^(]*)_py_GEN"
        # if "Plus0" in dset:
        #     pattern = TestFinMCIUnp_LU2000p0_du1p8_spin-2_M_500-2000_py_GEN
        #     pattern = "TestMCIPlus0_([^(]*)-LU([^(]*)-du([^(]*)_spin-([^(]*)-([^(]*)_pT125_M_([^(]*)_TuneCP2_py_GEN.root"
        # if "Plus2" in dset:
        #     pattern = "TestMCIPlus2_([^(]*)-LU([^(]*)-du([^(]*)_spin-([^(]*)-([^(]*)_pT125_M_([^(]*)_TuneCP2_py_GEN.root"
        match = re.findall(pattern, dset);
        LambdaU, du, spin, massrange = match[0]
        if LambdaU == '500':
             LambdaU = '1500' #typo
        #print PH, massrange

    keypattern = "Test([^(]*)_GEN"
    matchkey = re.findall(keypattern, dset)
    #keypattern = "Test([^(]*)GEN.root"
    #matchkey = re.findall(keypattern, dset)
    print dset, " ", matchkey
    xseckey = matchkey[0]
    mrange = massrange.replace('-', '_')
    if "SM" in dset:
        PH = "SM"
        classname = "Class_%s_%s" %(PH, mrange)
        #print classname
        an_func = "analyze_%s" %(classname)
        xsecval = xsecdict[xseckey]
        outfile = "%s_M%s.root" %(PH, mrange)
        #rep = {'ClassANGGJets': classname, "xsecvalue": xsecval, "outputfile": outfile, "spin": spin, "inputTree": dset, "analyzefunc": an_func}
    if "Unp" in dset:
        classname = "ClassLU%s_du%s_spin%s_M%s" %(LambdaU, du, spin, mrange)
        classname = classname.replace('-', '_')
        an_func = "analyze_%s" %(classname)
        outfile = "LU%s_du%s_spin%s_M%s.root" %(LambdaU, du, spin, mrange)
        xsecval = xsecdict[xseckey]
        #print classname

    rep = {'ClassANGGJets': classname, "xsecvalue": xsecval, "outputfile": outfile, "inputTree": dset, "analyzefunc": an_func}
    #print outfile

    #Read and replace template file
    C_src = Template(open(class_Ctemp).read())
    C_sub = C_src.substitute(rep)

    h_src = Template(open(class_htemp).read())
    h_sub = h_src.substitute(rep)

    an_src = Template(open(run_analyzetemp).read())
    an_sub = an_src.substitute(rep)

    #write to file
    #os.chdir("MakeClassFiles")
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
        if "Class_" in classFile:
            del_cmd = "rm %s" %(classFile)
            #print del_cmd
            os.system(del_cmd)
    print "deleted auxilliary files"
RunAnalyze(os.listdir('.'))
#DelClassFiles(os.listdir('.'))

sw.Stop()
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time:  " + str(sw.CpuTime() / 60.0) + " minutes"
