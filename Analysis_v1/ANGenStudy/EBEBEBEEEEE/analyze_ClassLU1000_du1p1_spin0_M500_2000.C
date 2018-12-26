#include "ClassLU1000_du1p1_spin0_M500_2000.C"
#include <iostream>
#include "TStopwatch.h"
using namespace std;

int analyze_ClassLU1000_du1p1_spin0_M500_2000(){
        // start stopwatch
	TStopwatch sw;
	sw.Start();

	ClassLU1000_du1p1_spin0_M500_2000 t;
        t.Loop();

	// stop stopwatch
	sw.Stop();
	cout << "Real Time: " << sw.RealTime()/60.0 << " minutes" << endl;
	cout << "CPU Time: " << sw.CpuTime()/60.0 << " minutes" << endl;
	return 0;

}
