##############################################
# now variables to plot
# Include also variables to be plotted
res_cuts = [ c for c in cuts if 'res' in c]
boost_cuts = [ c for c in cuts if 'boost' in c]
sig_cuts =  [ c for c in cuts if 'sig' in c]

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

########################
variables['Mww'] = {   'name': 'Mww',      
                        'range' : (60,0,5000),  
                        'xaxis' : 'Mww', 
                        'fold' : 3,
                         #'blind': [1000,2000]
                        }

variables['Mww_20'] = {   'name': 'Mww',      
                        'range' : (20,0,5000),  
                        'xaxis' : 'Mww', 
                        'fold' : 3,
                         #'blind': [1000,2000]
                        }

variables['Mww_binzv'] = {   'name': 'Mww',      
                        'range' : ([200.,300.,400.,500.,600., 700.,800.,900., 1000., 1250., 1500., 2000., 2500.],), #variable range  
                        'xaxis' : 'Mww', 
                        'fold' : 3,
                         #'blind': [1000,2000]
                        }

variables['mjjVsMww_binzv'] = {   'name': 'mjj_vbs:Mww',      
                        'range' : ([500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200, 1225, 1250, 1275, 1300, 1325, 1350, 1375, 1400, 1425, 1450, 1475, 1500, 1525, 1550, 1575, 1600, 1625, 1650, 1675, 1700, 1725, 1750, 1775, 1800, 1825, 1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075, 2100, 2125, 2150, 2175, 2200, 2225, 2250, 2275, 2300, 2325, 2350, 2375, 2400, 2425, 2450, 2475, 2500, 2525, 2550, 2575, 2600, 2625, 2650, 2675, 2700, 2725, 2750, 2775, 2800, 2825, 2850, 2875, 2900, 2925, 2950, 2975, 3000, 3025, 3050, 3075, 3100, 3125, 3150, 3175, 3200, 3225, 3250, 3275, 3300, 3325, 3350, 3375, 3400, 3425, 3450, 3475,3500],[200.,300.,400.,500.,600., 700.,800.,900., 1000., 1250., 1500., 2000., 2500.],), #variable range  
                        'xaxis' : 'M_{jj} VBS : Mww', 
                        'fold' : 3,
                         #'blind': [1000,2000]
                        }

variables['DNNoutput_res_v1'] = {
    'name': 'DNNoutput_resolved_v1',
    'range': (25,0.,1),
    'xaxis': 'DNN resolved',
    'fold': 3 ,
    'cuts':  res_cuts,
    'divideByBinWidth': True, 
    # 'blind': { c:[0.6,1] for c in cuts if "_sig_" in c},
}

'''
variables['DNNoutput_res_v2'] = {
    'name': 'DNNoutput_resolved_v1',
    'range': ([i*0.04 for i in range(20) ] + [0.8+0.025*i for i in range(9)],),
    'xaxis': 'DNN resolved',
    'fold': 3 ,
    'cuts':  res_cuts,
Configurations/VBSjjlnu/Full2018v7/conf_fit_v4.5/variables_weights.py    'divideByBinWidth': True, 
    # 'blind': { c:[0.6,1] for c in cuts if "_sig_" in c},
}
'''

variables['DNNoutput_boost'] = {
    'name': 'DNNoutput_boosted',
    'range': ([0., 0.05, 0.1, 0.15, 0.20, 0.25, 0.3, 0.35, 0.4, 0.55, 0.7, 0.85, 1.],),
    'xaxis': 'DNN boosted',
    'fold': 3 ,
    'cuts': boost_cuts,
    'divideByBinWidth': True,
    # 'blind': { c:[0.6,1] for c in cuts if "_sig_" in c} ,
}

#####################
#Fit variables

variables['fit_bins_res'] ={  'name' : 'fit_bin_res',
                            'range' : (21,1,22),
                            'xaxis' : 'Wjets resolved bin', 
                            'fold' : 0,
                            'cuts': res_cuts
}   

