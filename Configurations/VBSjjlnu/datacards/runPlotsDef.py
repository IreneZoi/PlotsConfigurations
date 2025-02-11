#! /cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_1_0_pre4/external/el9_amd64_gcc12/bin/python3

from itertools import combinations
import sys 
import os 
import json

point_mode = {
    1: 100,
    2: 10000,
    3: 100
}


if __name__ == "__main__":

    # mode indicates if we want 1d, 2d or Nd workspaces
    # with N the number of operators
    mode__ = int(sys.argv[1])
    
    with open('metadata.json') as file:
        metadata = json.load(file)

    ops = metadata["operators"].keys()

    if mode__ == 3: mode__ = len(ops)

    # create a list whose entries will contain the 
    # operators for which we want to create the workspace
    combos = list(combinations(ops, mode__))

    cmds = []
    for c in combos:
        ops = " ".join([f"k_{op}" for op in c])
        name = "_".join(c)
        fn = f"higgsCombine.{name}.individual.MultiDimFit.mH125.root"
        if not os.path.isfile(fn): continue
        cmds.append("mkEFTScan.py " + f"{fn} -p {ops} -maxNLL 10 -lumi 138 -cms -preliminary -o scan_{name}")
        
    for command in cmds:
        os.system(command)
