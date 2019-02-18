### Official documentation

[Manual to run combine](https://cms-hcomb.gitbooks.io/combine/content/)

### Standalone compilation in `lxplus`
```
cmsrel CMSSW_8_1_0
cd CMSSW_8_1_0/src
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
source env_standalone.sh
make -j 8; make # second make fixes compilation error of first
```
# USING COMBINE

1.) Setup combine and Combine Harvester.
2.) Prepare datacards in HiggsAnalysis/CombinedLimit directory.
We can provide the mkcard.py script the card template and the yields information. This will create datacards in new directories. Typically, you get one limit plot for each group.
```python

python mkcard.py -t basic_yieldscard_template.txt -i sensitivity_log.csv

```
3.) Run ./run_combine.sh with the prepared datacards. This will output the signal strengths for different confidence levels and higgsCombineTest.AsymptoticLimits*root. Currently uses AsymptoticLimits method but you can edit the flags.
4.) Run Combine Harvester. Output is limits.json.
```bash

../../CombineHarvester/CombineTools/scripts/combineTool.py -M CollectLimits higgsCombineTest.AsymptoticLimits.mH*root

```
5.) Reformat the json file into something readable by the current plotter, written by my friend Wenyu Zhang (Brown U.). (I butchered her work a bit.)
```bash
cd CombineCustomPlt
python limits_formatter.py
```
6.) Plot.

```bash
python plotlimits.py
```

Once the directories are created, you can also go into the directories and run to do the rest of the steps all at once.
```bash

python run_plotter.py

```
Or you could run all the plots at once by:

```bash

python run_limits_sets.py

```

## Output Naming flags
* The option -n allows you to specify part of the name of the rootfile. e.g. if you do -n HWW the roofile will be called higgsCombineHWW.... instead of higgsCombineTest

* The option -m allows you to specify the higgs boson mass, which gets written in the filename and also in the tree (this simplifies the bookeeping because you can merge together multiple trees corresponding to different higgs masses using hadd and then use the tree to plot the value of the limit vs mass) (default is m=120)

* The option -s allows to specify the seed (eg -s 12345) used in toy generation. If this option is given, the name of the file will be extended by this seed, eg higgsCombineTest.AsymptoticLimits.mH120.12345.root

* The option --keyword-value allows you to specify the value of a keyword in the datacard such that $WORD (in the datacard) will be given the value of VALUE in the command --keyword-value WORD=VALUE, eg  higgsCombineTest.AsymptoticLimits.mH120.WORDVALUE.12345.root
