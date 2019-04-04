//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Feb 21 01:06:28 2019 by ROOT version 6.12/07
// from TChain diphoton/fTree/
//////////////////////////////////////////////////////////

#ifndef Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000_h
#define Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000 {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Long64_t        Event_run;
   Long64_t        Event_LS;
   Long64_t        Event_evnum;
   Long64_t        Event_processid;
   Long64_t        Event_bx;
   Long64_t        Event_orbit;
   Float_t         Event_ptHat;
   Float_t         Event_alphaqcd;
   Float_t         Event_alphaqed;
   Float_t         Event_qscale;
   Float_t         Event_x1;
   Float_t         Event_x2;
   Float_t         Event_pdf1;
   Float_t         Event_pdf2;
   Float_t         Event_weight0;
   Float_t         Event_weight;
   Float_t         Event_weightPuUp;
   Float_t         Event_weightPu;
   Float_t         Event_weightPuDown;
   Float_t         Event_weightLumi;
   Float_t         Event_weightAll;
   Int_t           Event_interactingParton1PdgId;
   Int_t           Event_interactingParton2PdgId;
   Int_t           Event_pdf_id1;
   Int_t           Event_pdf_id2;
   Int_t           Event_npv_true;
   Bool_t          Event_beamHaloIDLoose;
   Bool_t          Event_beamHaloIDTight;
   Bool_t          Event_beamHaloIDTight2015;
   Double_t        GenPhoton1_pt;
   Double_t        GenPhoton1_eta;
   Double_t        GenPhoton1_phi;
   Double_t        GenPhoton1_deltaR_match;
   Double_t        GenPhoton1_deltaR_matchDau;
   Double_t        GenPhoton1_ptDiff_match;
   Int_t           GenPhoton1_matchCategory;
   Int_t           GenPhoton1_matchType;
   Int_t           GenPhoton1_nPhotonMotherDaughters;
   Int_t           GenPhoton1_status;
   Int_t           GenPhoton1_motherStatus;
   Int_t           GenPhoton1_grandmotherStatus;
   Int_t           GenPhoton1_pdgId;
   Int_t           GenPhoton1_motherPdgId;
   Int_t           GenPhoton1_grandmotherPdgId;
   Double_t        GenPhoton2_pt;
   Double_t        GenPhoton2_eta;
   Double_t        GenPhoton2_phi;
   Double_t        GenPhoton2_deltaR_match;
   Double_t        GenPhoton2_deltaR_matchDau;
   Double_t        GenPhoton2_ptDiff_match;
   Int_t           GenPhoton2_matchCategory;
   Int_t           GenPhoton2_matchType;
   Int_t           GenPhoton2_nPhotonMotherDaughters;
   Int_t           GenPhoton2_status;
   Int_t           GenPhoton2_motherStatus;
   Int_t           GenPhoton2_grandmotherStatus;
   Int_t           GenPhoton2_pdgId;
   Int_t           GenPhoton2_motherPdgId;
   Int_t           GenPhoton2_grandmotherPdgId;
   Double_t        Gendiphoton_Minv;
   Double_t        Gendiphoton_qt;
   Double_t        Gendiphoton_deltaPhi;
   Double_t        Gendiphoton_deltaEta;
   Double_t        Gendiphoton_deltaR;
   Double_t        Gendiphoton_cosThetaStar;
   Double_t        Gendiphoton_cosThetaStar_old;
   Double_t        Gendiphoton_chiDiphoton;
   Bool_t          Gendiphoton_isEBEB;
   Bool_t          Gendiphoton_isEBEE;
   Bool_t          Gendiphoton_isEEEB;
   Bool_t          Gendiphoton_isEEEE;
   Bool_t          isGood;
   Int_t           nPV;

   // List of branches
   TBranch        *b_Event;   //!
   TBranch        *b_GenPhoton1;   //!
   TBranch        *b_GenPhoton2;   //!
   TBranch        *b_Gendiphoton;   //!
   TBranch        *b_isGood;   //!
   TBranch        *b_nPV;   //!

   Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000(TTree *tree=0);
   virtual ~Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000_cxx
Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000::Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000(TTree *tree) : fChain(0)
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {

#ifdef SINGLE_TREE
      // The following code should be used if you want this class to access
      // a single tree instead of a chain
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("Memory Directory");
      if (!f || !f->IsOpen()) {
         f = new TFile("Memory Directory");
      }
      f->GetObject("demo/fTree",tree);

#else // SINGLE_TREE

      // The following code should be used if you want this class to access a chain
      // of trees.
      TChain * chain = new TChain("demo/fTree","");

      //no need to add diphoton/fTree in the end
      //chain->Add("root://cmsxrootd.fnal.gov//store/user/cuperez/DiPhotonAnalysis/signal-2018/ADDGravToGG_NegInt-0_LambdaT-10000_M-2000To4000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-10000_M-2000To4000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190207_171204/0000/out_ADDGravToGG_NegInt-0_LambdaT-10000_M-2000To4000_TuneCP2_13TeV-pythia8_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1_numEvent100_1.root/diphoton/fTree");

      chain->Add("root://cmseos.fnal.gov//eos/uscms/store/user/cuperez/DiPhotonAnalysis/nPhotonAnalyzer/ADDGravToGG_NegInt-0_LambdaT-10000_M-4000To10000_TuneCP2_13TeV-pythia8/crab_ADDGravToGG_NegInt-0_LambdaT-10000_M-4000To10000_TuneCP2_13TeV-pythia8__Fall17_PU2017-v1__MINIAODSIM/190326_055543/0000/*root");
      tree = chain;
#endif // SINGLE_TREE

   }
   Init(tree);
}

Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000::~Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("Event", &Event_run, &b_Event);
   fChain->SetBranchAddress("GenPhoton1", &GenPhoton1_pt, &b_GenPhoton1);
   fChain->SetBranchAddress("GenPhoton2", &GenPhoton2_pt, &b_GenPhoton2);
   fChain->SetBranchAddress("Gendiphoton", &Gendiphoton_Minv, &b_Gendiphoton);
   fChain->SetBranchAddress("isGood", &isGood, &b_isGood);
   fChain->SetBranchAddress("nPV", &nPV, &b_nPV);
   Notify();
}

Bool_t Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000_cxx
