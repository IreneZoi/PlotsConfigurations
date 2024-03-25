# plot configuration
from ROOT import TColor

# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used

colors = {
    # https://root.cern.ch/doc/master/classTColor.html#C02
    'kWhite'   : 0,
    'kBlack'   : 1,
    'kGray'    : 920,
    'kRed'     : 632,
    'kGreen'   : 416,
    'kBlue'    : 600,
    'kYellow'  : 400,
    'kMagenta' : 616,
    'kCyan'    : 432,
    'kOrange'  : 800,
    'kSpring'  : 820,
    'kTeal'    : 840,
    'kAzure'   : 860,
    'kViolet'  : 880,
    'kPink'    : 900, 
}

palette = {
    "Orange": (242, 108, 13), #f26c0d  
    "Yellow": (247, 195, 7), #f7c307
    "LightBlue": (153, 204, 255), #99ccff
    "MediumBlue": (72, 145, 234),  #4891ea
    "MediumBlue2": (56, 145, 224),    #3891e0
    "DarkBlue": (8, 103, 136), #086788
    "Green": (47, 181, 85), #2fb555
    "Green2": (55, 183, 76),  #37b74c
    "LightGreen" : (82, 221, 135), #52dd87
    "Violet": (242, 67, 114), #f24372   
}



#groupPlot['WmTo2J_ZTo2L_aQGC']  = {  
#                  'nameHR' : 'WZ aQGC',
#                  'isSignal' : 1,
#                  'color':   palette["Violet"], #kpink+1
#                  'samples'  : ['WmTo2J_ZTo2L_aQGC' ],#,'WGJJ'
#                  'fill': 1001
#
#              }
#
#groupPlot['WmTo2J_ZTo2L_aQGC_eboliv2']  = {
#                  'nameHR' : 'WZ aQGC (new)',
#                  'isSignal' : 1,
#                  'color':   palette["LightBlue"],
#                  'samples'  : ['WmTo2J_ZTo2L_aQGC_eboliv2'],
#                  'fill': 1001
#
#              }

# groupPlot['sm_FT0']  = {
#                  'nameHR' : '',
#                  'isSignal' : 2,
#                  'color':  palette["Orange"],
#                  'samples'  : ['sm_FT0'],
#                  'fill': 1001
#              }

groupPlot['sm_FT0_WmToLNu_ZTo2J']  = {
                 'nameHR' : 'FT0_WmLNu_Z2J',
                 'isSignal' : 2,
                 'color':  colors["kOrange"]+1,
                 'samples'  : ['sm_FT0_WmToLNu_ZTo2J'],
                 'fill': 1001
             }
groupPlot['sm_FT0_WpToLNu_ZTo2J']  = {
                 'nameHR' : 'FT0_WpLNu_Z2J',
                 'isSignal' : 2,
                 'color':  colors["kOrange"]+2,
                 'samples'  : ['sm_FT0_WpToLNu_ZTo2J'],
                 'fill': 1001
             }
groupPlot['sm_FT0_WmToLNu_WmTo2J']  = {
                 'nameHR' : 'FT0_WmLNu_Wm2J',
                 'isSignal' : 2,
                 'color':  colors["kOrange"]+3,
                 'samples'  : ['sm_FT0_WmToLNu_WmTo2J'],
                 'fill': 1001
             }
groupPlot['sm_FT0_WpToLNu_WmTo2J']  = {
                 'nameHR' : 'FT0_WpLNu_Wm2J',
                 'isSignal' : 2,
                 'color':  colors["kOrange"]+4,
                 'samples'  : ['sm_FT0_WpToLNu_WmTo2J'],
                 'fill': 1001
             }
groupPlot['sm_FT0_WpTo2J_WmToLNu']  = {
                 'nameHR' : 'FT0_Wp2J_WmLNu',
                 'isSignal' : 2,
                 'color':  colors["kOrange"]+5,
                 'samples'  : ['sm_FT0_WpTo2J_WmToLNu'],
                 'fill': 1001
             }
groupPlot['sm_FT0_WpToLNu_WpTo2J']  = {
                 'nameHR' : 'FT0_WpLNu_Wp2J',
                 'isSignal' : 2,
                 'color':  colors["kOrange"]+6,
                 'samples'  : ['sm_FT0_WpToLNu_WpTo2J'],
                 'fill': 1001
             }




groupPlot['sm_dipole_WmToLNu_ZTo2J']  = {
                 'nameHR' : 'dipole_WmLNu_Z2J',
                 'isSignal' : 2,
                 'color':  colors["kBlue"]+1,
                 'samples'  : ['sm_dipole_WmToLNu_ZTo2J'],
                 'fill': 1001
             }
groupPlot['sm_dipole_WpToLNu_ZTo2J']  = {
                 'nameHR' : 'dipole_WpLNu_Z2J',
                 'isSignal' : 2,
                 'color':  colors["kBlue"]+2,
                 'samples'  : ['sm_dipole_WpToLNu_ZTo2J'],
                 'fill': 1001
             }
