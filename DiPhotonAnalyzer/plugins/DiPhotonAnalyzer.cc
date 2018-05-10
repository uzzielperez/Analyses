// -*- C++ -*-
//
// Package:    Analyses/DiPhotonAnalyzer
// Class:      DiPhotonAnalyzer
// 
/**\class DiPhotonAnalyzer DiPhotonAnalyzer.cc Analyses/DiPhotonAnalyzer/plugins/DiPhotonAnalyzer.cc

 Description: GEN only analyzer (Based on Andrew's RSG Analyzer)

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cilicia Uzziel Perez
//         Created:  Tue, 08 May 2018 00:41:08 GMT
//
//

using namespace std;

// system include files
#include <memory>
#include <iostream>
#include <fstream>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// Misc.
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/Common/interface/Handle.h"

//TFile Service
#include "TTree.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

//for MC
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

//Common Classes 
//To implement later 


//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class DiPhotonAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit DiPhotonAnalyzer(const edm::ParameterSet&);
      ~DiPhotonAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      
      // ----------member data ---------------------------
    // genParticle token
   //edm::EDGetTokenT<edm::View<reco::GenParticle>> genParticlesToken_;
   edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;
   edm::InputTag genParticles_;

   TTree *fgenTree;
   //Could be in ExoDiPhotons namespace (Common Classes). Implement here fully for the first time
   struct eventInfo_t {
      Long64_t run;
      Long64_t LS;
      Long64_t evnum;
     };
   eventInfo_t fEventInfo; //ExoDiPhotons::eventInfo_t fEventInfo;
   
    struct genPhotonInfo_t{
      double pt; 
      double eta; 
      double phi;
    }; 

    genPhotonInfo_t fSignalPhoton1;
    genPhotonInfo_t fSignalPhoton2;
    
    double fGravitonMass; 
    
    struct genDiPhotonInfo_t{
      //kinematics 
      double Minv; 
      double qt; 
    }; 
    
    genDiPhotonInfo_t fSignalDiPhoton;    
};

// constants, enums and typedefs
// static data member definitions

// constructors and destructor
DiPhotonAnalyzer::DiPhotonAnalyzer(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
   usesResource("TFileService");
   edm::Service<TFileService> fs;
  
   fgenTree = fs->make<TTree>("fgenTree","GENDiphotonTree");
   
   fgenTree->Branch("genPhoton1", &fSignalPhoton1, "pt/D:eta:phi");
   fgenTree->Branch("genPhoton2", &fSignalPhoton2, "pt/D:eta:phi");
   fgenTree->Branch("genDiPhoton", &fSignalDiPhoton, "Minv/D:qt");
   //fgenTree->Branch("Graviton", &fGravitonMass, "Mass/D");

   //genParticle token
   //genParticlesToken_ = mayConsume<edm::View<reco::GenParticle>>(iConfig.getParameter<edm::InputTag>("genParticles"));
   genParticlesToken_ = consumes<vector<reco::GenParticle>>(iConfig.getParameter<edm::InputTag>("genParticles"));
   //genParticlesToken_ = mayConsume<edm::View<reco::GenParticle>>(iConfig.getParameter<edm::InputTag>(""));
}


DiPhotonAnalyzer::~DiPhotonAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
DiPhotonAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace std;

   //Init available in ExoDiphotons but do manual initialization here
  fEventInfo.run = -99999.99;
  fEventInfo.LS = -99999.99;
  fEventInfo.evnum = -99999.99;

  //An example of accessing GenParticles from the event. reco::GenParticleCollection is typedef for vector<reco::GenParticle>
  //Handle<reco::GenParticleCollection> genParticles;
  //iEvent.getByLabel("genParticles", genParticles);
  //Handle<edm::View<reco::GenParticle> > genParticles;
  edm::Handle<vector<reco::GenParticle> > genParticles;
  iEvent.getByToken(genParticlesToken_,genParticles);
  //Handle<reco::GenParticle> genParticles;
  //iEvent.getByLabel("genParticles", genParticles);

  if(!genParticles.isValid()) {
         cout << "No Gen Particles collection!" << endl;
         return;
  }

  fSignalPhoton1.pt = -99999.99;
  fSignalPhoton1.eta = -99999.99;
  fSignalPhoton1.phi = -99999.99;

  fSignalPhoton2.pt = -99999.99;
  fSignalPhoton2.eta = -99999.99;
  fSignalPhoton2.phi = -99999.99;

  fSignalDiPhoton.Minv = -99999.99;
  fSignalDiPhoton.qt = -99999.99;

  const reco::GenParticle *signalPhoton1 = NULL;
  const reco::GenParticle *signalPhoton2 = NULL;
  
  //store photon information
  //vector<genPhotonInfo_t> genPhoton_obj;
  //vector<genDiPhotonInfo_t> genDiPhoton_obj;

//Loop over genParticle Collection

for (reco::GenParticleCollection::const_iterator genParticle = genParticles->begin(); genParticle != genParticles->end(); ++genParticle){
//for (reco::GenParticle::const_iterator genParticle = genParticles->begin(); genParticle != genParticles->end(); ++genParticle){ 
//for (size_t i=0; i<genParticles->size(); i++){
  // Identify the status 1 particles (i.e. no further decays) photons
  // Came from hard scattering photons (status3) 
  //edm::Ptr<reco::GenParticle> gen = genParticles->ptrAt(i);
  //const reco::GenParticle::const_iterator gen = genParticle;


  if (genParticle->status()==1 && genParticle->pdgId()==22){
    if(genParticle->numberOfMothers()>0){
        if(genParticle->mother()->status()==3 && genParticle->mother()->pdgId()==22){
        // LATER further require that this status 3 photon came from Graviton
        //Some check
        cout << "MC particle: Status = " << genParticle->status() 
             << "; pdg id = " << genParticle->pdgId()
             << "; pt, eta, phi = " << genParticle->pt() 
             << ", " << genParticle->eta() 
             << ", " << genParticle->phi() 
             << endl;

        if(!signalPhoton1){
          signalPhoton1 = &(*genParticle);
        }
        else {
          signalPhoton2 = &(*genParticle);
        }

 //
 //  if (gen->status()==1 && gen->pdgId()==22){
 //    if(gen->numberOfMothers()>0){
 //        if(gen->mother()->status()==3 && gen->mother()->pdgId()==22){
 //        // LATER further require that this status 3 photon came from Graviton
 //        //Some check
 //        cout << "MC particle: Status = " << gen->status() 
 //             << "; pdg id = " << gen->pdgId()
 //             << "; pt, eta, phi = " << gen->pt() << ", " << gen->eta() << ", " << gen->phi() << endl;
 //
 //        if(!signalPhoton1){
 //          signalPhoton1 = &(*gen);
 //        }
 //        else {
 //          signalPhoton2 = &(*gen);
 //        }
       }//end of check for hardscattering origin, mother status 3
    }//end of check for numberOfMothers>0
  }//end status 1 check
}//end gen particle loop
 
  //reorder signalPhotons by pt
   if(signalPhoton2->pt()>signalPhoton1->pt()) {
     const reco::GenParticle *tempSignalPhoton = signalPhoton1;
     signalPhoton1 = signalPhoton2;
     signalPhoton2 = tempSignalPhoton;
   }

   //UPDATING STRUCT INFORMATION
  
   if(signalPhoton1){
      fSignalPhoton1.pt = signalPhoton1->pt();
      fSignalPhoton1.eta = signalPhoton1->eta();
      fSignalPhoton1.phi = signalPhoton1->phi();
    }
  
   
   if(signalPhoton2){
      fSignalPhoton2.pt = signalPhoton2->pt();
      fSignalPhoton2.eta = signalPhoton2->eta();
      fSignalPhoton2.phi = signalPhoton2->phi();
    }

   //Fill the tree Branches 
   fgenTree->Fill();
   

#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
DiPhotonAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DiPhotonAnalyzer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DiPhotonAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DiPhotonAnalyzer);
