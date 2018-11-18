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
DATASET.append("TestTestADD_NI-1_LambdaT-10000_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-11000_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-13000_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-4000_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-4500_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-5000_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-5500_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-6000_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-6500_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-7000_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-7500_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-8000_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-8500_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")
# DATASET.append("TestTestADD_NI-1_LambdaT-9000_M-1000_TuneCUEP8M1_13TeV_py_GEN.root/demo/fgenTree")

Class_template = "ClassTemplate.C"
ClassHeader_template = "ClassTemplate.h"
pattern = r'TestADD_NI-1_([^(]*)_M-1000_TuneCUEP8M1_13TeV_py_GEN.root'
xsecdict = {"LambdaT-10000": 7.823e-03+-4.059e-05,
             "LambdaT-11000": 7.708e-03+-4.058e-05,
             "LambdaT-13000": 7.717e-03+-4.010e-05,
             "LambdaT-4000": 2.607e-02+-1.134e-04,
             "LambdaT-4500": 1.565e-02+-6.173e-05,
             "LambdaT-5000": 1.163e-02+-4.952e-05,
             "LambdaT-5500": 9.849e-03+-4.935e-05,
             "LambdaT-6000": 8.970e-03+-4.534e-05,
             "LambdaT-6500": 8.468e-03+-4.300e-05,
             "LambdaT-7000": 8.311e-03+-4.245e-05,
             "LambdaT-7500": 8.151e-03+-4.224e-05,
             "LambdaT-8000": 7.992e-03+-4.144e-05,
             "LambdaT-8500": 7.922e-03+-4.085e-05,
             "LambdaT-9000": 7.886e-03+-4.090e-05}

#Templates
class_Ctemp = "ClassTemplate.C"
class_htemp = "ClassTemplate.h"
run_analyzetemp = "analyzeTemplate.C"


for dset in DATASET:
    match = re.findall(pattern, dset);
    xsecval = xsecdict[match[0]]
    classname = "Class%s" %(match[0].replace("-", "_"))
    #print match[0], " ", xsecval

    #Dictionaries for Templates replacements
    an_func = "analyze_%s" %(classname)
    rep = {'ClassANGGJets': classname, "xsecvalue": xsecval, "LambdaVAL": match[0], "inputTree": dset, "analyzefunc": an_func}
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

    # runAnalyze_cmd = "root -l -q analyze_%s.C" %(classname)
    # print runAnalyze_cmd
    # os.system(runAnalyze_cmd)

def RunAnalyze(file_list):
	for anFile in file_list:
		if anFile.startswith("analyze_ClassLambdaT_") and anFile.endswith(".C"):
			root_cmd = "root -l -q %s" %(anFile)
			os.system(root_cmd)
def DelClassFiles(file_list):
    for classFile in file_list:
        if "ClassLambdaT_" in classFile:
            del_cmd = "rm %s" %(classFile)
            print del_cmd
            os.system(del_cmd)

RunAnalyze(os.listdir('.'))
DelClassFiles(os.listdir('.'))




sw.Stop()
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time:  " + str(sw.CpuTime() / 60.0) + " minutes"
