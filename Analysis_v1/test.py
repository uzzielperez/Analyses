import ROOT 

#FILE PATH in EOS
INPATH = 'root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-1000To2000_Pt-50_13TeV-sherpa.root'

#First get the TTree from the ROOT file
rfile = ROOT.TFile.Open(INPATH)
rfile.cd("diphoton")
intree = rfile.Get('fTree')
fTree.Print()
