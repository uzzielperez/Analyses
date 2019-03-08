#!/usr/bin/python

import ROOT
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
from hep_plt.Sensitivityfunctions import CalcSensitivityADD, GetIntegralfromRange
from hep_plt.Plotfunctions import *
import argparse



# Command line options
parser = argparse.ArgumentParser(description="NonResonance")
parser.add_argument("-p", "--plot", action="store_true", help="Clean directory and delete copied files")
parser.add_argument("-s", "--sensitivity", action="store_true", help="Run os.system(cmd) to get CRAB files.")
args = parser.parse_args()

sw = ROOT.TStopwatch()
sw.Start()
gStyle.SetOptStat(0)


# To suppress canvas from popping up. Speeds up plots production.
gROOT.SetBatch()

doSM 	   = True

# ADD
doADD         = True

var = "chidiphoton"
#var = "diphotoncosthetastar"
#var = "diphotonMinv"

if doSM:
        DATASETSM = []
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_1000To2000_Pt_50mgg_2000.root")
       	DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_4000To6000_Pt_50mgg_2000.root")
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_6000To8000_Pt_50mgg_2000.root")
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_2000To4000_Pt_50mgg_2000.root")
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_500To1000_Pt_50mgg_2000.root")
	histSM, labelSM = Stitch(DATASETSM, var)
	
if doADD:
	signal = []
        DSETm2000 = []
        DSETm2000.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_1000To2000mgg_2000.root")
        DSETm2000.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_2000To4000mgg_2000.root")
       	DSETm2000.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_4000To13000mgg_2000.root")
        DSETm2000.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_500To1000mgg_2000.root")
	hist, label = Stitch(DSETm2000, var) 

#histSM = histSM.Scale(137)
#hist   = hist.Scale(137)

xmin, xmax = 0, 20
print label
b = GetIntegralfromRange(xmin, xmax, histSM)
sb = GetIntegralfromRange(xmin, xmax, hist)
print b
print sb

hstack = [histSM, hist]
labell = [labelSM, label]

CalcSensitivityADD(var, hstack, labell)
