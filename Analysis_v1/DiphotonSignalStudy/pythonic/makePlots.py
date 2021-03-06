import argparse
import numpy as np
import ROOT
import os

import argparse
parser = argparse.ArgumentParser(description="A simple ttree plotter")
parser.add_argument("-i", "--inputfiles", dest="inputfiles", default=["ggtree_mc.root"], nargs='*', help="List of input ggNtuplizer files")
parser.add_argument("-o", "--outputfile", dest="outputfile", default="plots.root", help="Input ggNtuplizer file")
parser.add_argument("-m", "--maxevents", dest="maxevents", type=int, default=-1, help="Maximum number events to loop over")
parser.add_argument("-t", "--ttree", dest="ttree", default="ggNtuplizer/EventTree", help="TTree Name")
args = parser.parse_args()

#----------------------------------------------------------

doSherpaADD   = True
DATASET = []
if doSherpaADD:
    DATASET.append('/store/user/cawest/ADDGravToGG_MS-6000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/crab_ADDGravToGG_MS-6000_NED-4_KK-1_M-1000To2000_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/181106_182643/0000')
    DATASET.append('/store/user/cawest/ADDGravToGG_MS-6000_NED-4_KK-1_M-2000To4000_13TeV-sherpa/crab_ADDGravToGG_MS-6000_NED-4_KK-1_M-2000To4000_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/181106_182658/0000')
    #DATASET.append('/store/user/cawest/ADDGravToGG_MS-6000_NED-4_KK-1_M-200To500_13TeV-sherpa/crab_ADDGravToGG_MS-6000_NED-4_KK-1_M-200To500_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/181106_182714/0000')
    #DATASET.append('/store/user/cawest/ADDGravToGG_MS-6000_NED-4_KK-1_M-4000To6000_13TeV-sherpa/crab_ADDGravToGG_MS-6000_NED-4_KK-1_M-4000To6000_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/181106_182726/0000')
    #DATASET.append('/store/user/cawest/ADDGravToGG_MS-6000_NED-4_KK-1_M-500To1000_13TeV-sherpa/crab_ADDGravToGG_MS-6000_NED-4_KK-1_M-500To1000_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/181106_182739/0000')

#-----------------------------------------------------------

# Adding files to TChain
tree = 'diphoton/fTree'
tchain = ROOT.TChain(tree)
print "Adding files to %s" %(tree)
for e in DATASET:
	rf = "root://cmseos.fnal.gov//eos/uscms%s/*root" %(e)
	tchain.Add(rf,0)

#-----------------------------------------------------------

# Histograms 
fileOut = ROOT.TFile(args.outputfile, 'recreate')
hMinv   = ROOT.TH1D('hMinv', 'invariant mass', 100, 500, 10000) 

# Get Branches
weightAll    = tchain.GetBranch("Event").GetLeaf('weightAll')
diphotonminv = tchain.GetBranch("Diphoton").GetLeaf('Minv')
isGood       = tchain.GetBranch("isGood").GetLeaf('isGood') 

#------------------------------------------------------------

# Loop over all events in the input ntuple
for ievent, event in enumerate(tchain):
 	if ievent % 10000 == 0: print 'Processing entry ' + str(ievent)
 	if ievent > args.maxevents and args.maxevents != -1: break
	
	weight = weightAll.GetValue(ievent)
	#if isGood.GetValue(ievent):
	hMinv.Fill(diphotonminv.GetValue(ievent))		

fileOut.Write()
fileOut.Close()	