variables['fit_bins_boost'] ={  'name' : 'w_lep_pt',
                            'range' : ([0,50,100,150,200,300,400,600],),
                            'xaxis' : 'W leptonic Pt', 
                            'fold' : 3,
                            'cuts': boost_cuts
}   

######################

variables['w_lep_pt'] = {   'name': 'w_lep_pt',      
                        'range' : (40,0,600),  
                        'xaxis' : 'Pt W leptonic', 
                        'fold' : 3
                        }

variables['vbs_1_pt_res'] = {   'name': 'vbs_1_pt',      
                        'range' : (15,30,250),  
                        'xaxis' : 'trailing VBS jet pt', 
                        'fold' : 3,
                        'cuts': res_cuts
} 

variables['vbs_1_pt_res_morebins'] = {   'name': 'vbs_1_pt',      
                        'range' : (30,30,250),  
                        'xaxis' : 'trailing VBS jet pt', 
                        'fold' : 3,
                        'cuts': res_cuts
} 

variables['vbs_1_pt_boost'] = {   'name': 'vbs_1_pt',      
                        'range' : (15,30,200),  
                        'xaxis' : 'trailing VBS jet pt', 
                        'fold' : 3,
                        'cuts':  boost_cuts
                        } 


variables['deltaeta_vbs'] = {   'name': 'deltaeta_vbs',      
                        'range' : (20,2.5,8.5),  
                        'xaxis' : '#Delta#eta VBS jets', 
                        'fold' : 3,
                        }    


variables['mjj_vjet_res'] = {   'name': 'mjj_vjet',      
                        'range' : (30,65,105),  
                        'xaxis' : 'Whad reco mass', 
                        'fold' : 3,
                        'cuts' : [c for c in res_cuts if 'wjetcr' not in c] 
                        }

variables['mjj_vjet_boost'] = {   'name': 'mjj_vjet',      
                        'range' : (15,70,115),  
                        'xaxis' : 'Whad reco mass', 
                        'fold' : 3,
                        'cuts' : [c for c in boost_cuts  if 'wjetcr' not in c] 
                        }

variables['mjj_vjet_wjetcr'] = {   'name': 'mjj_vjet',      
                        'range' : (50,40,250),  
                        'xaxis' : 'Whad reco mass', 
                        'fold' : 3,
                        'cuts' : [c for c in cuts if 'wjetcr' in c]
                        }

variables['mjj_vbs'] = {   'name': 'mjj_vbs',      
                        'range' : (25,500,3500) , 
                        'xaxis' : 'M_{jj} VBS', 
                        'fold' : 3,
                        #'blind':  { c: [1500,3000] for c in cuts if 'sig' in c} ,
                    }

variables['nJets_res'] = {   'name': 'nJets30',      
                        'range' : (6,4,10),  
                        'xaxis' : 'nJets cleaned from Ak8 >= 30 GeV', 
                        'fold' : 3,
                        'cuts': res_cuts
                        }

variables['nJets_boost'] = {   'name': 'nJets30',      
                        'range' : (6,2,8),  
                        'xaxis' : 'nJets cleaned from Ak8 >= 30 GeV', 
                        'fold' : 3,
                        'cuts':boost_cuts
                        }


variables['Zlep'] = {   'name': 'Zlep',      
                        'range' : (25,-1,1),  
                        'xaxis' : 'Zepp. lepton', 
                        'fold' : 3,
                        }

variables['Zvjets_0'] = {   'name': 'Zvjets_0',      
                        'range' : (20,-1,1),  
                        'xaxis' : 'Zepp. lepton', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }


variables['vbs_0_qgl_res'] = {  'name': 'vbs_0_qgl_res',
                        'range': (26,-0.04,1.),
                        'xaxis': 'Qgl VBS 0 jet',
                        'fold': 3,
                        'cuts':  [c for c in sig_cuts if "res" in c]
                }

