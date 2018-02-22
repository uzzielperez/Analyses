#define ClassGGJets_cxx
#include "ClassGGJets.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

#include <fstream>

void ClassGGJets::Loop()
{
//   In a ROOT session, you can do:
//      root> .L ClassGGJets.C
//      root> ClassGGJets t
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
	// fileout
	ofstream weightinfo;
	weightinfo.open("weightinfo.txt",ios::app);

	// counters
  	int nEBEB = 0;
  	int nEBEEorEEEB = 0;
  	int nPassisGood = 0;
        int Ntotal = 0;
	
	//histograms
        Long64_t nentries = fChain->GetEntriesFast();
	TH1D* diphotonMinv = new TH1D("diphotonMinv", "", 50, 0.,2000.);
	diphotonMinv->Sumw2();
	TH1D* photon1Pt  = new TH1D("photon1Pt", "", 50, 0.,2000.);
	TH1D* photon1Eta = new TH1D("photon1Eta", "", 80, -3,3);
	TH1D* photon1Phi = new TH1D("photon1Phi", "", 80, -3.5,3.5);
	TH1D* photon2Pt  = new TH1D("photon2Pt", "", 80, 0.,2000.);
	TH1D* photon2Eta = new TH1D("photon2Eta", "", 80, -3,3);
	TH1D* photon2Phi = new TH1D("photon2Phi", "", 80, -3.5,3.5);
	photon1Pt->Sumw2();
	photon1Eta->Sumw2();
	photon1Phi->Sumw2();
	photon2Pt->Sumw2();
	photon2Eta->Sumw2();
	photon2Phi->Sumw2();
	
	TH1D* diphotonMinvEBEB = new TH1D("diphotonMinvEBEB","",80,0.,2000.);
        TH1D* diphotonMinvEBEE = new TH1D("diphotonMinvEBEE","",80,0.,2000.);
        diphotonMinvEBEB->Sumw2();
        diphotonMinvEBEE->Sumw2();
        TH1D* photon1PtEBEB = new TH1D("photon1PtEBEB","",80,0.,2000.);
        TH1D* photon1PtEBEE = new TH1D("photon1PtEBEE","",80,0.,2000.);
        photon1PtEBEB->Sumw2();
        photon1PtEBEE->Sumw2();
        TH1D* photon2PtEBEB = new TH1D("photon2PtEBEB","",80,0.,2000.);
 	TH1D* photon2PtEBEE = new TH1D("photon2PtEBEE","",80,0.,2000.);
 	photon2PtEBEB->Sumw2();
 	photon2PtEBEE->Sumw2();

	// Detector Eta and Phi
	TH1D* photon1detEta = new TH1D("photon1detEta", "", 80, -3,3);
	TH1D* photon1detPhi = new TH1D("photon1detPhi", "", 80, -3.5,3.5);
	TH1D* photon2detEta = new TH1D("photon2detEta", "", 80, -3,3);
	TH1D* photon2detPhi = new TH1D("photon2detPhi", "", 80, -3.5,3.5);
	photon1detEta->Sumw2();
	photon1detPhi->Sumw2();
	photon2detEta->Sumw2();
	photon2detPhi->Sumw2();
	
   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
      Ntotal++; 
	//float weight = 0;
	//Weight Correction
	weight = Event_weightAll;
	if (jentry > 3606476 && jentry < 4606396){
		 cout << "Changing mass bin Event_weight" << endl; 
		 weight = Event_weightAll * 1.446113552;
	}

//    if (jentry%10000 == 0){
//	 cout << "Number of processed events: " << jentry << "; LumiWts: " << Event_weightLumi << "; Weight_All: " << Event_weightAll << "; Weight: " << Event_weight <<  endl;  
//  	 weightinfo << jentry <<" LumiWeight: " << Event_weightLumi << "; WeightALL: "<< Event_weightAll << "; Weight: " << Event_weight <<  endl; 
//      }
     if(jentry%10000 == 0) cout << "Number of processed events: " << jentry << endl;
	     
      if (isGood){ 
        nPassisGood++;
        diphotonMinv->Fill(Diphoton_Minv, weight);
	photon1Pt->Fill(Photon1_pt, weight);
	photon1Eta->Fill(Photon1_eta, weight);
	photon1Phi->Fill(Photon1_phi, weight);
	photon2Pt->Fill(Photon2_pt, weight);
	photon2Eta->Fill(Photon2_eta, weight);
	photon2Phi->Fill(Photon2_phi, weight);
	
	photon1detEta->Fill(Photon1_scEta, weight);
	photon1detPhi->Fill(Photon1_scPhi, weight); 
	photon2detEta->Fill(Photon2_scEta, weight);
	photon2detPhi->Fill(Photon2_scPhi, weight); 

	//EBEB
	if (fabs(Photon1_scEta) < 1.4442 && fabs(Photon2_scEta) < 1.4442) {
                nEBEB++;
		diphotonMinvEBEB->Fill(Diphoton_Minv, weight);
		photon1PtEBEB->Fill(Photon1_pt, weight);
		photon2PtEBEB->Fill(Photon2_pt, weight);
	}//end EBEB
	
	// EBEE or EEBE 
	if ((fabs(Photon1_scEta) < 1.4442 && 1.566 < fabs(Photon2_scEta) && fabs(Photon2_scEta) < 2.5) ||
	(fabs(Photon2_scEta) < 1.4442 && 1.566 < fabs(Photon1_scEta) && fabs(Photon1_scEta) < 2.5) ) {
     		nEBEEorEEEB++;
		diphotonMinvEBEE->Fill(Diphoton_Minv, weight);
		photon1PtEBEE->Fill(Photon1_pt, weight);
		photon2PtEBEE->Fill(Photon2_pt, weight);
	}//end EBEE or EEBE
	}//end isGood

   }//end loop over events

  cout << endl;
  cout << "Total entries             : " << nentries << endl;
  cout << " Passed isGood cut        : " << nPassisGood << endl;
  cout << "  and in EBEB             : " << nEBEB << endl;
  cout << "  and in EBEE or EEEB     : " << nEBEEorEEEB << endl;
  cout << endl;

  TFile file_out("WREGGJets_histograms.root","RECREATE");

	diphotonMinv->Write();
	photon1Pt->Write();
	photon1Eta->Write();
	photon1Phi->Write();
	photon2Pt->Write();
	photon2Eta->Write();
	photon2Phi->Write();

	diphotonMinvEBEB->Write();
        diphotonMinvEBEE->Write();

        photon1PtEBEB->Write();
        photon2PtEBEB->Write();
        photon1PtEBEE->Write();
        photon2PtEBEE->Write();

	photon1detEta->Write();
	photon1detPhi->Write();
	photon2detEta->Write();
	photon2detPhi->Write();

	weightinfo.close();		
}//end Class
