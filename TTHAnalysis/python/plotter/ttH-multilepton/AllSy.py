# luminosity
lumi_13TeV_2016		: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .* : 1.026

# lepton efficiencies
CMS_ttHl_lepEff_muloose : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*2lss_mm.* : 1.04
CMS_ttHl_lepEff_muloose : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*2lss_em.* : 1.02
CMS_ttHl_lepEff_muloose : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*3l.* : 1.03
CMS_ttHl_lepEff_muloose : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*4l.* : 1.04

CMS_ttHl_lepEff_elloose : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .* : elLooseUnc : templates

CMS_ttHl_lepEff_mutight : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*2lss_mm.* : 1.06
CMS_ttHl_lepEff_mutight : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*2lss_em.* : 1.03
CMS_ttHl_lepEff_mutight : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*3l.* : 1.04
CMS_ttHl_lepEff_mutight : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*4l.* : 1.06

CMS_ttHl_lepEff_eltight : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*2lss_ee.* : 1.06
CMS_ttHl_lepEff_eltight : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*2lss_em.* : 1.03
CMS_ttHl_lepEff_eltight : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*3l.* : 1.04
CMS_ttHl_lepEff_eltight : ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*4l.* : 1.06

### todo: replace with tau veto efficiency, not using this yet
#CMS_ttHl_tauID		: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*2lss_1tau.* : 1.1

# trigger efficiencies
CMS_ttHl16_trigger_ee	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*2lss_ee.* : 1.02
CMS_ttHl16_trigger_em	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*2lss_em.* : 1.01
CMS_ttHl16_trigger_mm	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*2lss_mm.* : 1.01
CMS_ttHl16_trigger_3l	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*3l.* : 1.03
CMS_ttHl16_trigger_3l	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .*4l.* : 1.03

# JES
CMS_ttHl_JES		: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .* : jec : templates

#### btag
CMS_ttHl_btag_LF	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .* : bTag_LF		: templates
CMS_ttHl_btag_HF	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .* : bTag_HF 		: templates
CMS_ttHl16_btag_HFStats1	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .* : bTag_HFStats1 	: templates
CMS_ttHl16_btag_HFStats2	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .* : bTag_HFStats2 	: templates	
CMS_ttHl16_btag_LFStats1	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .* : bTag_LFStats1 	: templates
CMS_ttHl16_btag_LFStats2	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .* : bTag_LFStats2 	: templates
CMS_ttHl_btag_cErr1	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .* : bTag_cErr1 	: templates
CMS_ttHl_btag_cErr2	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW : .* : bTag_cErr2 	: templates

# statistical fluctuations of all templates
CMS_ttHl16_templstat 	: ttH.*|TT[WZ]|WZ|Rares|Gstar|WWss|Convs|Flips|TT|DY|WJets|SingleTop|WW|data_fakes|data_flips : .* : 1.0 : stat_foreach_shape_bins : .*

# Diboson background
CMS_ttHl_WZ_stat : WZ : .*3l.* : 1.1
CMS_ttHl_WZ_bkgs : WZ : .*3l.* : 1.2
CMS_ttHl_WZ_btag : WZ : .*3l_bl.* : 1.1
CMS_ttHl_WZ_btag : WZ : .*3l_bt.* : 1.4
CMS_ttHl_WZ_theo : WZ : .*3l.* : 1.07
CMS_ttHl_WZ_4j : WZ : .*2lss.* : 2.0 

# Other normalizations
CMS_ttHl_Rares		: Rares|Gstar|WWss : .* : 1.5
CMS_ttHl_Convs		: Convs : .* : 1.3


# common theoretical uncertainties (fully correlated everywhere)
# note: pdf_gg is entered as 1/kappa since it has to be anti-correlated with Hgg
QCDscale_ttH   : ttH.* : .* : 0.915/1.058
QCDscale_ttW   : TTW   : .* : 1.12
QCDscale_ttZ   : TTZ   : .* : 1.11
pdf_Higgs_ttH  : ttH.* : .* : 1.036
pdf_gg         : TTZ   : .* : 0.966
pdf_qqbar      : TTW   : .* : 1.04

# shape theoretical uncertainties (private to this channel)
#CMS_ttHl_thu_shape_ttH_x  : ttH.* : .*2lss.*|.*3l.* : 1.0 : shapeOnly2D_1.03X_1Y
#CMS_ttHl_thu_shape_ttH_y  : ttH.* : .*2lss.*|.*3l.* : 1.0 : shapeOnly2D_1X_1.02Y
#CMS_ttHl_thu_shape_ttW_x  : TTW : .*2lss.*|.*3l.* : 1.0 : shapeOnly2D_1.04X_1Y
#CMS_ttHl_thu_shape_ttW_y  : TTW : .*2lss.*|.*3l.* : 1.0 : shapeOnly2D_1X_1.01Y
#CMS_ttHl_thu_shape_ttZ_x  : TTZ : .*2lss.*|.*3l.* : 1.0 : shapeOnly2D_1.02X_1Y
#CMS_ttHl_thu_shape_ttZ_y  : TTZ : .*2lss.*|.*3l.* : 1.0 : shapeOnly2D_1X_1.02Y


#####CMS_ttHl_pdf_shape_ttH_x  : ttH.* : .*2lss.*|.*3l.* : 1.0 : shapeOnly2D_X_1Y
#####CMS_ttHl_pdf_shape_ttH_y  : ttH.* : .*2lss.*|.*3l.* : 1.0 : shapeOnly2D_1X_Y
#####CMS_ttHl_pdf_shape_ttW_x  : TTW : .*2lss.*|.*3l.* : 1.0 : shapeOnly2D_X_1Y
#####CMS_ttHl_pdf_shape_ttW_y  : TTW : .*2lss.*|.*3l.* : 1.0 : shapeOnly2D_1X_Y
#####CMS_ttHl_pdf_shape_ttZ_x  : TTZ : .*2lss.*|.*3l.* : 1.0 : shapeOnly2D_X_1Y
#####CMS_ttHl_pdf_shape_ttZ_y  : TTZ : .*2lss.*|.*3l.* : 1.0 : shapeOnly2D_1X_Y

