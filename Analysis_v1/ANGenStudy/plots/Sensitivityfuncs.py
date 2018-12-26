#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad,TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
#from ROOT import kBlack, kBlue, kRed, kGreen, kMagenta, kCyan, kOrange, kViolet, kSpring
from ROOT import kBlue, kOrange, kCyan, kRed, kMagenta, kGreen, kViolet, kSpring, kPink, kAzure
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
from ROOT import TMath
#from legend import *
#from plotsHelpercomp import *
import re

import sys
CMSlumiPath = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/pyroot'
sys.path.append(CMSlumiPath)
from CMSlumi import CMS_lumi, set_CMS_lumi
import argparse
import numpy as np 
#import scipy.stats.distributions
from scipy.stats import poisson
import math
sw = ROOT.TStopwatch()
sw.Start()

LambdaT = "ALL"
SMPythia8 = True
SM = False
ADD = True

tag = "b"
zoom = False
#drawstyle = "hist, same"
drawstyle = "same"
#intlumi = 35.9
# Draw Options
DrawAsHi = False
gStyle.SetOptStat(0)

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html
def poisson_probability(actual, mean):

    # naive:   math.exp(-mean) * mean**actual / factorial(actual)
    return   math.exp(-mean) * mean**actual / math.factorial(actual)
    
# iterative, to keep the components from getting too large or small:
#    p = math.exp(-mean)
#    for i in xrange(actual):
#        p *= mean
#        p /= i+1
#    return p
# 

def CalcSensitivity(obj, DATASET, intlumi):
      uf = []
      for datafile in DATASET:
	      uf.append(ROOT.TFile(datafile, "READ"))
      uh = []
      for openfile in uf:
	      uh.append(openfile.Get(obj))
      histClones = []
      iset = 0
      i = 0
      while i < len(DATASET):
	      histClone = uh[i].Clone("histdu%s" %(DATASET[i]))
    	      histClones.append(histClone)
    	      i = i + 1
      sig = []
      j = 0
      for histclone in histClones:
	      if "SM" in DATASET[j]:
		      histSM = histclone
		      histSM.Scale(intlumi)
		      b = histSM.Integral()
		      print "b = ", b  
	      else:
		      pattern = "OUTUnp_LU([^(]*)_du([^(]*)_spin2_ggONM([^(]*).root"
		      match = re.findall(pattern, DATASET[j])	
		      LU, du, massmin = match[0]
		      #print "prescaled: ", histclone.Integral(), " ", histclone.GetEntries()
		      histclone.Scale(intlumi)
		      #print histclone.Integral(), " ", histclone.GetEntries()
		      s = histclone.Integral() 
		      sig.append(s) 
	              print intlumi,  "fb-1; LU, du, massmin= ", LU, du, massmin, ";b: ", b, "; sb: ", s, "; P(b, s+b): ", TMath.Poisson(b, s)
	      j = j+1

      #print poisson.p   
      #print np.random.poisson(b, 10000) #describes the probability of b events occuring with the observed s+B 
      #print poisson.pmf(b, splusb)

