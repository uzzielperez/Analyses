import ROOT
import time
import subprocess
import os
import argparse
import re
from string import Template
import sys

# Timer
sw = ROOT.TStopwatch()
sw.Start()

#filepath = "/uscms_data/d3/cuperez/CMSSW_8_0_25/src/multiphoton-analysis/nPhotonAnalyzer/out"
DATASET = []

do1p13Test = False
do1p83Test = False
do1p93Test = True
xsecdict = {}
if do1p13Test:
    du_tag = "1p1"
    DATASET.append("TestSTest1p1Unp1500p0_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p1Unp1500p0_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p1Unp1500p0_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p1Unp1500p0_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p1Unp2500p0_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p1Unp2500p0_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p1Unp2500p0_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p1Unp2500p0_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p1Unp4000p0_spin-0_M_2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p1Unp4000p0_spin-0_M_500-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p1Unp4000p0_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p1Unp4000p0_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    xsecdict_temp = {"du-%s_LambdaU-1500_spin-0_M_500-2000": 1.722e-01+-9.696e-04,
                "du-%s_LambdaU-1500_spin-0_M_2000": 7.249e-03+-4.311e-05,
                "du-%s_LambdaU-2500_spin-0_M_2000": 1.986e-03+-1.181e-05,
                "du-%s_LambdaU-2500_spin-0_M_500-2000": 5.329e-02+-2.974e-04,
                "du-%s_LambdaU-4000_spin-0_M_500-2000": 2.168e-02+-1.209e-04,
                "du-%s_LambdaU-4000_spin-0_M_2000": 6.149e-04+-3.639e-06,
                "du-%s_LambdaU-1500_spin-2_M_2000": 6.102e-03+-3.660e-05,
                "du-%s_LambdaU-1500_spin-2_M_500-2000": 1.643e-01+-7.972e-04,
                "du-%s_LambdaU-2500_spin-2_M_500-2000": 1.426e-01+-6.848e-04,
                "du-%s_LambdaU-2500_spin-2_M_2000": 9.302e-04+-5.216e-06,
                "du-%s_LambdaU-4000_spin-2_M_500-2000": 1.438e-01+-6.919e-04,
                "du-%s_LambdaU-4000_spin-2_M_2000": 6.016e-04+-3.076e-06}
    xsecdict.update(xsecdict_temp)
