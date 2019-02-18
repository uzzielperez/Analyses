import os
import re
from string import Template

# Run Combine and Collect Linits
print "Running combine..."
os.system("./run_combine.sh")
harvest_cmd = "../../../CombineHarvester/CombineTools/scripts/combineTool.py -M CollectLimits higgsCombine*.AsymptoticLimits.mH*root"
print "Harvesting combine outputs..."
os.system(harvest_cmd)

# Format output json from harvester
format_limits_cmd = "python ../hep_combine/limits_formatter.py -i limits.json"
os.system(format_limits_cmd)

# Write plotting script from inputs
plot_limits_template   = open("../hep_combine/limits_plotter.py").read()
LambdaU_list = []
for filename in os.listdir('.'):
    if filename.startswith("unpar_spin") and filename.endswith(".txt"):
	card = filename
        pattern = "unpar_spin([^(]*)_du([^(]*)_LU([^(]*)_intlumi([^(]*).txt"
        match = re.findall(pattern, card)
        spin, du, LU, intlumi = match[0]
        LambdaU_list.append(float(LU))

d = {'LambdaU_list':LambdaU_list, 'du':du.replace('p','.'),'du_label':du, 'spin':spin, 'intlumi':intlumi}
pltfile = open('plotlimits.py', 'w+')
src     = Template(plot_limits_template)
sub     = src.substitute(d)
pltfile.write(sub)
pltfile.close()

# Plot
plt_cmd = "python plotlimits.py"
os.system(plt_cmd)
