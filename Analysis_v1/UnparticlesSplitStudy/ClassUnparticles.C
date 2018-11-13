#define ClassUnparticles_cxx
#include "ClassUnparticles.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <iostream>
#include <fstream>

void ClassUnparticles::Loop()
{
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   //counters
 	int Ntotal      = 0;
 	int nDiphMinv   = 0;
 	int netaCut     = 0;
  int isEBEB = 0;
	int numevents   = 10000;
  //histograms
  TH1D* gendiphotonMinv = new TH1D("gendiphotonMinv", "", 100, 500., 13000.);// 100, 0, 10000
  TH1D* genphoton1Pt    = new TH1D("genphoton1Pt", "", 1000, 0., 7000.);//
  TH1D* genphoton2Pt    = new TH1D("genphoton2Pt", "", 1000, 0., 7000.);
  TH1D* genphoton1Eta   = new TH1D("genphoton1Eta", "", 80, -3.0, 3.0);
  TH1D* genphoton2Eta   = new TH1D("genphoton2Eta", "", 80, -3.0, 3.0);
  TH1D* genphoton1Phi   = new TH1D("genphoton1Phi", "", 80, -3.5, 3.5);
  TH1D* genphoton2Phi   = new TH1D("genphoton2Phi", "", 80, -3.5, 3.5);
  TH1D* gendiphotoncosthetastar = new TH1D("gendiphotoncosthetastar", "", 100, -1.0, 1.0);

  gendiphotonMinv->Sumw2();
  genphoton1Pt->Sumw2();
  genphoton2Pt->Sumw2();
  genphoton1Eta->Sumw2();
  genphoton2Eta->Sumw2();
  genphoton1Phi->Sumw2();
  genphoton2Phi->Sumw2();
  gendiphotoncosthetastar->Sumw2();

  TString dulogfile = "du1p9log.txt";

  //TString fileout_name = "Unparticles_du1p9_LambdaU_1000_M_2000_py_GEN.root"; double xsec = 3.686e-02+-2.029e-04;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_1000_M_500-2000_py_GEN.root"; double xsec = 1.345e-01+-6.106e-04;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_1250_M_2000_py_GEN.root"; double xsec = 7.573e-03+-4.063e-05;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_1250_M_500-2000_py_GEN.root"; double xsec = 1.182e-01+-5.474e-04;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_1500_M_2000_py_GEN.root"; double xsec = 2.456e-03+-1.288e-05;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_1500_M_500-2000_py_GEN.root"; double xsec = 1.145e-01+-5.330e-04;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_1750_M_2000_py_GEN.root"; double xsec = 1.192e-03+-6.300e-06;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_1750_M_500-2000_py_GEN.root"; double xsec = 1.134e-01+-5.255e-04;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_2000_M_2000_py_GEN.root"; double xsec = 7.897e-04+-3.912e-06;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_2000_M_500-2000_py_GEN.root"; double xsec = 1.129e-01+-5.276e-04;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_2500_M_2000_py_GEN.root"; double xsec = 5.659e-04+-2.825e-06;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_2500_M_500-2000_py_GEN.root"; double xsec = 1.128e-01+-5.291e-04;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_3000_M_2000_py_GEN.root"; double xsec = 5.099e-04+-2.580e-06;
  TString fileout_name = "Unparticles_du1p9_LambdaU_3000_M_500-2000_py_GEN.root"; double xsec = 1.121e-01+-5.255e-04;

  // TString fileout_name = "Unparticles_du1p9_LambdaU_3500_M_2000_py_GEN.root"; double xsec = ;
  // TString fileout_name = "Unparticles_du1p9_LambdaU_3500_M_500-2000_py_GEN.root"; double xsec = ;
  // TString fileout_name = "Unparticles_du1p9_LambdaU_4000_M_2000_py_GEN.root"; double xsec = ;
  // TString fileout_name = "Unparticles_du1p9_LambdaU_4000_M_500-2000_py_GEN.root"; double xsec = ;
  // TString fileout_name = "Unparticles_du1p9_LambdaU_4500_M_2000_py_GEN.root"; double xsec = ;
  // TString fileout_name = "Unparticles_du1p9_LambdaU_4500_M_500-2000_py_GEN.root"; double xsec = ;
  // TString fileout_name = "Unparticles_du1p9_LambdaU_5500_M_2000_py_GEN.root"; double xsec = ;
  // TString fileout_name = "Unparticles_du1p9_LambdaU_5500_M_500-2000_py_GEN.root"; double xsec = ;

  //TString dulogfile = "du1p4log.txt";

  //TString fileout_name = "Unparticles_du1p4_LambdaU_1500_M_2000_py_GEN.root"; double xsec = 2.064e-03+-1.154e-05;
  //TString fileout_name = "Unparticles_du1p4_LambdaU_1500_M_500-2000_py_GEN.root"; double xsec = 1.148e-01+-5.415e-04;
  //TString fileout_name = "Unparticles_du1p4_LambdaU_2000_M_2000_py_GEN.root"; double xsec = 7.523e-04+-3.822e-06;
  //TString fileout_name = "Unparticles_du1p4_LambdaU_2000_M_500-2000_py_GEN.root"; double xsec = 1.122e-01+-5.298e-04;
  //TString fileout_name = "Unparticles_du1p4_LambdaU_2500_M_2000_py_GEN.root"; double xsec = 5.406e-04+-2.755e-06;
  //TString fileout_name = "Unparticles_du1p4_LambdaU_2500_M_500-2000_py_GEN.root"; double xsec = 1.132e-01+-5.312e-04;
  //TString fileout_name = "Unparticles_du1p4_LambdaU_3000_M_2000_py_GEN.root"; double xsec = 4.900e-04+-2.482e-06;
  //TString fileout_name = "Unparticles_du1p4_LambdaU_3000_M_500-2000_py_GEN.root"; double xsec = 1.124e-01+-5.266e-04;
  //TString fileout_name = "Unparticles_du1p4_LambdaU_4000_M_2000_py_GEN.root"; double xsec = 4.776e-04+-2.426e-06;
  //TString fileout_name = "Unparticles_du1p4_LambdaU_4000_M_500-2000_py_GEN.root"; double xsec = 1.118e-01+-5.280e-04;

  //TString dulogfile = "du1p7log.txt";

  //TString fileout_name = "Unparticles_du1p7_LambdaU_1500p0_M_2000.root"; double xsec = 1.389e-03+-7.532e-06;
  //TString fileout_name = "Unparticles_du1p7_LambdaU_1500p0_M_500-2000.root"; double xsec = 1.138e-01+-5.273e-04;
  //TString fileout_name = "Unparticles_du1p7_LambdaU_1750p0_M_2000.root"; double xsec = 8.419e-04+-4.190e-06;
  //TString fileout_name = "Unparticles_du1p7_LambdaU_1750p0_M_500-2000.root"; double xsec = 1.134e-01+-5.344e-04;
  //TString fileout_name = "Unparticles_du1p7_LambdaU_2000p0_M_2000.root"; double xsec = 6.471e-04+-3.220e-06;
  //TString fileout_name = "Unparticles_du1p7_LambdaU_2000p0_M_500-2000.root"; double xsec = 1.125e-01+-5.276e-04;
  //TString fileout_name = "Unparticles_du1p7_LambdaU_2500p0_M_2000.root"; double xsec = 5.283e-04+-2.653e-06;
  //TString fileout_name = "Unparticles_du1p7_LambdaU_2500p0_M_500-2000.root"; double xsec = 1.129e-01+-5.271e-04;
  //TString fileout_name = "Unparticles_du1p7_LambdaU_3000p0_M_2000.root"; double xsec = 4.979e-04+-2.513e-06;
  //TString fileout_name = "Unparticles_du1p7_LambdaU_3000p0_M_500-2000.root"; double xsec = 1.117e-01+-5.255e-04;

//   STest1p7Unp1500p0_M_2000_py_GEN.txt	1.389e-03+-7.532e-06	STest1p7Unp1500p0_M_500-2000_py_GEN.txt	1.138e-01+-5.273e-04
// STest1p7Unp1750p0_M_2000_py_GEN.txt		STest1p7Unp1750p0_M_500-2000_py_GEN.txt
// STest1p7Unp2000p0_M_2000_py_GEN.txt		STest1p7Unp2000p0_M_500-2000_py_GEN.txt
// STest1p7Unp2500p0_M_2000_py_GEN.txt	5.283e-04+-2.653e-06	STest1p7Unp2500p0_M_500-2000_py_GEN.txt	1.129e-01+-5.271e-04
// STest1p7Unp3000p0_M_2000_py_GEN.txt		STest1p7Unp3000p0_M_500-2000_py_GEN.txt

  //TString dulogfile = "du1p3log.txt";

   //TString fileout_name = "Unparticles_du1p3_LambdaU_1750_M_2000_py_GEN.root"; double xsec = 1.489e-03+-8.534e-06;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_2000_M_2000_py_GEN.root"; double xsec = 9.244e-04+-4.884e-06;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_2500_M_2000_py_GEN.root"; double xsec = 5.728e-04+-2.956e-06;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_3000_M_2000_py_GEN.root"; double xsec = 4.948e-04+-2.532e-06;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_3500_M_2000_py_GEN.root"; double xsec = 4.666e-04+-2.368e-06;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_4000_M_2000_py_GEN.root"; double xsec = 4.679e-04+-2.384e-06;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_4500_M_2000_py_GEN.root"; double xsec = 4.622e-04+-2.344e-06;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_1750_M_500-2000_py_GEN.root"; double xsec = 1.120e-01+-5.284e-04;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_2000_M_500-2000_py_GEN.root"; double xsec = 1.107e-01+-5.198e-04;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_2500_M_500-2000_py_GEN.root"; double xsec = 1.111e-01+-5.254e-04;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_3000_M_500-2000_py_GEN.root"; double xsec = 1.124e-01+-5.291e-04;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_3500_M_500-2000_py_GEN.root"; double xsec = 1.120e-01+-5.278e-04;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_4000_M_500-2000_py_GEN.root"; double xsec = 1.120e-01+-5.270e-04;
   //TString fileout_name = "Unparticles_du1p3_LambdaU_4500_M_500-2000_py_GEN.root"; double xsec = 1.115e-01+-5.241e-04;

  //TString fileout_name = "Unparticles_du1p2_LambdaU-2000p0_M_2000.root"; double xsec = 1.306e-03+-7.426e-06;
  //TString fileout_name = "Unparticles_du1p2_LambdaU-2500p0_M_2000.root"; double xsec = 6.750e-04+-3.554e-06;
  //TString fileout_name = "Unparticles_du1p2_LambdaU-3000p0_M_2000.root"; double xsec = 5.149e-04+-2.690e-06;
  //TString fileout_name = "Unparticles_du1p2_LambdaU-3500p0_M_2000.root"; double xsec = 4.707e-04+-2.431e-06;
  //TString fileout_name = "Unparticles_du1p2_LambdaU-4000p0_M_2000.root"; double xsec = 4.521e-04+-2.329e-06;
  //TString fileout_name = "Unparticles_du1p2_LambdaU-2000p0_M_500-2000.root"; double xsec = 1.090e-01+-5.181e-04;
  //TString fileout_name = "Unparticles_du1p2_LambdaU-2500p0_M_500-2000.root"; double xsec = 1.097e-01+-5.141e-04;
  //TString fileout_name = "Unparticles_du1p2_LambdaU-3000p0_M_500-2000.root"; double xsec = 1.103e-01+-5.211e-04;
  //TString fileout_name = "Unparticles_du1p2_LambdaU-3500p0_M_500-2000.root"; double xsec = 1.108e-01+-5.184e-04;
  //TString fileout_name = "Unparticles_du1p2_LambdaU-4000p0_M_500-2000.root"; double xsec = 1.118e-01+-5.227e-04;

  // TString dulogfile = "du1p5log.txt";

  //TString fileout_name = "TestSTest1p5Unp1500p0_M_2000.root"; double xsec = 1.660e-03+-9.317e-06;
  //TString fileout_name = "TestSTest1p5Unp1500p0_M_500-2000.root"; double xsec = 1.135e-01+-5.364e-04;
  //TString fileout_name = "TestSTest1p5Unp2000p0_M_2000.root"; double xsec = 6.858e-04+-3.447e-06;
  //TString fileout_name = "TestSTest1p5Unp2000p0_M_500-2000.root"; double xsec = 1.138e-01+-5.347e-04;
  //TString fileout_name = "TestSTest1p5Unp2500p0_M_2000.root"; double xsec = 5.291e-04+-2.672e-06;
  //TString fileout_name = "TestSTest1p5Unp2500p0_M_500-2000.root"; double xsec = 1.120e-01+-5.269e-04;
  //TString fileout_name = "TestSTest1p5Unp3000p0_M_2000.root"; double xsec = 4.953e-04+-2.494e-06;
  //TString fileout_name = "TestSTest1p5Unp3000p0_M_500-2000.root"; double xsec = 1.118e-01+-5.269e-04;
  //TString fileout_name = "TestSTest1p5Unp3500p0_M_2000.root"; double xsec = 4.861e-04+-2.458e-06;
  //TString fileout_name = "TestSTest1p5Unp3500p0_M_500-2000.root"; double xsec = 1.118e-01+-5.273e-04;
  //TString fileout_name = "TestSTest1p5Unp4000p0_M_2000.root"; double xsec = 4.798e-04+-2.437e-06;
  //TString fileout_name = "TestSTest1p5Unp4000p0_M_500-2000.root"; double xsec = 1.115e-01+-5.244e-04;

  //TString dulogfile = "du1p6log.txt";

  //TString fileout_name = "TestSTest1p6Unp1500p0_M_2000.root"; double xsec = 1.423e-03+-7.847e-06;
  //TString fileout_name = "TestSTest1p6Unp1500p0_M_500-2000.root"; double xsec = 1.145e-01+-5.337e-04;
  //TString fileout_name = "TestSTest1p6Unp2000p0_M_2000.root"; double xsec = 6.470e-04+-3.223e-06;
  //TString fileout_name = "TestSTest1p6Unp2000p0_M_500-2000.root"; double xsec = 1.131e-01+-5.287e-04;
  //TString fileout_name = "TestSTest1p6Unp2500p0_M_2000.root"; double xsec = 5.301e-04+-2.654e-06;
  //TString fileout_name = "TestSTest1p6Unp2500p0_M_500-2000.root"; double xsec = 1.133e-01+-5.301e-04;
  //TString fileout_name = "TestSTest1p6Unp3000p0_M_2000.root"; double xsec = 4.995e-04+-2.523e-06;
  //TString fileout_name = "TestSTest1p6Unp3000p0_M_500-2000.root"; double xsec = 1.119e-01+-5.259e-04;
  //TString fileout_name = "TestSTest1p6Unp3500p0_M_2000.root"; double xsec = 4.901e-04+-2.499e-06;
  //TString fileout_name = "TestSTest1p6Unp3500p0_M_500-2000.root"; double xsec = 1.119e-01+-5.263e-04;
  //TString fileout_name = "TestSTest1p6Unp4000p0_M_2000.root"; double xsec = 4.858e-04+-2.468e-06;
  //TString fileout_name = "TestSTest1p6Unp4000p0_M_500-2000.root"; double xsec = 1.122e-01+-5.312e-04;

  //TString dulogfile = "du1p01log.txt";

  // TString fileout_name = "TestSTest1p01Unp2500p0_M_2000.root"; double xsec = 1.623e-03+-9.221e-06;
  // TString fileout_name = "TestSTest1p01Unp3000p0_M_2000.root"; double xsec = 9.194e-04+-4.985e-06;
  // TString fileout_name = "TestSTest1p01Unp3500p0_M_2000.root"; double xsec = 6.393e-04+-3.402e-06;
  // TString fileout_name = "TestSTest1p01Unp4000p0_M_2000.root"; double xsec = 5.272e-04+-2.814e-06;
  // TString fileout_name = "TestSTest1p01Unp4500p0_M_2000.root"; double xsec = 4.709e-04+-2.483e-06;
  // TString fileout_name = "TestSTest1p01Unp2500p0_M_500-2000.root"; double xsec = 1.123e-01+-5.417e-04;
  // TString fileout_name = "TestSTest1p01Unp3000p0_M_500-2000.root"; double xsec = 1.086e-01+-5.209e-04;
  // TString fileout_name = "TestSTest1p01Unp3500p0_M_500-2000.root"; double xsec = 1.073e-01+-5.066e-04;
  // TString fileout_name = "TestSTest1p01Unp4000p0_M_500-2000.root"; double xsec = 1.077e-01+-5.086e-04;
  // TString fileout_name = "TestSTest1p01Unp4500p0_M_500-2000.root"; double xsec = 1.079e-01+-5.100e-04;

  //TString fileout_name = "TestSTest1p1Unp2500p0_M_2000.root"; double xsec = 9.701e-04+-5.248e-06;
  //TString fileout_name = "TestSTest1p1Unp3000p0_M_2000.root"; double xsec = 6.193e-04+-3.291e-06;
  //TString fileout_name = "TestSTest1p1Unp3500p0_M_2000.root"; double xsec = 5.012e-04+-2.631e-06;
  //TString fileout_name = "TestSTest1p1Unp4000p0_M_2000.root"; double xsec = 4.565e-04+-2.412e-06;
  //TString fileout_name = "TestSTest1p1Unp4500p0_M_2000.root"; double xsec = 4.453e-04+-2.304e-06;
  //TString fileout_name = "TestSTest1p1Unp5000p0_M_2000.root"; double xsec = 4.440e-04+-2.305e-06;
  //TString fileout_name = "TestSTest1p1Unp2500p0_M_500-2000.root"; double xsec = 1.078e-01+-5.116e-04;
  //TString fileout_name = "TestSTest1p1Unp3000p0_M_500-2000.root"; double xsec = 1.087e-01+-5.158e-04;
  //TString fileout_name = "TestSTest1p1Unp3500p0_M_500-2000.root"; double xsec = 1.092e-01+-5.132e-04;
  //TString fileout_name = "TestSTest1p1Unp4000p0_M_500-2000.root"; double xsec = 1.097e-01+-5.155e-04;
  //TString fileout_name = "TestSTest1p1Unp4500p0_M_500-2000.root"; double xsec = 1.099e-01+-5.201e-04;
  //TString fileout_name = "TestSTest1p1Unp5000p0_M_500-2000.root"; double xsec = 1.099e-01+-5.156e-04;

  //TString fileout_name = "Unparticles_du1p8_LambdaU_2500_M_2000.root"; double xsec = 5.289e-04+-2.672e-06;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_1000_M_2000.root"; double xsec = 1.608e-02+-8.839e-05;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_1000_M_500-2000.root"; double xsec = 1.271e-01+-5.850e-04;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_1250_M_2000.root"; double xsec = 3.855e-03+-2.078e-05;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_1250_M_500-2000.root"; double xsec = 1.162e-01+-5.433e-04;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_1750_M_2000.root"; double xsec = 1.503e-03+-8.206e-06;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_1750_M_500-2000.root"; double xsec = 1.134e-01+-5.320e-04;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_2250_M_2000.root"; double xsec = 5.735e-04+-2.855e-06;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_2250_M_500-2000.root"; double xsec = 1.117e-01+-5.222e-04;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_2500_M_2000.root"; double xsec = 5.289e-04+-2.672e-06;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_2500_M_500-2000.root"; double xsec = 1.120e-01+-5.279e-04;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_2750_M_2000.root"; double xsec = 5.102e-04+-2.565e-06;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_2750_M_500-2000.root"; double xsec = 1.123e-01+-5.295e-04;
  //
  //TString fileout_name = "Unparticles_du1p8_LambdaU_2000_M_2000.root"; double xsec = 6.658e-04+-3.299e-06;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_2000_M_500-2000.root"; double xsec = 1.131e-01+-5.333e-04;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_1500_M_2000.root"; double xsec = 1.503e-03+-8.206e-06;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_1500_M_500-2000.root"; double xsec = 1.142e-01+-5.328e-04;

  //TString fileout_name = "Unparticles_du1p8_LambdaU_2500_M_2000.root"; double xsec = 5.289e-04+-2.672e-06;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_2500_M_500-2000.root"; double xsec = 1.120e-01 5.279e-04;

  //TString fileout_name = "Unparticles_SM_M_500-2000.root"; double xsec = 1.200e-01 +- 5.693e-04;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_3000_M_2000.root"; double xsec = 5.011e-04+-2.511e-06;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_3000_M_500-2000.root"; double xsec = 1.117e-01+-5.254e-04 ;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_4000_M_2000.root"; double xsec = 4.876e-04+-2.466e-06;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_4000_M_500-2000.root"; double xsec = 1.123e-01+-5.271e-04;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_6000_M_2000.root"; double xsec = 4.797e-04+-2.412e-06;
  //TString fileout_name = "Unparticles_du1p8_LambdaU_6000_M_500-2000.root"; double xsec = 1.118e-01+-5.256e-04;
  //TString fileout_name = "Unparticles_SM_M-2000.root"; double xsec = 4.734e-04;

  //TString fileout_name = "Unparticles_du1p5_LambdaU_1000_M_2000.root"; double xsec = 1.381e-02;
  //TString fileout_name = "Unparticles_du1p5_LambdaU_1000_M_500-2000.root"; double xsec = 1.326e-01;
  //TString fileout_name = "Unparticles_du1p5_LambdaU_1250_M_2000.root"; double xsec = 3.934e-03;
  //TString fileout_name = "Unparticles_du1p5_LambdaU_1250_M_500-2000.root"; double xsec = 1.176e-01;
  //TString fileout_name = "Unparticles_du1p5_LambdaU_1500_M_2000.root"; double xsec = 1.660e-03;
  //TString fileout_name = "Unparticles_du1p5_LambdaU_1500_M_500-2000.root"; double xsec = 1.135e-01;
  //TString fileout_name = "Unparticles_du1p5_LambdaU_1750_M_2000.root"; double xsec = 9.431e-04;

  //TString fileout_name = "Unparticles_du1p5_LambdaU_1750_M_500-2000.root"; double xsec = 1.130e-01;
  //TString fileout_name = "Unparticles_du1p5_LambdaU_2000_M_2000.root"; double xsec = 6.858e-04;
  //TString fileout_name = "Unparticles_du1p5_LambdaU_2000_M_500-2000.root"; double xsec = 1.138e-01;

  //TString fileout_name = "Unparticles_du1p9_LambdaU_1000_M_2000.root"; double xsec = 3.686e-02;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_1000_M_500-2000.root"; double xsec = 1.345e-01;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_1250_M_2000.root"; double xsec = 7.573e-03;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_1250_M_500-2000.root"; double xsec = 1.182e-01;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_1500_M_2000.root"; double xsec = 2.456e-03;

  //TString fileout_name = "Unparticles_du1p9_LambdaU_1500_M_500-2000.root"; double xsec = 1.145e-01;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_1750_M_2000.root"; double xsec = 1.192e-03;

  //TString fileout_name = "Unparticles_du1p9_LambdaU_1750_M_500-2000.root"; double xsec = 1.134e-01;
  //TString fileout_name = "Unparticles_du1p9_LambdaU_2000_M_2000.root"; double xsec = 7.897e-04;
  // TString fileout_name = "Unparticles_du1p9_LambdaU_2000_M_500-2000.root"; double xsec = 1.129e-01;

  //TString fileout_name = "Unparticles_du1p1_LambdaU_2000_M_2000.root"; double xsec = 	2.167e-03;
  //TString fileout_name = "Unparticles_du1p1_LambdaU_1500_M_2000.root"; double xsec = 	7.457e-03;
  //TString fileout_name = "Unparticles_du1p1_LambdaU_1250_M_2000.root"; double xsec = 	1.673e-02;
  //TString fileout_name = "Unparticles_du1p1_LambdaU_1750_M_2000.root"; double xsec = 	3.798e-03;
  //TString fileout_name = "Unparticles_du1p1_LambdaU_1000_M_2000.root"; double xsec = 	4.531e-02;
  //
  //TString fileout_name = "Unparticles_du1p3_LambdaU_2000_M_2000.root"; double xsec = 	9.244e-04;
  //TString fileout_name = "Unparticles_du1p3_LambdaU_1250_M_2000.root"; double xsec = 	7.092e-03;
  //TString fileout_name = "Unparticles_du1p3_LambdaU_1500_M_2000.root"; double xsec = 	2.904e-03;
  //TString fileout_name = "Unparticles_du1p3_LambdaU_1000_M_2000.root"; double xsec = 	2.246e-02;
  //TString fileout_name = "Unparticles_du1p3_LambdaU_1750_M_2000.root"; double xsec = 	1.489e-03;

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
      Ntotal++;

      double weight = xsec*1000/numevents;

      // if GenDiPhoton_isEBEB{
      //   isEBEB = isEBEB + 1;
      // }

      if  ((GenPhoton1_eta < 1.4442) && (GenPhoton2_eta< 1.4442)) isEBEB = isEBEB + 1; //

    if ((GenPhoton1_pt >75) && (GenPhoton2_pt >75)){
      gendiphotonMinv->Fill(GenDiPhoton_Minv, weight);
    	genphoton1Pt->Fill(GenPhoton1_pt, weight);
    	genphoton2Pt->Fill(GenPhoton2_pt, weight);
    	genphoton1Eta->Fill(GenPhoton1_eta, weight);
    	genphoton2Eta->Fill(GenPhoton2_eta, weight);
    	genphoton1Phi->Fill(GenPhoton1_phi, weight);
    	genphoton2Phi->Fill(GenPhoton2_phi, weight);
      gendiphotoncosthetastar->Fill(GenDiPhoton_cosThetaStar, weight);
    }
   }
   cout << endl;
   cout << "File: " << fileout_name << endl;
   cout << "Total entries            : " << Ntotal    << " " << nentries << endl;
   cout << "isEBEB  :" << isEBEB << endl;
   //cout << "Passed DiphMinv cut      : " << nDiphMinv << endl;
   //cout << "Passed etaCut            : " << netaCut   << endl;
   cout << endl;

   ofstream outfile;
   outfile.open(dulogfile, ios::app);
   outfile << "Log  : " << fileout_name << "; entries: " << Ntotal << "; isEBEB: " << isEBEB << endl;
   outfile.close();

   TFile file_out(fileout_name, "RECREATE");

   cout << "Writing file.." << endl;
   gendiphotonMinv->Write();
   genphoton1Pt->Write();
   genphoton2Pt->Write();
   genphoton1Eta->Write();
   genphoton2Eta->Write();
   genphoton1Phi->Write();
   genphoton2Phi->Write();
   gendiphotoncosthetastar->Write();
}
