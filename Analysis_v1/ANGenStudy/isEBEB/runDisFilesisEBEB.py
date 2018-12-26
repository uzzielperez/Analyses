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

do1p93Test = False
doMCTest = False
doMCPlusTest = True


#Templates
class_Ctemp = "ClassTemplateisEBEB.C"
class_htemp = "ClassTemplateisEBEB.h"
run_analyzetemp = "analyzeTemplate.C"

xsecdict = {}
if doMCPlusTest:
    du_tag = ""
    #DATASET.append("TesttMCIPlus2_Unp-LU4000-du1p8_spin-2-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TesttMCIPlus2_Unp-LU3000-du1p4_spin-2-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TesttMCIPlus2_Unp-LU4250-du1p1_spin-2-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TesttMCIPlus2_Unp-LU4000-du1p5_spin-2-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TesttMCIPlus2_Unp-LU3750-du1p1_spin-2-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TesttMCIPlus2_Unp-LU3500-du1p4_spin-2-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TesttMCIPlus2_Unp-LU3000-du1p1_spin-2-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCIPlus2_Unp-LU5000-du1p01_spin-2-ggON_pT125_M_1500_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCIPlus2_Unp-LU4500-du1p01_spin-2-ggON_pT125_M_1000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCIPlus2_Unp-LU4500-du1p01_spin-2-ggON_pT125_M_1500_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCIPlus2_Unp-LU4750-du1p01_spin-2-ggON_pT125_M_1500_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCIPlus2_Unp-LU4500-du1p9_spin-2-ggON_pT125_M_1500_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCIPlus2_Unp-LU4500-du1p9_spin-2-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCIPlus2_Unp-LU2500-du1p9_spin-2-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCIPlus2_Unp-LU4000-du1p9_spin-2-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")

   # DATASET.append("TestMCIPlus0_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_1000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCIPlus0_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_1500_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCIPlus2_Unp-LU500-du1p8_spin-2-ggON_pT125_M_1000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCIPlus2_Unp-LU500-du1p8_spin-2-ggON_pT125_M_1500_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCIPlus_SM_pT125_M_1000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCIPlus_SM_pT125_M_1500_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCIPlus_SM_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")

    xsecdict_temp = {"MCIPlus_SM_pT125_M_2000_TuneCP2_py":	5.312e-04+-2.734e-06,
    "MCIPlus_SM_pT125_M_1000_TuneCP2_py":	1.068e-02+-5.607e-05,
    "MCIPlus0_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_1000_TuneCP2_py":	1.175e-02+-6.217e-05,
    "MCIPlus2_Unp-LU500-du1p8_spin-2-ggON_pT125_M_1000_TuneCP2_py" :  1.282e-02+-6.459e-05, #1.282e-02+-6.459e-05
    "MCIPlus2_Unp-LU4500-du1p01_spin-2-ggON_pT125_M_1000_TuneCP2_py" : 9.450e-03 +- 5.049e-05,
    "MCIPlus2_Unp-LU5000-du1p01_spin-2-ggON_pT125_M_1500_TuneCP2_py" : 1.777e-03 +- 9.420e-06,
    "MCIPlus_SM_pT125_M_1500_TuneCP2_py":	2.073e-03+-1.081e-05,
    "MCIPlus0_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_1500_TuneCP2_py":	2.943e-03+-1.584e-05,
    "MCIPlus2_Unp-LU500-du1p8_spin-2-ggON_pT125_M_1500_TuneCP2_py" :  3.629e-03+-1.921e-05, #3.629e-03+-1.921e-05
    "MCIPlus2_Unp-LU4500-du1p01_spin-2-ggON_pT125_M_1500_TuneCP2_py" : 9.450e-03 +- 5.049e-05,
    "MCIPlus2_Unp-LU4750-du1p01_spin-2-ggON_pT125_M_1500_TuneCP2_py" : 1.796e-03 +- 9.600e-06,
    "MCIPlus2_Unp-LU4500-du1p9_spin-2-ggON_pT125_M_1500_TuneCP2_py" : 2.095e-03 +- 1.094e-05,
    "MCIPlus2_Unp-LU4500-du1p9_spin-2-ggON_pT125_M_2000_TuneCP2_py" : 5.399e-04 +- 2.767e-06,
    "MCIPlus2_Unp-LU2500-du1p9_spin-2-ggON_pT125_M_2000_TuneCP2_py" : 6.440e-04 +- 3.169e-06,
    "MCIPlus2_Unp-LU4000-du1p9_spin-2-ggON_pT125_M_2000_TuneCP2_py" : 5.457e-04 +- 2.791e-06,
    "MCIPlus2_Unp-LU3000-du1p4_spin-2-ggON_pT125_M_2000_TuneCP2_py": 5.290e-04+-2.685e-06,
    "MCIPlus2_Unp-LU3750-du1p1_spin-2-ggON_pT125_M_2000_TuneCP2_py": 4.554e-04+-2.338e-06,
    "MCIPlus2_Unp-LU3500-du1p4_spin-2-ggON_pT125_M_2000_TuneCP2_py": 5.246e-04+-2.687e-06,
    "MCIPlus2_Unp-LU3000-du1p1_spin-2-ggON_pT125_M_2000_TuneCP2_py": 5.357e-04+-2.684e-06,
    "MCIPlus2_Unp-LU4000-du1p8_spin-2-ggON_pT125_M_2000_TuneCP2_py": 5.451e-04+-2.775e-06,
    "MCIPlus2_Unp-LU4250-du1p1_spin-2-ggON_pT125_M_2000_TuneCP2_py": 4.535e-04+-2.350e-06,
    "MCIPlus2_Unp-LU4000-du1p5_spin-2-ggON_pT125_M_2000_TuneCP2_py": 5.336e-04 +- 2.716e-06,
}
    xsecdict.update(xsecdict_temp)
