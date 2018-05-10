#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh

#Sample format
#hadd -f root://cmseos.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-1000To2000.root 'xrdfsls -u /store/user/cuperez/DiPhotonAnalysis/Summer16GGJets/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/crab_GGJets_M-1000To2000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180202_203147/0000 | grep \.root'

######## STRINGS ############

rootfnal="root://cmseos.fnal.gov/"
#rootxrd="xrdfsls -u" #This command is not recognized unless you copy paste
rootxrd="xrdfs root://cmseos.fnal.gov ls -u"
#xrdfs root://cmseos.fnal.gov ls
greproot="| grep \.root"
crab="/crab_"
root=".root"
haddf="hadd -f"

#Output Directory
outputdir="/store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/"


#Input Directory
inputdir="/store/user/cuperez/DiPhotonAnalysis/Summer16GGJets/"
inputdir2="__80XMiniAODv2__MINIAODSIM"
#loop here 
inputdir3=("/180202_203147/0000"
	"/180202_203156/0000"
	"/180202_203125/0000"
	"/180202_203212/0000"
	"/180202_203137/0000"
	"/180202_203224/0000"
	"/180202_203112/0000"
	"/180202_203237/0000")
		

#Mass binning
#loop here 
massbin=("GGJets_M-1000To2000_Pt-50_13TeV-sherpa" 
	"GGJets_M-2000To4000_Pt-50_13TeV-sherpa"
	"GGJets_M-200To500_Pt-50_13TeV-sherpa"
	"GGJets_M-4000To6000_Pt-50_13TeV-sherpa"
        "GGJets_M-500To1000_Pt-50_13TeV-sherpa"
	"GGJets_M-6000To8000_Pt-50_13TeV-sherpa"
	"GGJets_M-60To200_Pt-50_13TeV-sherpa"
	"GGJets_M-8000To13000_Pt-50_13TeV-sherpa")


######### COMMANDS ##########
start="#!/bin/bash"
echo $start > haddcmds.sh
echo "source /cvmfs/cms.cern.ch/cmsset_default.sh" >> haddcmds.sh

bin_num=${#massbin[@]}
for ((i=0; i<bin_num; i++))
do
   output=$rootfnal$outputdir${massbin[i]}$root
   input="\`$rootxrd $inputdir${massbin[i]}$crab${massbin[i]}$inputdir2${inputdir3[i]} $greproot\`"
   #in=$($rootxrd $inputdir${massbin[i]}$crab${massbin[i]}$inputdir2${inputdir3[i]} $greproot)
   #echo $input
   #echo $output
   echo "hadd -f" $output $input >> haddcmds.sh
   #Merging files
   #$() same as `` back ticks for command substitution 
   #hadd -f $output `eval $input`	
   #cmd = hadd -f $output $input
   #eval $cmd
done

bash haddcmds.sh
