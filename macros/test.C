#include "DiPhoton16BKG.C"
#include <iostream>

using namespace std;

int test(){
	//For one file:	
	TFile *f = TFile::Open("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-8000To13000_Pt-50_13TeV-sherpa.root");
        f->ls();
	TTree *tree = (TTree *) f->Get("diphoton/fTree"); //->f TTree(diphoton/fTree) 	
	//tree->Print();
 	//DiPhoton16BKG t(tree);
	//t.Loop();
	return 0;
}