if do1p83Test:
    du_tag = "1p8"
    DATASET.append("TestSTest1p8Unp1500p0_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p8Unp1500p0_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p8Unp2500p0_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p8Unp2500p0_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p8Unp4000p0_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p8Unp4000p0_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # xsecdict_temp = {"du-%s_LambdaU-1500_spin-0_M_500-2000": 1.722e-01+-9.696e-04,
    #             "du-%s_LambdaU-1500_spin-0_M_2000": 7.249e-03+-4.311e-05,
    #             "du-%s_LambdaU-2500_spin-0_M_2000": 1.986e-03+-1.181e-05,
    #             "du-%s_LambdaU-2500_spin-0_M_500-2000": 5.329e-02+-2.974e-04,
    #             "du-%s_LambdaU-4000_spin-0_M_500-2000": 2.168e-02+-1.209e-04,
    #             "du-%s_LambdaU-4000_spin-0_M_2000": 6.149e-04+-3.639e-06,

    xsecdict_temp = {"du-%s_LambdaU-1500_spin-2_M_2000" %(du_tag): 1.809e-03+-1.065e-05,
                "du-%s_LambdaU-1500_spin-2_M_500-2000" %(du_tag): 1.507e-01+-7.174e-04,
                "du-%s_LambdaU-2500_spin-2_M_500-2000" %(du_tag): 1.489e-01+-7.070e-04,
                "du-%s_LambdaU-2500_spin-2_M_2000" %(du_tag): 7.649e-04+-3.775e-06,
                "du-%s_LambdaU-4000_spin-2_M_500-2000" %(du_tag): 1.478e-01+-7.067e-04,
                "du-%s_LambdaU-4000_spin-2_M_2000" %(du_tag): 6.995e-04+-3.512e-06}
    xsecdict.update(xsecdict_temp)

if do1p93Test:
    du_tag = "1p9"
    DATASET.append("TestSTest1p9Unp1500p0_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p9Unp1500p0_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p9Unp2500p0_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p9Unp2500p0_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p9Unp4000p0_spin-2_M_500-2000_py_GEN.root/demo/fgenTree")
    DATASET.append("TestSTest1p9Unp4000p0_spin-2_M_2000_py_GEN.root/demo/fgenTree")
    # xsecdict_temp = {"du-%s_LambdaU-1500_spin-0_M_500-2000": 1.722e-01+-9.696e-04,
    #             "du-%s_LambdaU-1500_spin-0_M_2000": 7.249e-03+-4.311e-05,
    #             "du-%s_LambdaU-2500_spin-0_M_2000": 1.986e-03+-1.181e-05,
    #             "du-%s_LambdaU-2500_spin-0_M_500-2000": 5.329e-02+-2.974e-04,
    #             "du-%s_LambdaU-4000_spin-0_M_500-2000": 2.168e-02+-1.209e-04,
    #             "du-%s_LambdaU-4000_spin-0_M_2000": 6.149e-04+-3.639e-06,

    xsecdict_temp = {"du-%s_LambdaU-1500_spin-2_M_2000" %(du_tag): 2.848e-03+-1.507e-05,
                "du-%s_LambdaU-1500_spin-2_M_500-2000" %(du_tag): 1.506e-01+-7.085e-04,
                "du-%s_LambdaU-2500_spin-2_M_500-2000" %(du_tag): 1.480e-01+-7.063e-04,
                "du-%s_LambdaU-2500_spin-2_M_2000" %(du_tag): 8.027e-04+-3.948e-06,
                "du-%s_LambdaU-4000_spin-2_M_500-2000" %(du_tag): 1.478e-01+-7.066e-04,
                "du-%s_LambdaU-4000_spin-2_M_2000" %(du_tag): 7.013e-04+-3.510e-06}
    xsecdict.update(xsecdict_temp)



Class_template = "ClassTemplate.C"
ClassHeader_template = "ClassTemplate.h"

#Templates
class_Ctemp = "ClassTemplateisEBEB.C"
class_htemp = "ClassTemplateisEBEB.h"
run_analyzetemp = "analyzeTemplate.C"
#CFilein  = open(class_Ctemp)
#hFilein  = open(class_htemp)
pattern = r'TestSTest%sUnp([^(]*)p0_spin-([^(]*)_M_([^(]*)_py_GEN' %(du_tag)
for dset in DATASET:
    match = re.findall(pattern, dset);
    LambdaU, spin,  massrange = match[0]
    #print match[0]
    xseckey = "du-%s_LambdaU-%s_spin-%s_M_%s" %(du_tag, LambdaU, spin, massrange)
    #print xseckey
    xsecval = xsecdict[xseckey]
    #print LambdaU, spin, xsecval
    mrange = massrange.replace('-', '_')
    classname = "Classdu%s_LU%s_spin%s%s" %(du_tag, LambdaU, spin, mrange)
    print classname
#print xsecdict

    #Dictionaries for Templates replacements
    an_func = "analyze_%s" %(classname)
    rep = {'ClassANGGJets': classname, "xsecvalue": xsecval, "outputfile": dset[:-14], "spin": spin, "inputTree": dset, "analyzefunc": an_func}
    #print dset
    #print rep

    #Read and replace template file
    C_src = Template(open(class_Ctemp).read())
    C_sub = C_src.substitute(rep)

    h_src = Template(open(class_htemp).read())
    h_sub = h_src.substitute(rep)

    an_src = Template(open(run_analyzetemp).read())
    an_sub = an_src.substitute(rep)

    #write to file
    #os.chdir("MakeClassFiles")
    outfile_C = open("%s.C" %(classname), "w+")
    outfile_C.write(C_sub)

    outfile_h = open("%s.h" %(classname), "w+")
    outfile_h.write(h_sub)

    outfile_an = open("analyze_%s.C" %(classname), "w+")
    outfile_an.write(an_sub)

def RunAnalyze(file_list):
	for anFile in file_list:
		if anFile.startswith("analyze_Class") and anFile.endswith(".C"):
			root_cmd = "root -l -q %s" %(anFile)
			os.system(root_cmd)
def DelClassFiles(file_list):
    for classFile in file_list:
        if "Classdu1p" in classFile:
            del_cmd = "rm %s" %(classFile)
            print del_cmd
            os.system(del_cmd)

#RunAnalyze(os.listdir('.'))
DelClassFiles(os.listdir('.'))

sw.Stop()
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time:  " + str(sw.CpuTime() / 60.0) + " minutes"
