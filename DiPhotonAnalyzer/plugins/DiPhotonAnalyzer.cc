// -*- C++ -*-
//
// Package:    Analyses/DiPhotonAnalyzer
// Class:      DiPhotonAnalyzer
// 
/**\class DiPhotonAnalyzer DiPhotonAnalyzer.cc Analyses/DiPhotonAnalyzer/plugins/DiPhotonAnalyzer.cc

 Description: Local DiPhoton Analyzer

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Uzziel Perez
//         Created:  Tue, 08 May 2018 00:41:08 GMT
//
//


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

//ROOT header files 
#include "TMath.h"
#include "TLorentzVector.h"

// Common Classes
//#include "Analyses/CommonClasses/interface/DiPhotonInfo.h"

// for TFileService
#include "TTree.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

// for genParticle
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

// for photons
#include "DataFormats/PatCandidates/interface/Photon.h"

// for deltaR
#include "DataFormats/Math/interface/deltaR.h"

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
     edm::EDGetToken photonsMiniAODToken_;
     edm::EDGetToken genParticlesMiniAODToken_; 
     TTree *fPythiaGenTree; 
     struct eventInfo_t{
            Long64_t run; 
            Long64_t LS; 
            Long64_t evnum;
      };
      eventInfo_t fEventInfo;

      struct genPhotonInfo_t{
             double pt; 
             double eta; 
             double phi; 
       };

   //Instantiate the different photon structs to store photoninfo
      genPhotonInfo_t photonInfo;
      genPhotonInfo_t iGenPhoton_info[2]; //one for each photon


     //static bool comparePhotonsByPt(const edm::Ptr<pat::Photon> photon1, const edm::Ptr<pat::Photon> photon2){
     static bool compareGenPhotonsByPt(const edm::Ptr<reco::GenParticle> photon1, const edm::Ptr<reco::GenParticle> photon2){
            return(photon1->pt()<=photon2->pt());
      }
      
      struct photonPtComparer{
        bool operator()(const genPhotonInfo_t& x, const genPhotonInfo_t& y)const{
             return x.pt<y.pt; //for sorting in descending order
              }
      }; 
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
DiPhotonAnalyzer::DiPhotonAnalyzer(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
   usesResource("TFileService");
   edm::Service<TFileService> fs;
   
   //Tree Name
   fPythiaGenTree = fs->make<TTree>("fTree","DiPhotonTree");
   
    //Branches
    fPythiaGenTree->Branch("Event",  &fEventInfo, "run/L:LS:evnum");
    fPythiaGenTree->Branch("Photon1", &iGenPhoton_info[0], "pt/D:eta:phi");
    fPythiaGenTree->Branch("Photon2", &iGenPhoton_info[1], "pt/D:eta:phi");
    //fPythiaGenTree->Branch("Diphoton", &diphoton_info, "Minv/D");
    photonsMiniAODToken_ = mayConsume<edm::View<pat::Photon>>(edm::InputTag("slimmedPhotons"));  
    //genParticlesMiniAODToken_ = mayConsume<edm::View<reco::GenParticle> >(iConfig.getParameter<edm::InputTag>("genParticlesMiniAOD")); 
    genParticlesMiniAODToken_ = mayConsume<reco::GenParticle>(iConfig.getParameter<edm::InputTag>("genParticlesMiniAOD")); 
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

   //Initialize leaf values
   fEventInfo.run = -99999.99;
   fEventInfo.LS  = -99999.99;
   fEventInfo.evnum = -99999.99;
   
   for(int k = 0; k<2; k++){
   iGenPhoton_info[k] = (genPhotonInfo_t){-99999.99, -99999.99, -99999.99};
   }
  
     //Print output to file:
   ofstream cout("output.txt", ios::app);

   //Print out event information 
  cout << "Run: " << iEvent.id().run() << ", LS: " << iEvent.id().luminosityBlock() 
    << ", Event: " << iEvent.id().event() << endl;
  
  //Store event info
  fEventInfo.run = iEvent.id().run();
  fEventInfo.LS = iEvent.id().luminosityBlock();
  fEventInfo.evnum = iEvent.id().event();

  edm::Handle<edm::View<pat::Photon>> photons;   // To get PAT photon collection
  //edm::Handle<edm::View<reco::GenParticle>> genPhotons;
  edm::Handle<reco::GenParticle> genPhotons; 

  iEvent.getByToken(genParticlesMiniAODToken_,genPhotons); 

  //DiPhoton vec
  vector<genPhotonInfo_t> DiPhoton_vec;
  vector<edm::Ptr<pat::Photon>> photon_vec; 
  vector<edm::Ptr<reco::GenParticle>> genPhoton_vec;

  //Loop over each photon in each event
  for (size_t i = 0; i<genPhotons->size(); i++){
      const auto genpho = genPhotons->ptrAt(i);
      //print out all Photon information
      cout << "Photon: " << "pt = " << genpho->pt()
                         << "; eta = " << genpho->eta()
                         << "; phi = " << genpho->phi()
                         << endl;

      //store all photons in photon_vec
      genPhoton_vec.push_back(genpho);

  }//end of photon loop 
  
  //Sort Here. See photonPtComparer() 
  sort(genPhoton_vec.rbegin(), genPhoton_vec.rend(), compareGenPhotonsByPt);

  //vector<edm::Ptr<pat::Photon>>::iterator iter;
  vector<edm::Ptr<reco::GenParticle>>::iterator iter;
  int jcounter = 0;
  //loop over photon_vec 
  for (iter = genPhoton_vec.begin(); iter != genPhoton_vec.end(); ++iter){
      cout << "genPhotonobjects_pt: " << (*iter)->pt() << endl;
      if (jcounter<2){
        iGenPhoton_info[jcounter] = (genPhotonInfo_t){(*iter)->pt(),
                                                 (*iter)->eta(),
                                                 (*iter)->phi()};
        jcounter = jcounter + 1;

      }//end iPhoton filling
  }//end loop over photon_vec
 
      //Check if there is more than one photon
if (photons->size()>1){
 
  fPythiaGenTree->Fill();

  //*CHECK INFORMATION BEING STORED IN THE STRUCTS*
  cout<< "****Check stored info****"<<endl;
  cout<< "Photon1:: "<< "pt: " << iGenPhoton_info[0].pt
                     << "; eta: " << iGenPhoton_info[0].eta
                     << "; phi: " << iGenPhoton_info[0].phi
                     << endl;
  cout<< "Photon2:: "<< "pt: " << iGenPhoton_info[1].pt
                     << "; eta: " << iGenPhoton_info[1].eta
                     << "; phi: " << iGenPhoton_info[1].phi
                     << endl;
  //cout<< "Diphoton:: "<< "Minv: " << diphoton_info.Minv 
  //                  << endl;
}//end condition for two photons
cout << "======================================RUN ENDS==================================" <<endl;


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
