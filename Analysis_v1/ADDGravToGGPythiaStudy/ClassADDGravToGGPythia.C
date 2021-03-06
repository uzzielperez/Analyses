#define ClassADDGravToGGPythia_cxx
#include "ClassADDGravToGGPythia.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

using namespace std; 
//bool etaCut = false;
bool etaCut = true;

void ClassADDGravToGGPythia::Loop()
{
//   In a ROOT session, you can do:
//      root> .L ClassADDGravToGGPythia.C
//      root> ClassADDGravToGGPythia t
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
	int netaCut     = 0;
   Long64_t nentries = fChain->GetEntriesFast();

	//histograms
	TH1D* gendiphotonMinv = new TH1D("gendiphotonMinv", "", 40, 0., 4000.);
	TH1D* genphoton1Pt    = new TH1D("genphoton1Pt", "", 40, 0., 4000.);
	TH1D* genphoton2Pt    = new TH1D("genphoton2Pt", "", 40, 0., 4000.);
	TH1D* genphoton1Eta   = new TH1D("genphoton1Eta", "", 80, -3.0, 3.0);
	TH1D* genphoton2Eta   = new TH1D("genphoton2Eta", "", 80, -3.0, 3.0);
	TH1D* genphoton1Phi   = new TH1D("genphoton1Phi", "", 80, -3.5, 3.5);
	TH1D* genphoton2Phi   = new TH1D("genphoton2Phi", "", 80, -3.5, 3.5);

	gendiphotonMinv->Sumw2();
	genphoton1Pt->Sumw2();
	genphoton2Pt->Sumw2();
	genphoton1Eta->Sumw2();
	genphoton2Eta->Sumw2();
	genphoton1Phi->Sumw2();
	genphoton2Phi->Sumw2();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
      Ntotal++; 
      //double weight = 1.00; 
      //double weight = 0.1228*1000.0/10000.0; //xsec is 0.1246 pb, please check this!
      //double weight = 2.092*1000.0/10000;
	
	//double weight = 0.1229*1000.0/10000; // LambdaT = 4000 GeV
//	 double weight = 0.1133*1000.0/10000; //	LambdaT = 5000 GeV
	//double weight = 0.1121*1000.0/10000; // LambdaT = 7000 GeV
	double weight = 0.1127*1000.0/10000; // LambdaT = 10000 GeV

	if(jentry%10000 == 0) cout << "Number of processed events: " << jentry << endl;
	if (GenDiPhoton_Minv > 500.){ // && GenDiPhoton_Minv < 4000.){
		nDiphMinv++;
	if (GenPhoton1_pt >75. && GenPhoton2_pt > 75.){
		if (etaCut){
		if (abs(GenPhoton1_eta) < 2.8 && abs(GenPhoton2_eta) < 2.8){	
			netaCut++;
			gendiphotonMinv->Fill(GenDiPhoton_Minv, weight);
			genphoton1Pt->Fill(GenPhoton1_pt, weight);
			genphoton2Pt->Fill(GenPhoton2_pt, weight);
			genphoton1Eta->Fill(GenPhoton1_eta, weight); 
			genphoton2Eta->Fill(GenPhoton2_eta, weight); 
			genphoton1Phi->Fill(GenPhoton1_phi, weight);
			genphoton2Phi->Fill(GenPhoton2_phi, weight);	
		}//etacut
		}//end etacut
		else{
			gendiphotonMinv->Fill(GenDiPhoton_Minv, weight);
			genphoton1Pt->Fill(GenPhoton1_pt, weight);
			genphoton2Pt->Fill(GenPhoton2_pt, weight);
			genphoton1Eta->Fill(GenPhoton1_eta, weight); 
			genphoton2Eta->Fill(GenPhoton2_eta, weight); 
			genphoton1Phi->Fill(GenPhoton1_phi, weight);
			genphoton2Phi->Fill(GenPhoton2_phi, weight);
		}//no etacut 
	}//ptCut75
	}//GenDiphMinv>500
   }//end of event Loop 

	cout << endl;
	cout << "Total entries            : " << Ntotal    << " " << nentries << endl;
	cout << "Passed DiphMinv cut      : " << nDiphMinv << endl;
        cout << "Passed etaCut            : " << netaCut   << endl;
	cout << endl;
		
	if (etaCut){

		 //noMD   
		 
		// TFile file_out("TestADDG2gg_LambdaT-4000_M-500-pythia8.root", "RECREATE");
		 //TFile file_out("TestADDG2gg_LambdaT-5000_M-500-pythia8.root", "RECREATE");
//		 TFile file_out("TestADDG2gg_LambdaT-7000_M-500-pythia8.root", "RECREATE");
		 TFile file_out("TestADDG2gg_LambdaT-10000_M-500-pythia8.root", "RECREATE");
//		 
		//wMD 	
		 
 		 //TFile file_out("Test_MD-1128-ADDG2gg_LambdaT-4000_M-500-pythia8.root", "RECREATE");
 		 //TFile file_out("Test_MD-1410-ADDG2gg_LambdaT-4000_M-500-pythia8.root", "RECREATE");
 		 //TFile file_out("Test_MD-1974-ADDG2gg_LambdaT-4000_M-500-pythia8.root", "RECREATE");
 		 //TFile file_out("Test_MD-2820-ADDG2gg_LambdaT-4000_M-500-pythia8.root", "RECREATE");
 //	
		//Write histograms to File
		 gendiphotonMinv->Write();
		 genphoton1Pt->Write();
		 genphoton2Pt->Write();
		 genphoton1Eta->Write();
		 genphoton2Eta->Write();
		 genphoton1Phi->Write();
		 genphoton2Phi->Write();
        }//w/etacut
	if (!etaCut){
		 cout << "noetacut" << endl;  
		 TFile file_out("wADDGravToGGPythia_histo_M-200-4000.root", "RECREATE");	
		 //TFile file_out("ADDGravToGGPythia_histo_M-200-4000.root", "RECREATE");	
		 //Write histograms to File
		 gendiphotonMinv->Write();
		 genphoton1Pt->Write();
		 genphoton2Pt->Write();
		 genphoton1Eta->Write();
		 genphoton2Eta->Write();
		 genphoton1Phi->Write();
		 genphoton2Phi->Write();
	}//noetacutWrite
}
