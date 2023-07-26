#
import FWCore.ParameterSet.Config as cms

process = cms.Process("simTest")

#process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load('Configuration.Geometry.GeometryExtended2017Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2017_cff')

#process.load("Configuration.StandardSequences.MagneticField_38T_cff")


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('PixSimHitsTest'),
    destinations = cms.untracked.vstring('cout'),
#    destinations = cms.untracked.vstring("log","cout"),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
    )
#    log = cms.untracked.PSet(
#        threshold = cms.untracked.string('DEBUG')
#    )
)

process.source = cms.Source("PoolSource",
    fileNames =  cms.untracked.vstring(
    'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu_phase1/pt100_76/simhits/simHits1.root'
#    '/store/user/kotlinski/mu100/simhits/simHits.root',
#    'file:simHits_100eve.root'
#    'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu/pt100_72/simhits/simHits1.root'
#    'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu/pt100_71_pre5/simhits/simHits3.root'
#    'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu/pt100_71_pre5/simhits/simHits4.root'
#    'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu/pt100_71_pre5/simhits/simHits5.root'
#    'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu/pt100_71_pre5/simhits/simHits6.root'
#    'file:/afs/cern.ch/work/d/dkotlins/public//MC/mb/13tev/simhits/simHits1.root'
#    'file:/afs/cern.ch/work/d/dkotlins/public//MC/mb/8tev/simhits/simHits1.root'
    )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('sim_histos.root')
)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#from Configuration.AlCa.GlobalTag import GlobalTag
# to use no All 

#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_design', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2017', '')


# use the test from SiTracker
#process.analysis =  cms.EDAnalyzer("PixelSimHitsTest",
# or from DPGAnalysis 
process.analysis =  cms.EDAnalyzer("PixSimHitsTest",
	src = cms.string("g4SimHits"),
        mode = cms.untracked.string("bpix"),
	list = cms.string("TrackerHitsPixelBarrelLowTof"),
#	list = cms.string("TrackerHitsPixelBarrelHighTof"),
#        mode = cms.untracked.string("fpix"),
#	list = cms.string("TrackerHitsPixelEndcapLowTof"),
#	list = cms.string("TrackerHitsPixelEndcapHighTof"),
        Verbosity = cms.untracked.bool(True),
        phase1 = cms.untracked.bool(True),
)

process.p = cms.Path(process.analysis)

