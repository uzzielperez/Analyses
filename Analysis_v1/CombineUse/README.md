# USING COMBINE
### Special thanks to Wenyu Zhang for her plotting script and for Caleb Smith for helping me put it all together.

1.) Setup combine and Combine Harvester.  
2.) Prepare datacards in HiggsAnalysis/CombinedLimit directory.   
3.) Run ./run_combine.sh with the prepared datacards. This will output the signal strengths for different confidence levels and higgsCombineTest.AsymptoticLimits*root. Currently uses AsymptoticLimits method but you can edit the flags.  
4.) Run Combine Harvester. Output is limits.json.
```bash

../../CombineHarvester/CombineTools/scripts/combineTool.py -M CollectLimits higgsCombineTest.AsymptoticLimits.mH*root

```  
5.) Reformat the json file into something readable by the current plotter, written by my friend Wenyu Zhang (Brown U.). (I butchered her work a bit.). 

```bash
cd CombineCustomPlt
python limits_formatter.py. 
```
6.) Plot.  

```bash
python plot_limits.py
``` 
