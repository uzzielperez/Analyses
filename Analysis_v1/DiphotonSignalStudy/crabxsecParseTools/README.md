#How to use crabxsecparser

Specify sample/decay and Tune to retrieve cross-sections. 

```bash

python xsec.py

```
To get formatted cross-section information for Common Classes:

```bash

python xsec_get.py -a

```

Sample output:
```bash
Calculating Average Cross-sections from parsed log files.
if(sample.Contains("RSGravToGG_kMpl-001_M-3000_TuneCUEP8M1_13TeV-pythia8")) xsec =  1.501e-05;
if(sample.Contains("RSGravToGG_kMpl-001_M-750_TuneCUEP8M1_13TeV-pythia8")) xsec =  5.088e-02;
if(sample.Contains("RSGravToGG_kMpl-01_M-5000_TuneCUEP8M1_13TeV-pythia8")) xsec =  1.439e-05;
if(sample.Contains("RSGravToGG_kMpl-02_M-3000_TuneCUEP8M1_13TeV-pythia8")) xsec =  5.803e-03;
if(sample.Contains("RSGravToGG_kMpl-02_M-750_TuneCUEP8M1_13TeV-pythia8")) xsec =  2.062e+01;
if(sample.Contains("RSGravToGG_kMpl-001_M-5000_TuneCUEP8M1_13TeV-pythia8")) xsec =  1.425e-07;
if(sample.Contains("RSGravToGG_kMpl-01_M-3000_TuneCUEP8M1_13TeV-pythia8")) xsec =  1.492e-03;
if(sample.Contains("RSGravToGG_kMpl-01_M-750_TuneCUEP8M1_13TeV-pythia8")) xsec =  5.092e+00;
if(sample.Contains("RSGravToGG_kMpl-02_M-6000_TuneCUEP8M1_13TeV-pythia8")) xsec =  7.185e-06;
```
## OLD 

1.) Locate the crab outputs you want. You can use the eoshelper.sh to loop through the output directories you need.
2.) Generate parsedis.txt file to include the logfiles containing the cross sections. To do this get the eos directories of the datasets of interest and run

```bash

python eoshelper.py -i processdis.txt -f > parsedis.txt

```
The -f flag is to run the formatter flag to get the tar files.
If you don't know the time stamps yet you can use the -t flag.

3.) Run xsec_get.py to copy the tarred files to current directory. You need the -r flag to copy the tarred files and untar them for parsing, -a to parse and get average cross-sections and write them into
the format you need for Cross-sections.h

```bash

python xsec_get.py -i parsedis.txt -r -a

```

You can sort the formatted list of cross-sections with the -s option after running. You can use -d to clean directory when you are done.
