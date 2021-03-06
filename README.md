# Analyses

## Workflow
0.) Codes in Analysis_vx directories. <br />
1.) Produce Ntuples by running Analyzer over datasets <br />
2.) Merge Root files with the same Mass Bin <br />
3.) Chain the same trees together and Make Class to loop over events <br />
Run selection criteria through ClassName.C and analyze.C. <br />
This will write histograms into a new .root file for plotting. <br />
4.) Run Plotter <br />

## New Features
Cross-sections retrieval from CRAB can be facilitated using tools below:

```bash

cd Analyses/Analysis_v1/Simulation/crabxsecParseTools

```

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

2.) Using aInputMerged.txt as input, chain trees and make class. Change the work directory (study) in the runChainClass.py file and run <br />
```bash

python runChainClass.py

```

This will create a new <Classname>.C, <Classname>.h, analyze<Classname>.C. To start a new analysis with different cuts make new directory and do your analysis there. Otherwise
you risk overwriting your main analysis codes. RunChainClass.py actually makes the directory for you and you can start working there.

As of 5/22/18, this step now has command line options to include custom files. To see options:

```bash

python runChainClass.py -h

```


3.) Configure class for selection and execute analyze.C to loop over events. One can do, <br />
```bash

root -l analyze.C

```
This will write a root file which you can make plots from.

4.) Using root file created plot with
```bash

python quick_plotter_v1.py

```
This will generate .png or .pdf files that you need for presentation or quick view. Program needs refinement.
For comparison plots one can use the ratio plotter or the multiPlotter. Update file manually for histograms you want to compare. MultiPlotter takes a list of files and loops over the files and overlays the similar objects (must be created by the same MakeClass script). Variants of these basic plotters are in a directory.

```bash

python ratioPlotter.py
# or
python multiPlotter.py

```


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
