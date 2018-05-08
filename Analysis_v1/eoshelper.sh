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
crabntuplesDEEP=true #To search deep for ALL the unmerged CRAB ntuples 
crabntuples=true    # true to get full path, uncomment appropriate sub
#sub2='/Summer16GGJets'
#sub2='/Summer16GGJetsResubmit'
sub2='/Run2016Data'
#-- MERGED FILES 
merged=true           # true to get full path, uncomment appropriate sub
#sub='/Summer16_GGJets_Merged'
sub='/Run2016Data-Merged'
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

#-------/store/user/cuperez/projectname/sub ------>  MERGED
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

#-------/store/user/cuperez/projectname/sub2 -----> CRABNTUPLES
while $crabntuples; do
 echo 'CRAB Ntuples here:'
 for i in `$eosls $DIR2`
 do
  newdir2=$DIR2/$i
  for j in `$eosls $newdir2`
  do
   new2=$newdir2/$j
   echo $new2 
  done
 done
break
done

#------DiPhotonAnalysis Full
redirector='root://cmsxrootd.fnal.gov/'
while $crabntuplesDEEP; do
 echo 'CRAB unmerged ntuples:' 
 for i in `$eosls $DIR2`
 do 
   #echo $i
   newdir3=$DIR2/$i
   #echo $eosls $newdir
   for j in `$eosls $newdir3`
   do
    new3=$newdir3/$j
    for k in `$eosls $new3`
    do
     new4=$new3/$k
     #echo $new3/$k ---> just up to datesdir
     for l in `$eosls $new4`
     do
      #echo $l 
      new5=$new4/$l	
      #echo $new5 # -----> just up to 0000/
      for m in `$eosls $new5`
      do
       new6=$new5/$m
       echo $new6
       # echo $m # filename only
       #echo $new6 >> ${k}fi.txt
       echo $redirector$new6 >> ${j}fi.txt
      done
     done
    done
   done
 done
break
done

echo 'To check root files'
echo 'root -l root://cmsxrootd.fnal.gov//store/user/jjesus/rootFile.root'
