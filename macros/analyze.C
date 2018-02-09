#include "DiPhoton16BKG.C"
#include <iostream>

using namespace std;

int analyze(){
	//For one file:
	
	//TFile *f = TFile::Open("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-8000To13000_Pt-50_13TeV-sherpa.root");
        //f->ls();
	//TTree *tree = (TTree *) f->Get("diphoton/fTree"); //->f TTree(diphoton/fTree) 	
	//tree->Print();
 	//DiPhoton2016BKG t(tree);
	//t.Loop();
	//return 0;

	//Chain trees 
	//trialClass t(Chainedtrees), chain.Add("file.root", 0) to calculate correct entries add 0 arg
	
	TChain chain("diphoton/fTree");
	chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-1000To2000_Pt-50_13TeV-sherpa.root", 0);
	chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-2000To4000_Pt-50_13TeV-sherpa.root", 0);
	chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-200To500_Pt-50_13TeV-sherpa.root", 0);
	chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-4000To6000_Pt-50_13TeV-sherpa.root", 0);	
	chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-500To1000_Pt-50_13TeV-sherpa.root", 0);
	chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-6000To8000_Pt-50_13TeV-sherpa.root",0);
	chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-60To200_Pt-50_13TeV-sherpa.root",0);
	chain.Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-8000To13000_Pt-50_13TeV-sherpa.root", 0);
	chain.ls();
	Int_t nevent = chain.GetEntries();
	cout << nevent;
        
        //TTree *tree = (TTree *) chain.Get("diphoton/fTree");
	chain.Print();
	//chain.MakeClass("DiPhoton16BKG");
	DiPhoton16BKG t;
        t.Loop();	
	
	//This doesn't work.
 	//TTree *tree = chain.GetTree();
	//Instantiate Class
	//DiPhoton2016BKG t(tree);
	//t.Loop();
	return 0;
	
}

