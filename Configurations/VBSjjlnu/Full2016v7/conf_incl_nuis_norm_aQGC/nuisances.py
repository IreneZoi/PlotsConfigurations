# nuisances
# # # name of samples here must match keys in samples.py 

mc =["DY", "top",  "Wjets_HT", "VV", "VVV", "VBF-V", "Vg", "VgS", "VBS", "ggWW"]
# mc_norm = [m for m in mc if m not in ["VBS", "VV"]]
# mc_sep =  ["VBS", "VV"]
mc = ["sm",
    "quad_cT0","sm_lin_quad_cT0",
    "quad_cT1","sm_lin_quad_cT1",
    "quad_cT2","sm_lin_quad_cT2",
    "quad_cT3","sm_lin_quad_cT3",
    "quad_cT4","sm_lin_quad_cT4",
    "quad_cT5","sm_lin_quad_cT5",
    "quad_cT6","sm_lin_quad_cT6",
    "quad_cT7","sm_lin_quad_cT7",
    "quad_cT8","sm_lin_quad_cT8",
    "quad_cT9","sm_lin_quad_cT9",
    "quad_cS0","sm_lin_quad_cS0",
    "quad_cS1","sm_lin_quad_cS1",
    "quad_cM0","sm_lin_quad_cM0",
    "quad_cM1","sm_lin_quad_cM1",
    "quad_cM2","sm_lin_quad_cM2",
    "quad_cM3","sm_lin_quad_cM3",
    "quad_cM4","sm_lin_quad_cM4",
    "quad_cM5","sm_lin_quad_cM5",
    "quad_cM7","sm_lin_quad_cM7"
    ]
def getSamplesWithout(samples, samples_to_remove):
    return [m for m in samples if m not in samples_to_remove]

phase_spaces_boost = [ c for c in cuts if 'boost' in c]
phase_spaces_res = [ c for c in cuts if 'res' in c]

phase_spaces_res_ele = [ c for c in phase_spaces_res if 'ele' in c]
phase_spaces_res_mu = [ c for c in phase_spaces_res if 'mu' in c]
phase_spaces_boost_ele = [ c for c in phase_spaces_boost if 'ele' in c]
phase_spaces_boost_mu =  [ c for c in phase_spaces_boost if 'mu' in c]

phase_spaces_tot_ele = phase_spaces_res_ele + phase_spaces_boost_ele
phase_spaces_tot_mu = phase_spaces_res_mu + phase_spaces_boost_mu
phase_spaces_tot_res = phase_spaces_res_ele + phase_spaces_res_mu
phase_spaces_tot_boost = phase_spaces_boost_ele + phase_spaces_boost_mu

phase_spaces_dict = {"boost": phase_spaces_boost, "res": phase_spaces_res}
phase_spaces_tot = phase_spaces_tot_ele + phase_spaces_tot_mu


# # ################################ EXPERIMENTAL UNCERTAINTIES  #################################

# # #### Luminosity

# ######################
# # Theory nuisance
nuisances['QCD_scale_VBS'] = {
    'name'  : 'QCDscale_VBS',
    'kind'  : 'weight',
    'type'  : 'shape',
    'samples'  :  { 'VBS': ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
}


nuisances['PU']  = {
                'name'  : 'CMS_PU_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict ( (skey, [ '(puWeightUp/puWeight)','(puWeightDown/puWeight)']) for skey in mc ),
                'AsLnN'      : '1',
}

for i in range(0,103):
    nuisances['pdf_weight_'+str(i)] = {
        'name'  : 'pdf_weight_'+str(i),
        'kind'  : 'weight',
        'OneSided': True,
        'type'  : 'shape',
        'samples' :  {'VBS': ['Alt$(LHEPdfWeight['+str(i)+'], 1.)']}
    }



for n in nuisances.values():
    n['skipCMS'] = 1

   
print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))


# nuisances = { k:v for k,v in nuisances.items() if k in ['fake_syst','fake_ele','fake_ele_stat','fake_mu','fake_mu_stat',
#                                                     'eff_e','eff_m','electronpt_0','muonpt_0','electronpt_1','muonpt_1' ] }