# How to use crabxsecparser

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
