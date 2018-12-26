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

DATASET = []
doqcdTest = True

#Templates
class_Ctemp = "ClassTemplateisEBEB.C"
class_htemp = "ClassTemplateisEBEB.h"
run_analyzetemp = "analyzeTemplate.C"


xsecdict = {}

if doqcdTest:
    du_tag = ""
    DATASET.append("Testqcd_gg2qqbar_TuneCP2_py_GEN.root/demo/fgenTree")
    DATASET.append("Testqcd_qqbar2gg_TuneCP2_py_GEN.root/demo/fgenTree")

    xsecdict_temp = {"qcd_gg2qqbar_TuneCP2_py": 5.146e+03+-8.786e+01,
                     "qcd_qqbar2gg_TuneCP2_py" : 7.496e+02+-1.233e+01}
    xsecdict.update(xsecdict_temp)
for dset in DATASET:
    pattern = "qcd_([^(]*)_TuneCP2_py"
    match = re.findall(pattern, dset)
    proc = match[0]
    print match

    keypattern = "Test([^(]*)_GEN.root"
    matchkey = re.findall(keypattern, dset)
    xseckey = matchkey[0]

    classname = "Class_%s" %(proc)
    an_func = "analyze_%s" %(classname)
    xsecval = xsecdict[xseckey]
    outfile = "%s.root" %(proc)
        #rep = {'ClassANGGJets': classname, "xsecvalue": xsecval, "outputfile": outfile, "spin": spin, "inputTree": dset, "analyzefunc": an_func}

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