if doMCTest:
    du_tag = ""
    DATASET.append("TestMCI_SM_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCI_SM_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0-ggON_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    #DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCI_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCI_Unp-LU500-du1p8_spin-2-ggON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("TestMCI_Unp-LU500-du1p8_spin-2-ggON_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-2-ggffON_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-2-ggffON_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-2_pT125_M_2000_TuneCP2_py_GEN.root/demo/fgenTree")
    # DATASET.append("TestMCI_Unp-LU500-du1p8_spin-2_pT125_M_500-2000_TuneCP2_py_GEN.root/demo/fgenTree")
    xsecdict_temp = {"MCI_SM_pT125_M_500-2000_TuneCP2_py":	9.799e-02+-4.831e-04,
                     "MCI_Unp-LU500-du1p8_spin-2-ggON_pT125_M_500-2000_TuneCP2_py":	9.947e-02+-4.855e-04,
                     "MCI_Unp-LU500-du1p8_spin-2-ggffON_pT125_M_500-2000_TuneCP2_py":	1.959e-01+-9.612e-04,
                     "MCI_Unp-LU500-du1p8_spin-2_pT125_M_500-2000_TuneCP2_py":	9.517e-02+-4.627e-04,
                     "MCI_Unp-LU500-du1p8_spin-0_pT125_M_500-2000_TuneCP2_py":	5.584e-03+-3.052e-05,
                     "MCI_Unp-LU500-du1p8_spin-0-ggON_pT125_M_500-2000_TuneCP2_py":	5.584e-03+-3.052e-05,
                     "MCI_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_500-2000_TuneCP2_py":	9.977e-02+-4.908e-04,
                     "MCI_SM_pT125_M_2000_TuneCP2_py":	  5.312e-04+-2.734e-06,
                     "MCI_Unp-LU500-du1p8_spin-2-ggON_pT125_M_2000_TuneCP2_py":	1.662e-03+-9.437e-06,
                     "MCI_Unp-LU500-du1p8_spin-2-ggffON_pT125_M_2000_TuneCP2_py":	2.186e-03+-1.208e-05,
                     "MCI_Unp-LU500-du1p8_spin-2_pT125_M_2000_TuneCP2_py":	1.650e-03+-9.361e-06,
                     "MCI_Unp-LU500-du1p8_spin-0-ggffON_pT125_M_2000_TuneCP2_py":	1.151e-03+-6.490e-06,
                     "MCI_Unp-LU500-du1p8_spin-0_pT125_M_2000_TuneCP2_py":	6.191e-04+-3.766e-06,
                     "MCI_Unp-LU500-du1p8_spin-0-ggON_pT125_M_2000_TuneCP2_py":	6.199e-04+-3.742e-06,
                     }
    xsecdict.update(xsecdict_temp)
for dset in DATASET:
    if "SM" in dset:
        ## TestMCIPlus_SM_pT125_M_2000
        #pattern = "TestMCI_([^(]*)_pT125_M_([^(]*)_TuneCP2_py_GEN"
        pattern = "TestMCIPlus_([^(]*)_pT125_M_([^(]*)_TuneCP2_py_GEN"
        match = re.findall(pattern, dset)
        PH, massrange = match[0]
        #print PH, massrange
    if "Unp" in dset:
        #pattern = "TestMCI_([^(]*)-LU([^(]*)-du([^(]*)_spin-([^(]*)([^(]*)_pT125_M_([^(]*)_TuneCP2_py_GEN"
        if "Plus0" in dset:
            pattern = "TestMCIPlus0_([^(]*)-LU([^(]*)-du([^(]*)_spin-([^(]*)-([^(]*)_pT125_M_([^(]*)_TuneCP2_py_GEN.root"
        if "Plus2" in dset:
            pattern = "TesttMCIPlus2_([^(]*)-LU([^(]*)-du([^(]*)_spin-([^(]*)-([^(]*)_pT125_M_([^(]*)_TuneCP2_py_GEN.root"
        match = re.findall(pattern, dset);
        PH, LambdaU, du, spin, switch, massrange = match[0]
        if LambdaU == '500':
             LambdaU = '1500' #typo
        #print PH, massrange

    print match

    keypattern = "Testt([^(]*)_GEN.root"
    matchkey = re.findall(keypattern, dset)
    xseckey = matchkey[0]
    mrange = massrange.replace('-', '_')
    if "SM" in dset:
        classname = "Class_%s_%s" %(PH, mrange)
        #print classname
        an_func = "analyze_%s" %(classname)
        xsecval = xsecdict[xseckey]
        outfile = "%s_M%s.root" %(PH, mrange)
        #rep = {'ClassANGGJets': classname, "xsecvalue": xsecval, "outputfile": outfile, "spin": spin, "inputTree": dset, "analyzefunc": an_func}
    if "Unp" in dset:
        classname = "Class_%s_LU%s_du%s_spin%s_%s_M%s" %(PH, LambdaU, du, spin, switch, mrange)
        classname = classname.replace('-', '_')
        an_func = "analyze_%s" %(classname)
        outfile = "%s_LU%s_du%s_spin%s_%sM%s.root" %(PH, LambdaU, du, spin, switch, mrange)
        xsecval = xsecdict[xseckey]
        #print classname

    rep = {'ClassANGGJets': classname, "xsecvalue": xsecval, "outputfile": outfile, "inputTree": dset, "analyzefunc": an_func}
    #print outfile

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
        if "Class_" in classFile:
            del_cmd = "rm %s" %(classFile)
            #print del_cmd
            os.system(del_cmd)
    print "deleted auxilliary files"
RunAnalyze(os.listdir('.'))
#DelClassFiles(os.listdir('.'))

sw.Stop()
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time:  " + str(sw.CpuTime() / 60.0) + " minutes"
