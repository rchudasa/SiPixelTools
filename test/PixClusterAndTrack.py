#
# Last update: new version for python
#
#
import FWCore.ParameterSet.Config as cms
process = cms.Process("cluTest")
                   
#process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
# process.load("Configuration.StandardSequences.Services_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
# to use no All 
# 2017
#process.GlobalTag.globaltag = '90X_dataRun2_Express_v4' # 
process.GlobalTag.globaltag = '92X_dataRun2_Express_v2' # 
#process.GlobalTag.globaltag = '92X_dataRun2_Express_v4' # 
# 2016
#process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v3' # for 266277
#process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v9' # >=8010
#process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v10' # >=8014
#process.GlobalTag.globaltag = '80X_dataRun2_Express_v10' # >8010
#process.GlobalTag.globaltag = '80X_dataRun2_Express_v12' # >8014
# AUTO conditions 
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_design', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2017', '')


import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
# accept if 'path_1' succeeds
process.hltfilter = hlt.hltHighLevel.clone(
# Min-Bias	
#    HLTPaths = ['HLT_Physics*'],
#    HLTPaths = ['HLT_Random*'],
    HLTPaths = ['HLT_ZeroBias*'],
#    HLTPaths = ['HLT_ZeroBias_part*'],  # empty
#    HLTPaths = ['HLT_ZeroBias_FirstCollisionInTrain_*'], # empty
#    HLTPaths = ['HLT_ZeroBias_LastCollisionInTrain_*'],  # empty
#    HLTPaths = ['HLT_ZeroBias_FirstBXAfterTrain_*'], # empty
#    HLTPaths = ['HLT_ZeroBias_IsolatedBunches_*'], # empty
#    HLTPaths = ['HLT_ZeroBias_FirstCollisionAfterAbortGap_*'],
#    HLTPaths = ['HLT_L1SingleMuOpen_v*'],
#    HLTPaths = ['HLT_PAZeroBias*'],
#    HLTPaths = ['HLT_PARandom*'],
#    HLTPaths = ['HLT_PAMinBias*'],
# Commissioning:
#    HLTPaths = ['HLT_L1Tech5_BPTX_PlusOnly_v*'],
#    HLTPaths = ['HLT_L1Tech6_BPTX_MinusOnly_v*'],
#    HLTPaths = ['HLT_L1Tech7_NoBPTX_v*'],
#
#    HLTPaths = ['p*'],
#    HLTPaths = ['path_?'],
    andOr = True,  # False = and, True=or
    throw = False
    )


process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('siPixelClusters'),
    destinations = cms.untracked.vstring('cout'),
#    destinations = cms.untracked.vstring("log","cout"),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
    )
#    log = cms.untracked.PSet(
#        threshold = cms.untracked.string('DEBUG')
#    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

myfilelist = cms.untracked.vstring()
myfilelist.extend([
])

