
import yaml
import os
from subprocess import call

with open("coreutils.yaml", "r") as f:
    coreutils = yaml.load(f)

FNULL = open(os.devnull, "w")

for c, d in coreutils.items():
    if "pre" in d.keys():
        call(d["pre"], stdout=FNULL, shell=True)
    if call(d["bin"] + " " + d["args"], stdout=FNULL, shell=True) == 0:
        print "  [OK]",
    else:
        print "X [KO]",
    print "{}".format(c)
    if "post" in d.keys():
        call(d["post"], stdout=FNULL, shell=True)
