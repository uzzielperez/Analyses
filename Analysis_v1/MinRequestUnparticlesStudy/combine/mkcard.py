import ROOT
import time
import subprocess
import os
import argparse
from string import Template
import math
import csv

## Command Line Options
parser = argparse.ArgumentParser(description='Run Card Settings')
parser.add_argument('-t', '--template', help='Run Card Template. Basic template is default.', type=str,
                    default="basic_yieldscard_template.txt")
parser.add_argument('-i', '--input', help='Input Yields.', type=str,
                    default="sensitivity_log.csv")

args = parser.parse_args()

cardtemplate = args.template
inputfile = args.input


with open(inputfile, mode='r') as infile:
    # Parse Input File line by line and write cards for each line
    csv_file = csv.DictReader(infile)
    row_num = 0
    for line in csv_file:
        B, S = line["B"], line["S"]
        n_obs = B[:2]
        spin, du, LU, intlumi = line["spin"], line["du"], line["LambdaU"], line["intlumi"]

        # Open Template
        filein       = open(cardtemplate)
        card_outName = "unpar_spin%s_du%s_LU%s_intlumi%s.txt" %(spin, du, LU, intlumi)
        print card_outName + "B=%s, S=%s, n_obs=%s" %(B, S, n_obs)
        dir_name = "unpar_spin%s_du%s" %(spin, du)
        d            = {'n_obs':n_obs, 'spin':spin, 'du':du, 'LU':LU, 'intlumi':intlumi,
                        'S':S, 'B':B, 'dir_name':dir_name}

        # Create a directory for each du for spin-0 and spin-2 cases
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            # Create Plotting Script once
            cp_cmd = "cp hep_combine/run_plotter_template.py %s/run_combine_plotter.py" %(dir_name)
            os.system(cp_cmd)

        os.chdir(dir_name)
        fruncombine  = open('run_combine.sh', "a+")
        outfile      = open(card_outName, "w+")
        src          = Template(filein.read())
        sub          = src.substitute(d)

        # Write Cards into appropriate directories
        outfile.write(sub)
        combine_cmd = "combine -m %s -M AsymptoticLimits -n unpar_spin%s_du%s %s > %s \n" %(LU, spin, du, card_outName, "Limit"+card_outName)
        fruncombine.write(combine_cmd)
        outfile.close()
        fruncombine.close()
        os.system("chmod u+x run_combine.sh")

        os.chdir("..")
        filein.close()
        print "Generated %s in %s." %(card_outName, dir_name)
        row_num = row_num + 1
