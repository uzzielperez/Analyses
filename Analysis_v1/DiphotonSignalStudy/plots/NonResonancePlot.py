#!/usr/bin/python

import ROOT
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
from hep_plt.Sensitivityfunctions import CalcSensitivityADD
from hep_plt.Plotfunctions import *

sw = ROOT.TStopwatch()
sw.Start()
gStyle.SetOptStat(0)


# To suppress canvas from popping up. Speeds up plots production.
gROOT.SetBatch()

doSM 	   = True

# ADD
doADD         = True
NI1_13        = True
NI1_13_m2000  = True

# Variables to Plot
kinematicsON = True
genON        = True
angularON    = True



obj = []
if kinematicsON:
        obj.append("diphotonMinv")
        obj.append("photon1Pt")
        obj.append("photon2Pt")
        obj.append("photon1Eta")
        obj.append("photon2Eta")
       	obj.append("photon1Phi")
        obj.append("photon2Phi")
if angularON:
        obj.append("chidiphoton")
        obj.append("diphotoncosthetastar")
if genON:
        obj.append("gendiphotonMinv")
        obj.append("genphoton1Pt")
        obj.append("genphoton2Pt")
        obj.append("genphoton1Eta")
        obj.append("genphoton2Eta")
        obj.append("genphoton1Phi")
        obj.append("genphoton2Phi")
        if angularON:
                obj.append("genchidiphoton")
                obj.append("gendiphotoncosthetastar")


if doSM:
        DATASETSM = []
        # DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_60To200_Pt_50.root")
        # DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_200To500_Pt_50.root")
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_500To1000_Pt_50.root")
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_1000To2000_Pt_50.root")
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_2000To4000_Pt_50.root")
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_4000To6000_Pt_50.root")
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_6000To8000_Pt_50.root")
        varhistsm = [Stitch(DATASETSM, var) for var in obj]
if doADD:
	signal = []
        if NI1_13:
	    tag = "NI1_13"
            DATASETS = []
            DATASETS.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_1000To2000.root")
            DATASETS.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_2000To4000.root")
            DATASETS.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_4000To13000.root")
            DATASETS.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_500To1000.root")
            vhist = [Stitch(DATASETS, var) for var in obj]
	    signal.append(vhist)
            #print len(varhist)
        if NI1_13_m2000:
            tag = tag + "mgg2000"
            DSETm2000 = []
            DSETm2000.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_1000To2000mgg_2000.root")
            DSETm2000.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_2000To4000mgg_2000.root")
            DSETm2000.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_4000To13000mgg_2000.root")
            DSETm2000.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_500To1000mgg_2000.root")
            # Stitch function returns stitched histogram and label - Tuple
	    vhist2 = [Stitch(DSETm2000, var) for var in obj]
	    signal.append(vhist2)


#for var, sm, sig in zip(obj, varhistsm, signal[0]):
#	# New stack for each variable
#	hstack, labels = [], []
#	hstack.append(sm[0])
#	labels.append(sm[1])
#	hstack.append(sig[0])
#	labels.append(sig[1])
#	
#	OverlayHists(var, hstack, labels, tag="NI13orig", lumi=137)
#print signal[2][1]
print obj
#print signal[0][1][1]
ipts, ivar = 0, 0 #signal[modelptindex][varindex][hist(0)/label(1)]
for var, sm in zip(obj, varhistsm):
	# New stack for each variable
	hstack, labels = [], []
	hstack.append(sm[0])
	labels.append(sm[1])
	for sig in signal:
		#print var, sig[ivar][1]
		hstack.append(sig[ivar][0])
		labels.append(sig[ivar][1])
	#print labels	
	ivar = ivar + 1  
	OverlayHists(var, hstack, labels, tag="NI13orig", lumi=137)



# Original
"""
for var, sm, sig in zip(obj, varhistsm, varhist):
    #print var, sm[1], sig[1]
    hstack = []
    hstack.append(sm[0])
    hstack.append(sig[0])
    labels = []
    labels.append(sm[1])
    labels.append(sig[1])

    OverlayHists(var, hstack, labels)
"""
