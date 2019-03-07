#include "Class_RSGravitonToGammaGamma_kMpl001_M_750.C"
#include <iostream>
#include "TStopwatch.h"
using namespace std;

int analyze_RSGravitonToGammaGamma_kMpl001_M_750(){
        // start stopwatch
	TStopwatch sw;
	sw.Start();

	Class_RSGravitonToGammaGamma_kMpl001_M_750 t;
        t.Loop();

	// stop stopwatch
	sw.Stop();
	cout << "Real Time: " << sw.RealTime()/60.0 << " minutes" << endl;
	cout << "CPU Time: " << sw.CpuTime()/60.0 << " minutes" << endl;
	return 0;

}
