#include "Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000.C"
#include <iostream>
#include "TStopwatch.h"
using namespace std;

int analyze_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000(){
        // start stopwatch
	TStopwatch sw;
	sw.Start();

	Class_ADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000 t;
        t.Loop();

	// stop stopwatch
	sw.Stop();
	cout << "Real Time: " << sw.RealTime()/60.0 << " minutes" << endl;
	cout << "CPU Time: " << sw.CpuTime()/60.0 << " minutes" << endl;
	return 0;

}
