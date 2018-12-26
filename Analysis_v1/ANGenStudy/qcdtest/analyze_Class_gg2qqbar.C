#include "Class_gg2qqbar.C"
#include <iostream>
#include "TStopwatch.h"
using namespace std;

int analyze_Class_gg2qqbar(){
        // start stopwatch
	TStopwatch sw;
	sw.Start();

	Class_gg2qqbar t;
        t.Loop();

	// stop stopwatch
	sw.Stop();
	cout << "Real Time: " << sw.RealTime()/60.0 << " minutes" << endl;
	cout << "CPU Time: " << sw.CpuTime()/60.0 << " minutes" << endl;
	return 0;

}
