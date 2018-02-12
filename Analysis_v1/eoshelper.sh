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
quickcheck=false

#-- CRAB NTUPLES 
crabntuples=false    # true to get full path, uncomment appropriate sub

#sub='/Summer16GGJets'

#-- MERGED FILES 
merged=true           # true to get full path, uncomment appropriate sub
sub='/Summer16_GGJets_Merged'

#######
DIR=$eosdir$project$sub

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
 for i in `$eosls $DIR`
 do 
   #echo $i
   newdir=$DIR/$i
   #echo $eosls $newdir
   for j in `$eosls $newdir`
   do
    #echo $j
    new=$newdir/$j
    #echo $eosls $new
   done
    for k in `$eosls $new`
    do
     echo $new/$k
    done
 done
break
done
