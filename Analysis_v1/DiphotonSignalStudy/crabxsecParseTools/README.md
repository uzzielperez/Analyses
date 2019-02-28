# How to use crabxsecparser

1.) Locate the crab outputs you want. You can use the eoshelper.sh to loop through the output directories you need. 
2.) Generate parsedis.txt file to include the logfiles containing the cross sections. To do this get the eos directories of the datasets of interest and run 
```bash
python eoshepler.py -i somefilecontaininglistofdirectories.txt 
``` 
If you don't know the time stamps yet you can use the -t flag. 

3.) Run xsec_get.py to copy the tarred files to current directory. 
4.) Run xsecParser.py to get the cross-sections.  