process.source = cms.Source("PoolSource",
#fileNames =  myfilelist

  fileNames = cms.untracked.vstring(    

# mc
#"/store/relval/CMSSW_9_2_3/RelValNuGun/GEN-SIM-RECO/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/12995CE4-3851-E711-B4A6-0CC47A4D7602.root",
# "/store/relval/CMSSW_9_2_3/RelValNuGun/GEN-SIM-DIGI-RAW-HLTDEBUG/PUpmx25ns_92X_upgrade2017_realistic_v2_earlyBS2017-v1/10000/1ECCAF11-2E51-E711-AE03-0025905B8594.root",


"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/670/00000/A4AFA400-9E5C-E711-ABFB-02163E01A6AD.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/671/00000/1665877E-B15C-E711-8FC7-02163E0133E1.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/672/00000/0645B604-AA5C-E711-8231-02163E013778.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/673/00000/08A31073-A95C-E711-90CA-02163E01A45A.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/674/00000/00090DB9-B85C-E711-9A6A-02163E0134D8.root",

#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/664/00000/0268DAE5-6C5C-E711-BC2D-02163E019DE0.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/663/00000/1078B975-6C5C-E711-886A-02163E01237E.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/662/00000/1CEE72F3-675C-E711-AE3B-02163E019E36.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/656/00000/701D9DCD-535C-E711-A3AD-02163E019B52.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/661/00000/00FB7699-5E5C-E711-9877-02163E01450F.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/666/00000/0247FEAC-845C-E711-B03B-02163E011CE3.root",

# high Vibias  250
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/494/00000/221DC7DD-1E5A-E711-A76A-02163E011BB6.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/495/00000/003591BD-1A5A-E711-AF2A-02163E01A508.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/496/00000/04813659-1B5A-E711-9DE9-02163E0143BD.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/499/00000/0E628ABD-225A-E711-8B40-02163E01A5E2.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/501/00000/00CCEF78-235A-E711-8A06-02163E019C00.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/502/00000/04EA9099-215A-E711-AD16-02163E01427E.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/503/00000/0024EBBF-385A-E711-BF25-02163E019E77.root",

#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/424/00000/08244BBE-9758-E711-968E-02163E013479.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/426/00000/02E7F5BF-A158-E711-A567-02163E01412C.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/430/00000/00B72BF4-AF58-E711-A68D-02163E011A70.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/432/00000/00305E99-C358-E711-867B-02163E012A01.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/435/00000/004B3ABB-DC58-E711-82F3-02163E01A1D9.root",

# +11ns 200VforL1
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/281/00000/847D13F4-0657-E711-ACBE-02163E019BAA.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/287/00000/0E731E39-1457-E711-BC95-02163E01383A.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/288/00000/0803556C-1657-E711-8F2C-02163E019BD7.root",

# +12ns 
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/211/00000/028283A8-CF55-E711-A842-02163E0133E6.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/178/00000/00179E1E-7055-E711-811C-02163E01283D.root",
# +11ns 
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/215/00000/0C4DCA2A-D755-E711-BFB4-02163E01A5F0.root",
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/179/00000/00346B77-9655-E711-B4F3-02163E0123BE.root",
# +10ns 
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/180/00000/00038195-9D55-E711-96E2-02163E011F67.root",
# +9ns 
#"/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/181/00000/0054993F-A355-E711-B2D7-02163E01422D.root",


# high Vibias  100
# +18ns
#"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v3/000/297/019/00000/00D8147A-B752-E711-B5A8-02163E011D5B.root",
# +15ns
#"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v3/000/297/018/00000/1AEA423A-B652-E711-AEAD-02163E01180A.root",
# +10.5ns
#"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v3/000/297/017/00000/06A19196-B852-E711-884E-02163E0138C1.root",
# +12ns
#"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v3/000/297/016/00000/0255F076-B552-E711-9E49-02163E011FA9.root",
# +7.5ns
#"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v3/000/297/012/00000/02E7996A-B852-E711-B96F-02163E0143F0.root",
# nominal
#"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v3/000/297/003/00000/029D5DDE-A252-E711-9166-02163E0146E9.root",

# time 
#"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/902/00000/008557CF-BE51-E711-A29A-02163E01A4E0.root",
#"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/901/00000/009184D1-BF51-E711-A86D-02163E0143CF.root",
#"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/900/00000/2C83793D-BE51-E711-9E1F-02163E0138BA.root",
#"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/899/00000/185FC0AB-BE51-E711-9C71-02163E012019.root",
###"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/898/00000/44CD306E-BA51-E711-977A-02163E01351C.root",
#"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/888/00000/D8232BCF-AB51-E711-8B13-02163E013978.root",

# ctrl reg sca 
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/795/00000/1A1C0A23-0851-E711-8692-02163E01472F.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/790/00000/02DC1127-0951-E711-851C-02163E0143F0.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/789/00000/06177BD3-0451-E711-ABDF-02163E0133C1.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/788/00000/A0F7FF84-0351-E711-8FEE-02163E013662.root",

# vibias_bus scan
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/879/00000/046EAD9E-6151-E711-B783-02163E012B0C.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/876/00000/00A4AF1A-5C51-E711-83A7-02163E0146E8.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/875/00000/0895EF79-5A51-E711-99A0-02163E0142F0.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/874/00000/1475EB30-5751-E711-8988-02163E014472.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/873/00000/0638B0A2-5751-E711-BB45-02163E012477.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/872/00000/0E4D488C-5951-E711-8FD1-02163E0120C8.root",

# threshold scan 
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/878/00000/026F3312-5F51-E711-81E7-02163E011C6D.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/877/00000/04ED8753-5D51-E711-8C13-02163E011BE7.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/871/00000/0A593904-5751-E711-AB41-02163E011B0E.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/870/00000/065E00C2-5851-E711-8C67-02163E01356F.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/869/00000/263C3C92-5351-E711-9FE6-02163E0142F9.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/868/00000/0607D84F-4F51-E711-9E94-02163E01338F.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/867/00000/02BC1FDC-4C51-E711-BE3E-02163E0128EB.root",

#
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/702/00000/FED4EA05-D64F-E711-82F9-02163E012A6B.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/664/00000/00F38C8D-A54F-E711-A312-02163E01472F.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v2/000/296/643/00000/08070285-5E4F-E711-BB56-02163E01476C.root",

# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/296/116/00000/00187318-DE49-E711-883F-02163E019DD2.root",

# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/296/108/00000/22174A51-CB49-E711-8375-02163E01384C.root",

# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/296/075/00000/045D378C-9949-E711-A42A-02163E011F09.root",

# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/640/00000/029DD0A3-8645-E711-AE8C-02163E013978.root",

 #"/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/636/00000/003BFB77-6E45-E711-AECD-02163E013407.root",


# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/436/00000/F60EF27A-FC43-E711-86F2-02163E019E38.root",

# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/439/00000/426B4782-FC43-E711-9328-02163E011A76.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/439/00000/F853E939-FF43-E711-A59D-02163E013479.root",

# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/454/00000/0E5832FA-1744-E711-A404-02163E01A6AA.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/458/00000/0A262760-1644-E711-926B-02163E01A1E0.root",

# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/381/00000/00034176-5043-E711-AA6F-02163E019C98.root",

# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/380/00000/18B13C10-4543-E711-9D8F-02163E0125F8.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/379/00000/047A3D4D-4343-E711-A34B-02163E0128BB.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/378/00000/1C460005-4443-E711-968C-02163E013976.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/377/00000/0642F3F7-4043-E711-B633-02163E01A3C7.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/366/00000/02380CCF-1843-E711-9242-02163E01A4FF.root",

# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/318/00000/06085100-B142-E711-A1D0-02163E01A1FA.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/209/00000/005E61C9-D341-E711-BEAE-02163E019C9F.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/295/128/00000/2E861F6A-1F41-E711-BEEC-02163E01A32B.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/294/929/00000/000E8FD5-1D40-E711-80C9-02163E01467E.root",
# "/store/express/Run2017A/ExpressPhysics/FEVT/Express-v1/000/294/927/00000/FE44FBE2-CE3F-E711-B011-02163E019BD5.root",

#"/store/express/Commissioning2017/ExpressCosmics/FEVT/Express-v1/000/294/307/00000/FADCA9A2-623B-E711-B713-02163E019CA0.root",

# 272022
#"/store/data/Run2016B/ZeroBias1/RECO/PromptReco-v1/000/272/022/00000/0014666A-D80F-E611-83FA-02163E011999.root",
#"/store/data/Run2016B/AlCaLumiPixels/ALCARECO/LumiPixels-PromptReco-v1/000/272/022/00000/1C85457B-D30F-E611-8EE6-02163E014695.root",

# 272783
#"root://eoscms//eos/cms/tier0/store/data/Run2016B/ZeroBias/RECO/PromptReco-v1/000/272/783/00000/1C4AD70E-7916-E611-9B0D-02163E0140FF.root",
#"root://eoscms//eos/cms/tier0/store/data/Run2016B/ZeroBias1/RECO/PromptReco-v1/000/272/783/00000/02BD007E-6E16-E611-994B-02163E01468A.root",
# 278193
#"root://eoscms//eos/cms/tier0/store/express/Run2016F/ExpressPhysics/FEVT/Express-v1/000/278/193/00000/04476347-4F5A-E611-AF5B-FA163EB8F285.root",
#"/store/data/Run2016F/ZeroBias/ALCARECO/TkAlMinBias-PromptReco-v1/000/278/509/00000/18648660-5460-E611-9CDB-FA163ED6B29A.root",

  )   # end the list "by-hand"

)

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('124230:26-124230:9999','124030:2-124030:9999')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('297211:26-297211:83')


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('clus_ana.root')
)

