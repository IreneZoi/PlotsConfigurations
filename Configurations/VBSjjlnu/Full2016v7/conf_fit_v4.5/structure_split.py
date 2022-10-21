# structure configuration for datacard
from itertools import product, chain
#structure = {}

wjets_bins = []
for ir in range(1,22):
    wjets_bins.append("Wjets_res_"+str(ir))
for ir in range(1,8):
    wjets_bins.append("Wjets_boost_"+str(ir))


phase_spaces_boost = [c for c in cuts if "boost" in c]
phase_spaces_res = [c for c in cuts if "res" in c]


for wbin in wjets_bins:
    if 'boost' in wbin:
        structure[wbin] = {
                    'isSignal' : 0,
                    'isData'   : 0 ,
                    'removeFromCuts': phase_spaces_res 
        }
    else:
        structure[wbin] = {
                    'isSignal' : 0,
                    'isData'   : 0 ,
                    'removeFromCuts': phase_spaces_boost 
        }


# structure['Wjets_HT']  = {  
#                   'isSignal' : 0,
#                   'isData'   : 0
#               }

structure['DY']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['top']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

# structure['VV']  = {  
#                   'isSignal' : 0,
#                   'isData'   : 0
#               }
for VV_s in VV_samples:
    structure[VV_s]  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['Fake']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }


structure['VVV']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

# structure['VBF-V']  = {  
#                   'isSignal' : 0,
#                   'isData'   : 0 
#               }

structure['VBF-V_dipole']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['ggWW']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['Vg']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['VgS']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['VBS_WZll']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['VBS_ZZ']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }


# structure['VBS']  = { 
#                   'isSignal' : 1,
#                   'isData'   : 0 
#               }

# structure['VBS_dipoleRecoil']  = { 
#                   'isSignal' : 1,
#                   'isData'   : 0 
#               }

structure['VBS_osWW']  = {  
                  'isSignal' : 1,
                  'isData'   : 0 
              }

structure['VBS_ssWW']  = {  
                  'isSignal' : 1,
                  'isData'   : 0 
              }

structure['VBS_WZjj']  = {  
                  'isSignal' : 1,
                  'isData'   : 0 
              }

# data


structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }


# It seems that this is needed for 2016 comparing the rate parameters that I can reproduce with what is in the full run 2 datacard from Davide /eos/user/d/dvalsecc/www/VBSPlots/FullRun2/datacards/datacards_combined/fullrun2_fit_v4.5.5/run2_all/combined_run2_all.txt
for sample in structure.keys():
    if sample.find("Fake") != -1:
        # Correct the luminosity
        structure[sample]['scaleSampleForDatacard'] = 36.33/35.867

# It seems that this is not needed anymore for 2016 comparing the rate parameters that I can reproduce with what is in the full run 2 datacard from Davide /eos/user/d/dvalsecc/www/VBSPlots/FullRun2/datacards/datacards_combined/fullrun2_fit_v4.5.5/run2_all/combined_run2_all.txt
'''
for sample in structure.values():
    if sample['isData'] != 1:
        # Correct the luminosity
        sample['scaleSampleForDatacard'] = 36.33/35.867
'''