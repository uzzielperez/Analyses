#ifndef FAKEPREDICTION_HH
#define FAKEPREDICTION_HH

// needed to get default implementations from base class
#define ntupleAnalyzerBase_cxx

#include "ntupleAnalyzerBase.h"

// this is not defined in default MakeClass headers
// and so it needs a definition to avoid compilation errors
void ntupleAnalyzerBase::Loop() {};

class fakePrediction : public ntupleAnalyzerBase {

  bool isBarrelBarrel(double eta1, double eta2);
  bool isBarrelEndcap(double eta1, double eta2);

 public:
  using ntupleAnalyzerBase::ntupleAnalyzerBase;
  void Loop();
  void setIsMC(bool mc) { isMC = mc; };
  bool isMC;

};

#endif
