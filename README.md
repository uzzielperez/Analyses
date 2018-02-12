# Analyses

## Workflow
1.) Produce Ntuples by running Analyzer over datasets <br />
2.) Merge Root files with the same Mass Bin <br />
3.) Chain the same trees together and Make Class to loop over events <br />
Run selection criteria through ClassName.C and analyze.C. <br />
This will write histograms into a new .root file for plotting. <br />
4.) Run Plotter <br />

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
root -l analyze.C

```  
5.) To plot run 
```bash

python plotnostat-diphbkg.py

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

