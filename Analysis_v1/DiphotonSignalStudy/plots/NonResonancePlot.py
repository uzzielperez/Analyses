#!/usr/bin/python

import ROOT
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
from hep_plt.Sensitivityfunctions import CalcSensitivity
from hep_plt.Plotfunctions import *

sw = ROOT.TStopwatch()
sw.Start()
gStyle.SetOptStat(0)


# To suppress canvas from popping up. Speeds up plots production.
#gROOT.SetBatch()

doSM 	   = True


# ADD
doADD      = True
NI1_13     = True

# Variables to Plot
kinematicsON = True
genON        = False
angularON    = False

doSMstitch = False
doADDstitch= False


obj = []
if kinematicsON:
        #obj.append("diphotonMinv")
        obj.append("photon1Pt")
        # obj.append("photon2Pt")
        # obj.append("photon1Eta")
        # obj.append("photon2Eta")
        # obj.append("photon1Phi")
        # obj.append("photon2Phi")
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
        if NI1_13:
            DATASETS = []
            DATASETS.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_1000To2000.root")
            DATASETS.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_2000To4000.root")
            DATASETS.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_4000To13000.root")
            DATASETS.append("../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_500To1000.root")
            varhist = [Stitch(DATASETS, var) for var in obj]
            #print len(varhist)

for var, sm, sig in zip(obj, varhistsm, varhist):
    #print var, sm[1], sig[1]
    hstack = []
    hstack.append(sm[0])
    hstack.append(sig[0])
    labels = []
    labels.append(sm[1])
    labels.append(sig[1])

    OverlayHists(var, hstack, labels)
