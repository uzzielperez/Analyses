//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Fri Oct 19 02:28:28 2018 by ROOT version 6.06/01
// from TChain demo/fgenTree/
//////////////////////////////////////////////////////////

#ifndef ClassUnparticles_h
#define ClassUnparticles_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class ClassUnparticles {
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
   Double_t        GenDiPhoton_Minv;
   Double_t        GenDiPhoton_qt;
   Double_t        GenDiPhoton_deltaPhi;
   Double_t        GenDiPhoton_deltaEta;
   Double_t        GenDiPhoton_deltaR;
   Double_t        GenDiPhoton_cosThetaStar;
   Double_t        GenDiPhoton_cosThetaStar_old;
   Bool_t          GenDiPhoton_isEBEB;
   Bool_t          GenDiPhoton_isEBEE;
   Bool_t          GenDiPhoton_isEEEB;
   Bool_t          GenDiPhoton_isEEEE;
   Bool_t          isGood;
   Int_t           nPV;

   // List of branches
   TBranch        *b_Event;   //!
   TBranch        *b_GenPhoton1;   //!
   TBranch        *b_GenPhoton2;   //!
   TBranch        *b_GenDiPhoton;   //!
   TBranch        *b_isGood;   //!
   TBranch        *b_nPV;   //!

   ClassUnparticles(TTree *tree=0);
   virtual ~ClassUnparticles();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef ClassUnparticles_cxx
ClassUnparticles::ClassUnparticles(TTree *tree) : fChain(0)
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
      f->GetObject("demo/fgenTree",tree);

#else // SINGLE_TREE

      // The following code should be used if you want this class to access a chain
      // of trees.
      TChain * chain = new TChain("demo/fgenTree","");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1250p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1250p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1750p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1750p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp2000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp2000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp2500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp2500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp3000p0_M_2000_py_GEN.root/demo/fgenTree");
      chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp3000p0_M_500-2000_py_GEN.root/demo/fgenTree");

      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp3500p0_M_2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp3500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp4000p0_M_2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp4000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp4500p0_M_2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp4500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp5500p0_M_2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp5500p0_M_500-2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p4Unp1500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p4Unp1500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p4Unp2000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p4Unp2000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p4Unp2500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p4Unp2500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p4Unp3000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p4Unp3000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p4Unp4000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p4Unp4000p0_M_500-2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p7Unp1500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p7Unp1500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p7Unp1750p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p7Unp1750p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p7Unp2000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p7Unp2000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p7Unp2500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p7Unp2500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p7Unp3000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p7Unp3000p0_M_500-2000_py_GEN.root/demo/fgenTree");


      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp1750p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp2000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp2500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp3000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp3500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp4000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp4500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp1750p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp2000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp2500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp3000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp3500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp4000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp4500p0_M_500-2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p2Unp2000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p2Unp2500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p2Unp3000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p2Unp3500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p2Unp4000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p2Unp2000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p2Unp2500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p2Unp3000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p2Unp3500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p2Unp4000p0_M_500-2000_py_GEN.root/demo/fgenTree");

      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp1500p0_M_2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp1500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp2000p0_M_2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp2000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp2500p0_M_2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp2500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp3000p0_M_2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp3000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp3500p0_M_2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp3500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp4000p0_M_2000_py_GEN.root/demo/fgenTree");
      // chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp4000p0_M_500-2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p6Unp1500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p6Unp1500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p6Unp2000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p6Unp2000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p6Unp2500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p6Unp2500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p6Unp3000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p6Unp3000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p6Unp3500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p6Unp3500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p6Unp4000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p6Unp4000p0_M_500-2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p01Unp2500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p01Unp3000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cu//perez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p01Unp3500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p01Unp4000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p01Unp4500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p01Unp2500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p01Unp3000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p01Unp3500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p01Unp4000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p01Unp4500p0_M_500-2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp2500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp3000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp3500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp4000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp4500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp5000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp2500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp3000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp3500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp4000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp4500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp5000p0_M_500-2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp1000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp1000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp1250p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp1250p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp1750p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp1750p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp2250p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp2250p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp2500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp2500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp2750p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp2750p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp2000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp2000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp1500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp1500p0_M_500-2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp2500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp2500p0_M_500-2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestTestSM_M-500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp3000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp3000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp4000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp4000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp6000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p8Unp6000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestTestSM_M-2000_py_GEN.root/demo/fgenTree");

        //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp1000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp1000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp1250p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp1250p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp1500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp1500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp1750p0_M_2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp1750p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp2000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p5Unp2000p0_M_500-2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1000p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1250p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1250p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1500p0_M_2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1500p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1750p0_M_2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp1750p0_M_500-2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp2000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p9Unp2000p0_M_500-2000_py_GEN.root/demo/fgenTree");

      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp2000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp1500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp1250p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp1750p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p1Unp1000p0_M_2000_py_GEN.root/demo/fgenTree");
      //
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp2000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp1250p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp1500p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp1000p0_M_2000_py_GEN.root/demo/fgenTree");
      //chain->Add("/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out/TestSTest1p3Unp1750p0_M_2000_py_GEN.root/demo/fgenTree");

      tree = chain;
#endif // SINGLE_TREE

   }
   Init(tree);
}

ClassUnparticles::~ClassUnparticles()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t ClassUnparticles::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t ClassUnparticles::LoadTree(Long64_t entry)
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

void ClassUnparticles::Init(TTree *tree)
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
   fChain->SetBranchAddress("GenDiPhoton", &GenDiPhoton_Minv, &b_GenDiPhoton);
   fChain->SetBranchAddress("isGood", &isGood, &b_isGood);
   fChain->SetBranchAddress("nPV", &nPV, &b_nPV);
   Notify();
}

Bool_t ClassUnparticles::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void ClassUnparticles::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t ClassUnparticles::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef ClassUnparticles_cxx
