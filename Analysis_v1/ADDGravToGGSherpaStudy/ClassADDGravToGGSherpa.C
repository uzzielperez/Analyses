#define ClassADDGravToGGSherpa_cxx
#include "ClassADDGravToGGSherpa.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void ClassADDGravToGGSherpa::Loop()
{
//   In a ROOT session, you can do:
//      root> .L ClassADDGravToGGSherpa.C
//      root> ClassADDGravToGGSherpa t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;
	//counters
	int Ntotal      = 0;
	int nDiphMinv   = 0;
   Long64_t nentries = fChain->GetEntriesFast();

	//histograms
	TH1D* gendiphotonMinv = new TH1D("gendiphotonMinv", "", 40, 0., 4000.);
	TH1D* genphoton1Pt    = new TH1D("genphoton1Pt", "", 40, 0., 4000.);
	TH1D* genphoton2Pt    = new TH1D("genphoton2Pt", "", 40, 0., 4000.);
	TH1D* genphoton1Phi   = new TH1D("genphoton1Phi", "", 80, -3.5, 3.5);
	TH1D* genphoton2Phi   = new TH1D("genphoton2Phi", "", 80, -3.5, 3.5);

	gendiphotonMinv->Sumw2();
	genphoton1Pt->Sumw2();
	genphoton2Pt->Sumw2();
	genphoton1Phi->Sumw2();
	genphoton2Phi->Sumw2();
		
   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
      Ntotal++;
      double weight   = Event_weightAll;

	if(jentry%10000 == 0) cout << "Number of processed events: " << jentry << endl;
	if (isGood){
	if (GenDiphoton_Minv > 500){
		nDiphMinv++;
	if (GenPhoton1_pt >75 && GenPhoton2_pt > 75){
		gendiphotonMinv->Fill(GenDiphoton_Minv, weight);
		genphoton1Pt->Fill(GenPhoton1_pt, weight);
		genphoton2Pt->Fill(GenPhoton2_pt, weight);
		genphoton1Phi->Fill(GenPhoton1_phi, weight);
		genphoton2Phi->Fill(GenPhoton2_phi, weight);
	}//ptCut75
	}//GenDiphMinv>500
	}//isGood
   }//fLoop
	
	cout << endl;
	cout << "Total entries            : " << Ntotal    << " " << nentries << endl;
	cout << "Passed DiphMinv cut      : " << nDiphMinv << endl;
        cout << endl;

	TFile file_out("ADDGravToGGSherpa_histo_M-200-4000.root","RECREATE");
	
	//Write histograms to File
	gendiphotonMinv->Write();
	genphoton1Pt->Write();
	genphoton2Pt->Write();
	genphoton1Phi->Write();
	genphoton2Phi->Write();

}//fClass
