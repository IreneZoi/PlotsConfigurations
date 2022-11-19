# structure configuration for datacard
from itertools import product, chain
#structure = {}

wjets_bins = []
for ir in range(1,7):
    wjets_bins.append("Wjets_HT_res_"+str(ir))
for ir in range(1,6):
    wjets_bins.append("Wjets_HT_boost_"+str(ir))


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



structure['DY']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['top']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['VV']  = {  
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

structure['VBF-V']  = {  
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

structure['VBS']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
              }

# data


structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }

# Structure for aqgc

structure['sm'] = {
                  'isSignal' : 1,
                  'isData'   : 0    
                  }

#### EFT ###
# structure['quad_cT0'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0
#                  }
# structure['sm_lin_quad_cT0'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0
#                  }

structure['quad_cT2'] = {
                 'isSignal' : 1,
                 'isData'   : 0    
                 }
structure['sm_lin_quad_cT2'] = {
                 'isSignal' : 1,
                 'isData'   : 0    
                 }