variables['vjet_0_qgl_res'] = {  'name': 'vjet_0_qgl_res',
                        'range': (26,-0.04,1.),
                        'xaxis': 'Qgl Vjet 0 jet',
                        'fold': 3,
                        'cuts':  [c for c in sig_cuts if "res" in c]
                }

variables['vjet_1_qgl_res'] = {  'name': 'vjet_1_qgl_res',
                        'range': (26,-0.04,1.),
                        'xaxis': 'Qgl Vjet 1 jet',
                        'fold': 3,
                        'cuts': [c for c in sig_cuts if "res" in c]
                }


variables['vbs_0_qgl_boost'] = {  'name': 'vbs_0_qgl_boost',
                        'range': (26,-0.04,1.),
                        'xaxis': 'Qgl VBS 0 jet',
                        'fold': 3,
                        'cuts':  [c for c in sig_cuts if "boost" in c]
                }


variables['vbs_0_pt'] = {   'name': 'vbs_0_pt',      
                        'range' : (35,50,400),  
                        'xaxis' : 'leading VBS jet pt', 
                        'fold' : 3
                        } 


variables['vjet_0_pt'] = {   'name': 'vjet_0_pt',      
                        'range' : (20,30,180),  
                        'xaxis' : 'leading V-jet pt', 
                        'fold' : 3,
                        'cuts': [c for c in sig_cuts if "res" in c]
                        }


variables['whad_pt_boost'] = {  'name': "w_had_pt",
                                'range': (20, 200, 600),
                                'xaxis': 'W hadronic Pt',
                                'fold': 3 ,
                                'cuts': [c for c in boost_cuts if 'sig' in c]
                            }


variables['vjet_1_pt'] = {   'name': 'vjet_1_pt',      
                        'range' : (20,30,100),  
                        'xaxis' : 'trailing V-jet pt', 
                        'fold' : 3,
                        'cuts': [c for c in sig_cuts if "res" in c]
                        }


variables['deltaphi_vbs'] = {   'name': 'deltaphi_vbs',      
                        'range' : (20,0,3.14),  
                        'xaxis' : '#Delta#phi VBS jets', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }


variables['Lepton_eta'] = {   'name': 'Lepton_eta[0]',      
                        'range' : (30,-2.5,2.5),  
                        'xaxis' : 'Lepton #eta', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }

variables['Lepton_pt'] = {   'name': 'Lepton_pt[0]',      
                        'range' : (20,25,400),  
                        'xaxis' : 'Lepton pt', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }   



variables['Centr_ww'] = {   'name': 'Centr_ww',      
                        'range' : (30,-3,3),  
                        'xaxis' : 'W boson centrality', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }


variables['deltaeta_vjet'] = {   'name': 'deltaeta_vjet',      
                        'range' : (20,0,2),  
                        'xaxis' : '#Delta#eta V jets', 
                        'fold' : 3,
                        'cuts': [c for c in sig_cuts if "res" in c]
                        }   

# variables['Mww'] = {   'name': 'Mww',      
#                         'range' : (30,0,5000),  
#                         'xaxis' : 'Mww', 
#                         'fold' : 3,
#                          #'blind': [1000,2000]
#                         }
# variables['run_info_boost'] = {
#     'tree':  {"run":"run","lumi":"luminosityBlock","event":"event", "DNN":"DNNoutput_boosted"},
#     'cuts' : ['boost_sig_ele', 'boost_sig_mu']
# }

# variables['run_info_res'] = {
#     'tree':  {"run":"run","lumi":"luminosityBlock","event":"event", "DNN":"DNNoutput_resolved_v1"},
#     'cuts' : ['res_sig_ele', 'res_sig_mu']
# }


#variables = {k:v for k,v in variables.items() if k in ["events", "DNNoutput_res_v1", "DNNoutput_boost", "fit_bins_res","fit_bins_boost"]}
variables = {k:v for k,v in variables.items() if "mjjVsMww_binzv" not in k}
#variables = {k:v for k,v in variables.items() if k in ["events"]}