process.d = cms.EDAnalyzer("PixClusterAna",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    #src = cms.InputTag("siPixelClustersForLumi"),   # from the lumi stream
    src = cms.InputTag("siPixelClusters"),
    #src = cms.InputTag("siPixelClustersPreSplitting"),
    #src = cms.InputTag("ALCARECOTkAlMinBias"), # ALCARECO
    # additional selections, e.g. select bx=1 -> (2,1)
    Select1 = cms.untracked.int32(0),  # select the cut type, 0 no cut
    Select2 = cms.untracked.int32(0),  # select the cut value   
)

process.d2 = cms.EDAnalyzer("PixClusterAna",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    #src = cms.InputTag("siPixelClustersForLumi"),   # from the lumi stream
    src = cms.InputTag("siPixelClusters"),
    #src = cms.InputTag("siPixelClustersPreSplitting"),
    #src = cms.InputTag("ALCARECOTkAlMinBias"), # ALCARECO
    # additional selections, e.g. select bx=1 -> (2,1)
    Select1 = cms.untracked.int32(2),  # select the cut type, 0 no cut
    Select2 = cms.untracked.int32(1),  # select the cut value   
)

process.clutest = cms.EDAnalyzer("PixClusterTest",
    Verbosity = cms.untracked.bool(True),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("siPixelClusters"),
#    src = cms.InputTag("siPixelClustersPreSplitting"),
)

