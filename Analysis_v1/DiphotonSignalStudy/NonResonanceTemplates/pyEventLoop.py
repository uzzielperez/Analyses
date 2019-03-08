#! /usr/bin/env python
import argparse
from pyRunDis import chaindis
# Code from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideCMSDataAnalysisSchoolLPC2018egamma
# Command line options
parser = argparse.ArgumentParser(description="A simple ttree plotter")
#parser.add_argument("-i", "--inputfiles", dest="inputfiles", default=["ggtree_mc_GluGluHToGG_M-125.root"], nargs='*', help="List of input ggNtuplizer files")
parser.add_argument("-o", "--outputfile", dest="outputfile", default="plots.root", help="Input ggNtuplizer file")
parser.add_argument("-m", "--maxevents", dest="maxevents", type=int, default=-1, help="Maximum number events to loop over. Default set to -1 to loop over all events in the input file/s.")
parser.add_argument("-t", "--ttree", dest="ttree", default="diphoton/fTree", help="TTree Name")
args = parser.parse_args()

import numpy as np
import ROOT
import os

if os.path.isfile('~/.rootlogon.C'): ROOT.gROOT.Macro(os.path.expanduser('~/.rootlogon.C'))
ROOT.gROOT.SetBatch()
ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetOptStat(000000)
ROOT.gStyle.SetPalette(ROOT.kRainBow)
ROOT.gStyle.UseCurrentStyle()

# Start Timer
sw = ROOT.TStopwatch()
sw.Start()

# Input ggNtuple
tchain = ROOT.TChain(args.ttree)
#for filename in args.inputfiles: tchain.Add("root://cmseos.fnal.gov//eos/uscms%s/*root"  %(filename))
for filename in chaindis(): tchain.Add("root://cmseos.fnal.gov//eos/uscms%s/*root"  %(filename))
print 'Total number of events: ' + str(tchain.GetEntries())

# Output file
file_out = ROOT.TFile(args.outputfile, 'recreate')
# Histograms to fill
diphotonMinv = ROOT.TH1D('diphotonMinv', r'm_{#gamma#gamma]', 100, 20.0, 1000.0)
chidiphoton = ROOT.TH1D('chidiphoton', r'#chi_{#gamma#gamma}', 80, 0, 50)
diphotoncosthetastar = ROOT.TH1D('diphotoncosthetastar', r'cos#theta*', 80, -1, 1)

diphotonMinv.Sumw2()
chidiphoton.Sumw2()
diphotoncosthetastar.Sumw2()

tree = args.ttree
tree.SetBranchAddress(“Diphoton”, Diphoton)

#Loop over all the events in the input ntuple
for ievent,event in enumerate(tchain):
    if ievent > args.maxevents and args.maxevents != -1: break
    if ievent % 10000 == 0: print 'Processing entry ' + str(ievent)

    weight = event.weightAll
    if event.isGood:
        #print event.Diphoton_Minv
        diphotonMinv.Fill(event.Diphoton.Minv)
        #chidiphoton.Fill(event.phoEta[i])
        #diphotoncosthetastar.Fill(event.phoPhi[i])

#file_out.Write()
#file_out.Close()

# Stop Timer
sw.Stop()
print 'Real time: ' + str(round(sw.RealTime() / 60.0,2)) + ' minutes'
print 'CPU time:  ' + str(round(sw.CpuTime() / 60.0,2)) + ' minutes'
