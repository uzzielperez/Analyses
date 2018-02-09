#define DiPhoton16BKG_cxx
#include "DiPhoton16BKG.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <iostream>

using namespace std;
void DiPhoton16BKG::Loop()
{
//   In a ROOT session, you can do:
//      root> .L DiPhoton16BKG.C
//      root> DiPhoton16BKG t
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
   
   //histograms
	TH1D* diphotonMinv = new TH1D("diphotonMinv", "", 80, 0.,1600.);
	diphotonMinv->Sumw2();
	TH1D* photon1Pt  = new TH1D("photon1Pt", "", 80, 0.,1600.);
	TH1D* photon1Eta = new TH1D("photon1Eta", "", 80, 0.,1600.);
	TH1D* photon1Phi = new TH1D("photon1Phi", "", 80, 0.,1600.);
	TH1D* photon2Pt  = new TH1D("photon2Pt", "", 80, 0.,1600.);
	TH1D* photon2Eta = new TH1D("photon2Eta", "", 80, 0.,1600.);
	TH1D* photon2Phi = new TH1D("photon2Phi", "", 80, 0.,1600.);
	photon1Pt->Sumw2();
	photon1Eta->Sumw2();
	photon1Phi->Sumw2();
	photon2Pt->Sumw2();
	photon2Eta->Sumw2();
	photon2Phi->Sumw2();
		
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
      if (jentry%10000 == 0) cout << "Number of processed events: "<< jentry << endl;

	diphotonMinv->Fill(Diphoton_Minv, Event_weightAll);
	photon1Pt->Fill(Photon1_pt, Event_weightAll);
	photon1Eta->Fill(Photon1_eta, Event_weightAll);
	photon1Phi->Fill(Photon1_phi, Event_weightAll);
	photon2Pt->Fill(Photon2_pt, Event_weightAll);
	photon2Eta->Fill(Photon2_eta, Event_weightAll);
	photon2Phi->Fill(Photon2_phi, Event_weightAll);
		
  }//end of loop over events
	
	TFile file_out("diphoton16bkg_histograms.root", "RECREATE");

	diphotonMinv->Write();
	photon1Pt->Write();
	photon1Eta->Write();
	photon1Phi->Write();
	photon2Pt->Write();
	photon2Eta->Write();
	photon2Phi->Write();
	
	file_out.ls();
	file_out.Close();

}//end of Class loop