process.c = cms.EDAnalyzer("PixClustersWithTracks",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("generalTracks"),
# for cosmics 
#    src = cms.InputTag("ctfWithMaterialTracksP5"),
#     PrimaryVertexLabel = cms.untracked.InputTag("offlinePrimaryVertices"),
#     trajectoryInput = cms.string("TrackRefitterP5")
#     trajectoryInput = cms.string('cosmictrackfinderP5')
# additional selections
    Select1 = cms.untracked.int32(0),  # select the cut type, o no cut
    Select2 = cms.untracked.int32(0),  # select the cut value   
)
process.c1 = cms.EDAnalyzer("PixClustersWithTracks",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("generalTracks"),
# for cosmics 
#    src = cms.InputTag("ctfWithMaterialTracksP5"),
#     PrimaryVertexLabel = cms.untracked.InputTag("offlinePrimaryVertices"),
#     trajectoryInput = cms.string("TrackRefitterP5")
#     trajectoryInput = cms.string('cosmictrackfinderP5')
# additional selections
    Select1 = cms.untracked.int32(13),  # select the cut type, o no cut
    Select2 = cms.untracked.int32(1),  # select the cut value   
)
process.c2 = cms.EDAnalyzer("PixClustersWithTracks",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("generalTracks"),
# for cosmics 
#    src = cms.InputTag("ctfWithMaterialTracksP5"),
#     PrimaryVertexLabel = cms.untracked.InputTag("offlinePrimaryVertices"),
#     trajectoryInput = cms.string("TrackRefitterP5")
#     trajectoryInput = cms.string('cosmictrackfinderP5')
# additional selections
    Select1 = cms.untracked.int32(14),  # select the cut type, o no cut
    Select2 = cms.untracked.int32(1),  # select the cut value   
)


#process.p = cms.Path(process.hltfilter*process.c2)
#process.p = cms.Path(process.hltfilter*process.d)
process.p = cms.Path(process.hltfilter*process.d*process.c*process.c1*process.c2)
#process.p = cms.Path(process.d*process.b*process.c)  # for mc 
#process.p = cms.Path(process.d) # for cosmics


