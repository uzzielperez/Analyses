#include "Class_Unp_LU4000_du1p5_spin2_ggON_M2000.C"
#include <iostream>
#include "TStopwatch.h"
using namespace std;

int analyze_Class_Unp_LU4000_du1p5_spin2_ggON_M2000(){
        // start stopwatch
	TStopwatch sw;
	sw.Start();

	Class_Unp_LU4000_du1p5_spin2_ggON_M2000 t;
        t.Loop();

	// stop stopwatch
	sw.Stop();
	cout << "Real Time: " << sw.RealTime()/60.0 << " minutes" << endl;
	cout << "CPU Time: " << sw.CpuTime()/60.0 << " minutes" << endl;
	return 0;

}
