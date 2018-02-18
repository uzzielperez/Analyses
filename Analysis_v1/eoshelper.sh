#!/bin/bash

####### Directories
# Main
eosdir='/store/user/cuperez'

## EDIT HERE sub
project='/DiPhotonAnalysis'
#project='/TriPhotonAnalysis'
######################################
#------ECHO SETTINGS
#-- Quickcheck
quickcheck=true

#-- CRAB NTUPLES 
crabntuples=true    # true to get full path, uncomment appropriate sub
#sub2='/Summer16GGJets'
sub2='/Summer16GGJetsResubmit'
#-- MERGED FILES 
merged=true           # true to get full path, uncomment appropriate sub
sub='/Summer16_GGJets_Merged'
#sub='/
#######
DIR=$eosdir$project$sub
DIR2=$eosdir$project$sub2
####### eos aliases 
eosls='eos root://cmseos.fnal.gov ls'
eosmkdir='eos root://cmseos.fnal.gov mkdir'
eosrm='eos root://cmseos.fnal.gov rm'
eosrmdir='eos root://cmseos.fnal.gov rm -r '
xrdfsls='xrdfs root://cmseos.fnal.gov ls'

# flags
#-u=prints urls
#-l= lists

###### eos commands
# EDIT COMMAND HERE: 
#$eosls -l eosdir

#--------/store/user/cuperez/projectname
while $quickcheck; do
 echo 'Printing out subdirectories of' $eosdir$project:
 for i in `$eosls $eosdir$project`
 do
   echo $i
 done
break
done

#-------/store/user/cuperez/projectname/sub
while $merged; do
 echo 'Printing out Contents of Directories with Merged files':
 for i in `$eosls $DIR`
 do
  #echo $i
  newdir=$DIR/$i
  for j in `$eosls $newdir`
  do
   new=$newdir/$j
   echo $new 
  done
 done
break
done

#------DiPhotonAnalysis Full
while $crabntuples; do
 echo 'CRAB staged out files in these directories:' 
 for i in `$eosls $DIR2`
 do 
   #echo $i
   newdir2=$DIR2/$i
   #echo $eosls $newdir
   for j in `$eosls $newdir2`
   do
    #echo $j
    new2=$newdir2/$j
    #echo $eosls $new
   done
   for k in `$eosls $new2`
    do
     echo $new2/$k
   done
 done
break
done

echo 'To check root files'
echo 'root -l root://cmsxrootd.fnal.gov//store/user/jjesus/rootFile.root'
