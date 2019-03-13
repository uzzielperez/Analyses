import os
import re
from string import Template
parser.add_argument("-p", "--plot", action="store_true")



args = parser.parse_args()

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
plot_limits_template   = open("../hep_combine/ADDlimitsPlotter.py").read()
LambdaT_list = []
for filename in os.listdir('.'):
    if filename.startswith("higgsCombine") and filename.endswith(".root"):
	card = filename
        #pattern = "unpar_spin([^(]*)_du([^(]*)_LU([^(]*)_intlumi([^(]*).txt"
        pattern = "higgsCombineADD([^(]*).AsymptoticLimits.mH([^(]*).root"
        match = re.findall(pattern, card)
        KKconv, LambdaT = match[0]
        LambdaT_list.append(float(LambdaT))
        intlumi = 137

d = {'LambdaT_list':LambdaT_list, 'KKconv':KKconv, 'intlumi':intlumi}
pltfile = open('plotlimits.py', 'w+')
src     = Template(plot_limits_template)
sub     = src.substitute(d)
pltfile.write(sub)
pltfile.close()

# Plot
if args.plot:
    plt_cmd = "python plotlimits.py"
    os.system(plt_cmd)
