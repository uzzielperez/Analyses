# Analyses

## Workflow
0.) Codes in Analysis_vx directories. <br />
1.) Produce Ntuples by running Analyzer over datasets <br />
2.) Merge Root files with the same Mass Bin <br />
3.) Chain the same trees together and Make Class to loop over events <br />
Run selection criteria through ClassName.C and analyze.C. <br />
This will write histograms into a new .root file for plotting. <br />
4.) Run Plotter <br />

## Analysis_vx
```bash
cd Analysis_vx/

```

0.) Interacting with eos files can be quite daunting without tab completion and wildcards.  Configure and run eoshelper.sh to get full paths (quite LONG!) to the CRAB ntuples. <br />
```bash

./eoshelper.sh

```
1.) Configure Input and Output path and files in merge.py. To merge, run
```bash

python merge.py

```
This will create two files: arootmerger.sh (will be executed with previous command) and a text (afiles2chain.txt) file containing fulls paths to files of the new merged products. 
 
2.) Using afiles2chain.txt as input, chain trees and make class. In progress...<br />
3.) Configure class for selection and execute analyze.C to loop over events. In progress...<br />
4.) Make general purpose plotters

## Initial SM Diphoton 2016 Pipeline
1.) Run ExoDiPhotonAnalyzer on GGJets Sherpa from summer using ./submit_crab_cfg.py <br />
2.) Merge files in eos using 
```bash

/merger/.hadd_script.sh

```
3.) Create TChain and MakeClass using analyze.C. Comment out instance of Class and t.Loop(). <br />
4.) Do selection in Classname.C <br />
5.) Uncomment class instance and t.Loop(). Run 
```bash

cmsenv
root -l /macros/analyze.C

```  
5.) To plot run 
```bash

python /pyroot/plotnostat-diphbkg.py

```

## Bash Scripts
To execute the bash scripts <br />
```bash

chmod u+x scriptname.sh 
./scriptname.sh  

```

or <br />

```bash

-x script_name.sh 
bash -x script_name.sh 
source scriptname.sh 

```