groupPlot['sm_dipole_WmToLNu_WmTo2J']  = {
                 'nameHR' : 'dipole_WmLNu_Wm2J',
                 'isSignal' : 2,
                 'color':  colors["kBlue"]+3,
                 'samples'  : ['sm_dipole_WmToLNu_WmTo2J'],
                 'fill': 1001
             }
groupPlot['sm_dipole_WpToLNu_WmTo2J']  = {
                 'nameHR' : 'dipole_WpLNu_Wm2J',
                 'isSignal' : 2,
                 'color':  colors["kBlue"]+4,
                 'samples'  : ['sm_dipole_WpToLNu_WmTo2J'],
                 'fill': 1001
             }
groupPlot['sm_dipole_WpTo2J_WmToLNu']  = {
                 'nameHR' : 'dipole_Wp2J_WmLNu',
                 'isSignal' : 2,
                 'color':  colors["kBlue"]+5,
                 'samples'  : ['sm_dipole_WpTo2J_WmToLNu'],
                 'fill': 1001
             }
groupPlot['sm_dipole_WpToLNu_WpTo2J']  = {
                 'nameHR' : 'dipole_WpLNu_Wp2J',
                 'isSignal' : 2,
                 'color':  colors["kBlue"]+6,
                 'samples'  : ['sm_dipole_WpToLNu_WpTo2J'],
                 'fill': 1001
             }



# groupPlot['sm_FT1']  = {
#                   'nameHR' : 'sm_FT1',
#                   'isSignal' : 2,
#                   'color': palette["LightBlue"],    # kGray + 1
#                   'samples'  : ['sm_FT1']
# }




# groupPlot['sm_dipole']  = {
#                  'nameHR' : 'dipole',
#                  'isSignal' : 2,
#                  'color': palette["DarkBlue"],
#                  'samples'  : ['sm_dipole'],
#                  'fill': 1001
#               }
            
# groupPlot['sm_FT2']  = {
#                 'nameHR' : 'sm_FT2',
#                 'isSignal' : 2,
#                 'color': palette["Violet"],
#                 'samples'  : ['sm_FT2'],
#                 'fill': 1001
#              }

#groupPlot['sm_global']  = {
#                 'nameHR' : 'VBS ewk global',
#                 'isSignal' : 1,
#                 'color': colors["kRed"],
#                 'samples'  : ['sm_global'],
#                 'fill': 1001
#              }


# plot['sm_FT2']  = { 
#                   'color': colors["kOrange"],    
#                   'isSignal' : 1,
#                   'isData'   : 0,
#                   'scale'    : 1.0
#                   }


plot['sm_FT0_WmToLNu_ZTo2J'] = {   
                 'color': colors['kAzure'],
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }


plot['sm_FT0_WpToLNu_ZTo2J'] = {   
                 'color': colors['kAzure'],
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }
plot['sm_FT0_WpToLNu_WpTo2J'] = {   
                 'color': colors['kAzure'],
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }
plot['sm_FT0_WmToLNu_WmTo2J'] = {   
                 'color': colors['kAzure'],
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }
plot['sm_FT0_WpToLNu_WmTo2J'] = {   
                 'color': colors['kAzure'],
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }
plot['sm_FT0_WpTo2J_WmToLNu'] = {   
                 'color': colors['kAzure'],
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }
# plot['sm_FT0'] = {   
#                  'color': colors['kAzure'],
#                  'isSignal' : 1,
#                  'isData'   : 0, 
#                  'scale'    : 1.
#         }

#plot['WmTo2J_ZTo2L_aQGC']  = {
#                  'color':  colors['kRed']-3,
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#              }

# plot['sm_dipole']  = {
#                   'color': colors["kRed"], 
#                   'isSignal' : 1,
#                   'isData'   : 0,
#                   'scale'    : 1.   
#               }

plot['sm_dipole_WmToLNu_ZTo2J'] = {   
                 'color': colors['kAzure'],
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }


plot['sm_dipole_WpToLNu_ZTo2J'] = {   
                 'color': colors['kAzure'],
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }
plot['sm_dipole_WpToLNu_WpTo2J'] = {   
                 'color': colors['kAzure'],
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }
plot['sm_dipole_WmToLNu_WmTo2J'] = {   
                 'color': colors['kAzure'],
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }
plot['sm_dipole_WpToLNu_WmTo2J'] = {   
                 'color': colors['kAzure'],
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }
plot['sm_dipole_WpTo2J_WmToLNu'] = {   
                 'color': colors['kAzure'],
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }

#plot['WmTo2J_ZTo2L_aQGC_eboliv2']  = {
#                  'color': colors["kCyan"]+2,
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1.   
#              }
#
#plot['WGJJ']= { 'color': colors["kCyan"]+4,
#                'isSignal' : 0,
#                'isData'   : 0,
#                'scale'    : 1.   
#            }

# plot['sm_FT1']  = {  
#                 'color': colors['kGreen'],
#                 'isSignal' : 1,
#                 'isData'   : 0, 
#                 'scale'    : 1.0
#             }

# additional options

legend['lumi'] = 'L = 59.74/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
