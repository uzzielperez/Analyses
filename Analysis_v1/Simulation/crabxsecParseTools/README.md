# How to use crabxsecparser

1.) Locate the crab outputs you want. You can use the eoshelper.sh to loop through the output directories you need.
2.) Edit the parsedis.txt file to include the directories containing the cross sections
3.) Edit the "pattern" in xsec_get.py and then run it to copy the tarred files to current directory.
4.) Run xsecParser.py to get the cross-sections with exact patterns in parsedis.txt. Or run xsecParseDirectories.py (WIP)
