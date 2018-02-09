import ROOT
import sys

ext = raw_input("Enter Extension: ")
filename="root://cmsxrootd.fnal.gov//store/user/cuperez/"+ext
print filename

f =ROOT.TFile.Open(filename)
