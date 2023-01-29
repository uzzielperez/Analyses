import fileinput

f = "../CP2UnparticlesPythia8fragments-2018PSWeights/UnparToGG_Spin2_du1p9_LambdaU-3500_pT70_M500-1000_TuneCP2_13TeV_pythia8_cfi.py"

import re

find_replace = {

	'from Configuration.Generator.MCTunes2017.PythiaCP2Settings_cfi import *' : 'from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *',
        'from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *' : '',
}
 



findlines = open(f).read().split('\n')
replacelines = open('replace.txt').read().split('\n')
find_replace = dict(zip(findlines, replacelines))



with open('data.txt') as data:
    with open('new_data.txt', 'w') as new_data:
        for line in data:
            for key in find_replace:
                if key in line:
                    line = line.replace(key, find_replace[key])
            new_data.write(line)


with open('data.txt') as data:
    with open('new_data.txt', 'w') as new_data:
        for line in data:
            for key in find_replace:
                if key in line:
                    line = line.replace(key, find_replace[key])
            new_data.write(line) =open(f)


fin.close()
fout.close()



