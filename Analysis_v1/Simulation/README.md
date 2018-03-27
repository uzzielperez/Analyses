## Sherpa 
# Setup working environment
```bash

scram project CMSSW_9_3_1 # Do once
cd CMSSW_9_3_1/src
cmsenv
export TOPDIR=$PWD

```
Checkout SherpaInterface.

```bash

git cms-addpkg GeneratorInterface/SherpaInterface # Do once 

```
# Make work directory
mkdir -p <StudyName>/PROJECT/test
mkdir -p <StudyName>/PROJECT/python
cd <StudyName>/PROJECT/test/
cp $TOPDIR/GeneratorInterface/SherpaInterface/data/*SherpaLibs.sh .
cp [PATH_TO_YOUR_RUNCARD]/Run.dat_[XYZ] .

## Sherpack Creation 
Initialization and PhaseSpace Integration is very time-consuming. One can use OpenMPI for parallelization.<br />
```bash

./MakeSherpaLibs.sh -p [XYZ] -o LBCR -v

```

To use OpenMPI parallelization you can use this instead:

```bash 

./MakeSherpaLibs.sh -p [XYZ] -o LBCR -v -m mpirun -M '-n [NUMBEROFCORES]'

```

# Create Sherpack 
After making SherpaLibs, create Sherpack 
./PrepareSherpaLibs.sh -p [XYZ]

# test locally

mv sherpa_[XYZ]_MASTER_cff.py $TOPDIR/<StudyName>/PROJECT/python
cd ..
scram b
cd test
cmsDriver.py <StudyName>/PROJECT/python/sherpa_[XYZ]_MASTER_cff.py -s GEN -n 100 --no_exec --conditions auto:mc --eventcontent RAWSIM
cmsRun sherpa_[XYZ]_MASTER_cff_py_GEN.py 
