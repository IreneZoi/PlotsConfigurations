#!/bin/bash

years=(2016 2017 2018)
categories_boost=(boost_wjetcr_ele boost_wjetcr_mu  boost_topcr_ele boost_topcr_ele )
variables_boost=(events Mww deltaeta_vbs deltaphi_vbs fit_bins_boost Lepton_pt Lepton_eta mjj_vbs nJets_boost Centr_ww Zlep whad_pt_boost w_lep_pt )

categories_res=(res_wjetcr_ele res_wjetcr_mu res_topcr_ele res_topcr_mu)
variables_res=(events Mww deltaeta_vbs deltaphi_vbs fit_bins_res Lepton_pt Lepton_eta mjj_vbs nJets_res Centr_ww Zlep w_lep_pt )

fits=(prefit postfit)

fulloperator=cT0_eboliv2
Category=run2_all
SRVAR=DNN




for year in ${years[*]}; do
    echo " plotting ${year}"
    for fit in ${fits[*]}; do
        for CUT in ${categories_boost[*]}; do
            echo " category: ${CUT}"
            for PLOTVAR in ${variables_boost[*]}; do
                echo " PLOTVAR: ${PLOTVAR}"

                mv /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/${fit}/WV_${year}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/PlotVar${PLOTVAR}/log_cratio_${CUT}_${PLOTVAR}.png /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/${fit}/WV_${year}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/
                rm -rf /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/${fit}/WV_${year}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/PlotVar${PLOTVAR}/
            done
        done


        for CUT in ${categories_res[*]}; do
            echo " category: ${CUT}"
            for PLOTVAR in ${variables_res[*]}; do
                echo " PLOTVAR: ${PLOTVAR}"

                mv /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/${fit}/WV_${year}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/PlotVar${PLOTVAR}/log_cratio_${CUT}_${PLOTVAR}.png /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/${fit}/WV_${year}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/
                rm -rf /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/${fit}/WV_${year}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/PlotVar${PLOTVAR}/
            done
        done
    done
done