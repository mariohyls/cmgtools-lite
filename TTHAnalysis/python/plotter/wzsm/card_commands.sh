#These have the back norm uncertainties (so no for the multifit to SR + CR)
python makeShapeCardsSusy.py ./wzsm/mca_includes.txt ./wzsm/cuts_wzsm.txt '(abs(LepSel1_pdgId)==13)+(abs(LepSel2_pdgId)==13)+(abs(LepSel3_pdgId)==13)' '4,-0.5,3.5' ./wzsm/systs_wz.txt -P /pool/cienciasrw/userstorage/carlosec/wzSkimmed/ --Fs {P}/leptonJetReCleanerWZSM --Fs {P}/leptonBuilderWZSM --FMCs {P}/bTagEventWeightFullSimWZ30 -j 64 -l 35.9 --s2v --s2v --tree treeProducerSusyMultilepton --mcc wzsm/mcc_varsub_wzsm.txt --mcc wzsm/mcc_triggerdefs.txt -f -W ' puw_nInt_Moriond(nTrueInt)*getLepSF(LepSel1_conePt,LepSel1_eta,LepSel1_pdgId,1,1)*getLepSF(LepSel2_conePt,LepSel2_eta,LepSel2_pdgId,1,1)*getLepSF(LepSel3_conePt,LepSel3_eta,LepSel3_pdgId,1,1)*bTagWeight' -p data -p prompt_.* -p convs.* -p rares.* -p fakes_appldata.* --plotgroup fakes_appldata+=promptsub --load-macro wzsm/functionsPUW.cc --load-macro wzsm/functionsSF.cc --load-macro wzsm/functionsWZ.cc --od /nfs/fanae/user/carlosec/Combine/CMSSW_8_1_0/src/datacards/ -o WZ_Feb14 -E SR --neglist promptsub --autoMCStats

python makeShapeCardsSusy.py ./wzsm/mca_includes.txt ./wzsm/cuts_wzsm.txt '(abs(LepSel1_pdgId)==13)+(abs(LepSel2_pdgId)==13)+(abs(LepSel3_pdgId)==13)' '4,-0.5,3.5' ./wzsm/systs_wz.txt -P /pool/cienciasrw/userstorage/carlosec/wzSkimmed/ --Fs {P}/leptonJetReCleanerWZSM --Fs {P}/leptonBuilderWZSM --FMCs {P}/bTagEventWeightFullSimWZ30 -j 8 -l 35.9 --s2v --tree treeProducerSusyMultilepton --mcc wzsm/mcc_varsub_wzsm.txt --mcc wzsm/mcc_triggerdefs.txt -f -W 'puw_nInt_Moriond(nTrueInt)*getLepSF(LepSel1_conePt,LepSel1_eta,LepSel1_pdgId,1,1)*getLepSF(LepSel2_conePt,LepSel2_eta,LepSel2_pdgId,1,1)*getLepSF(LepSel3_conePt,LepSel3_eta,LepSel3_pdgId,1,1)*bTagWeight' -p data -p prompt_.* -p convs.* -p rares.* -p fakes_appldata.* --plotgroup fakes_appldata+=promptsub --load-macro wzsm/functionsPUW.cc --load-macro wzsm/functionsSF.cc --load-macro wzsm/functionsWZ.cc --od /nfs/fanae/user/carlosec/Combine/CMSSW_8_1_0/src/datacards/chargeSplit -o WZ_Minus -E SR --neglist promptsub --autoMCStats -E pmm

#These doesn't have the back norm uncertainties (so for the multifit to SR + CR)
python makeShapeCardsSusy.py ./wzsm/mca_includes.txt ./wzsm/cuts_wzsm.txt '(abs(LepSel1_pdgId)==13)+(abs(LepSel2_pdgId)==13)+(abs(LepSel3_pdgId)==13)' '4,-0.4,3.5' ./wzsm/systs_wz_unNorm.txt -P /pool/cienciasrw/userstorage/carlosec/wzSkimmed/ --Fs {P}/leptonJetReCleanerWZSM --Fs {P}/leptonBuilderWZSM --FMCs {P}/bTagEventWeightFullSimWZ30 -j 64 -l 35.9 --s2v --s2v --tree treeProducerSusyMultilepton --mcc wzsm/mcc_varsub_wzsm.txt --mcc wzsm/mcc_triggerdefs.txt -f -W ' puw_nInt_Moriond(nTrueInt)*getLepSF(LepSel1_conePt,LepSel1_eta,LepSel1_pdgId,1,1)*getLepSF(LepSel2_conePt,LepSel2_eta,LepSel2_pdgId,1,1)*getLepSF(LepSel3_conePt,LepSel3_eta,LepSel3_pdgId,1,1)*bTagWeight ' -p data -p prompt_.* -p convs.* -p rares.* -p incl_fakes_appldata* --plotgroup incl_fakes_appldata+=incl_promptsub --load-macro wzsm/functionsPUW.cc --load-macro wzsm/functionsSF.cc --load-macro wzsm/functionsWZ.cc --od /nfs/fanae/user/vischia/workarea/cmssw/combine/CMSSW_8_1_0/src/wz/incl/ -o WZSR -E SR  --neglist promptsub --extraText 'rttX   rateParam * rares_ttX      1' --extraText 'rZZ    rateParam * prompt_ZZH     1' --extraText 'rconvs rateParam * convs          1' --autoMCStats

