////#include "DiPhoton16BKG.C"
//v#include <iostream>
//#include "TStopwatch.h"
//using namespace std;
//
//int analyze(){
//	// start stopwatch
//	TStopwatch sw;
//	sw.Start();
//
	// Chain trees 
	// trialClass t(Chainedtrees), chain.Add("file.root", 0) to calculate correct entries add 0 arg
{
TChain chain("diphoton/fTree");
chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Run2016Data-Merged/DoubleEG__Run2016B-03Feb2017_ver2-v2__MINIAOD/out.root", 0);
chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Run2016Data-Merged/DoubleEG__Run2016C-03Feb2017-v1__MINIAOD/out.root", 0);
chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Run2016Data-Merged/DoubleEG__Run2016D-03Feb2017-v1__MINIAOD/out.root", 0);
chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Run2016Data-Merged/DoubleEG__Run2016E-03Feb2017-v1__MINIAOD/out.root", 0);
chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Run2016Data-Merged/DoubleEG__Run2016F-03Feb2017-v1__MINIAOD/out.root", 0);
chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Run2016Data-Merged/DoubleEG__Run2016G-03Feb2017-v1__MINIAOD/out.root", 0);
chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Run2016Data-Merged/DoubleEG__Run2016H-03Feb2017_ver2-v1__MINIAOD/out.root", 0);
chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Run2016Data-Merged/DoubleEG__Run2016H-03Feb2017_ver3-v1__MINIAOD/out.root", 0);
TH1D *h = new TH1D("h", "h", 30, 0, 3000); 

chain.Draw("Diphoton.Minv >> h", "isGood && Diphoton.Minv > 500. && Photon1.r9_5x5 > 0.8 && Photon2.r9_5x5 > 0.8  && Photon1.pt > 75. && Photon2.pt > 75. &&  TMath::Abs(Photon1.scEta) < 1.4442 && TMath::Abs(Photon2.scEta) < 1.4442 "); 


//chain.Draw("Diphoton.Minv >> h", "isGood && Diphoton.Minv > 500. && Photon1.r9_5x5 > 0.8 && Photon2.r9_5x5 > 0.8  && Photon1.pt > 75. && Photon2.pt > 75. && (( TMath::Abs(Photon1.scEta) < 1.4442 && 1.566 < TMath::Abs(Photon2.scEta) && TMath::Abs(Photon2.scEta)< 2.5) || ( TMath::Abs(Photon2.scEta) < 1.4442 && 1.566 < TMath::Abs(Photon1.scEta)&& TMath::Abs(Photon1.scEta) < 2.5))"); 
TFile f("out.root", "RECREATE");
h->Write();
f.ls();
f.Close(); 
}


