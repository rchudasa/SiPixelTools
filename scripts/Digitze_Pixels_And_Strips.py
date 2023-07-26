##############################################################################

import FWCore.ParameterSet.Config as cms

process = cms.Process("Test")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
# process.load("Configuration.StandardSequences.Geometry_cff")
#process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

# process.load("SimTracker.Configuration.SimTracker_cff")
process.load("SimG4Core.Configuration.SimG4Core_cff")

# for strips 
process.load("CalibTracker.SiStripESProducers.SiStripGainSimESProducer_cfi")

# Choose the global tag here:
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
# for v7.0
#process.GlobalTag.globaltag = 'MC_70_V1::All'
#process.GlobalTag.globaltag = 'START70_V1::All'
#process.GlobalTag.globaltag = 'DESIGN70_V1::All'

#process.GlobalTag.globaltag = 'POSTLS171_V1::All'
#process.GlobalTag.globaltag = "PRE_MC_71_V2::All"
#process.GlobalTag.globaltag = "PRE_STA71_V4::All"

#process.GlobalTag.globaltag = "START71_V7::All"
#process.GlobalTag.globaltag = 'MC_71_V7::All'

#from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#from Configuration.AlCa.GlobalTag import GlobalTag
# to use no All 

# tags for 72X
#process.GlobalTag.globaltag = "MC_72_V1::All"
#process.GlobalTag.globaltag = "MC_72_V1"

# tags for 73X
#process.GlobalTag.globaltag = "MCRUN2_73_V11"
#process.GlobalTag.globaltag = "DESRUN1_73_V5"
#process.GlobalTag.globaltag = "MCRUN1_73_V5::All" # OK for condDB
#process.GlobalTag.globaltag = "MCRUN1_73_V5" # needs condDBv2

from Configuration.AlCa.autoCond_condDBv2 import autoCond
#process.GlobalTag.globaltag = autoCond['run2_design']
process.GlobalTag.globaltag = autoCond['run2_mc']


# process.load("SimGeneral.MixingModule.mixNoPU_cfi")

from SimGeneral.MixingModule.aliases_cfi import * 
from SimGeneral.MixingModule.mixObjects_cfi import *
# from SimGeneral.MixingModule.digitizers_cfi import *
from SimGeneral.MixingModule.pixelDigitizer_cfi import *
from SimGeneral.MixingModule.stripDigitizer_cfi import *
from SimGeneral.MixingModule.trackingTruthProducer_cfi import *


process.simSiPixelDigis = cms.EDProducer("MixingModule",
#    digitizers = cms.PSet(theDigitizers),
#    digitizers = cms.PSet(
#      mergedtruth = cms.PSet(
#            trackingParticles
#      )
#    ),

  digitizers = cms.PSet(
   pixel = cms.PSet(
    pixelDigitizer
   ),
  strip = cms.PSet(
    stripDigitizer
  ),
  ),

#theDigitizersValid = cms.PSet(
#  pixel = cms.PSet(
#    pixelDigitizer
#  ),
#  strip = cms.PSet(
#    stripDigitizer
#  ),
#  ecal = cms.PSet(
#    ecalDigitizer
#  ),
#  hcal = cms.PSet(
#    hcalDigitizer
#  ),
#  castor = cms.PSet(
#    castorDigitizer
#  ),
#  mergedtruth = cms.PSet(
#    trackingParticles
#  )
#),


    LabelPlayback = cms.string(' '),
    maxBunch = cms.int32(3),
    minBunch = cms.int32(-5), ## in terms of 25 ns

    bunchspace = cms.int32(25),
    mixProdStep1 = cms.bool(False),
    mixProdStep2 = cms.bool(False),

    playback = cms.untracked.bool(False),
    useCurrentProcessOnly = cms.bool(False),
    mixObjects = cms.PSet(
        mixTracks = cms.PSet(
            mixSimTracks
        ),
        mixVertices = cms.PSet(
            mixSimVertices
        ),
        mixSH = cms.PSet(
#            mixPixSimHits
# mixPixSimHits = cms.PSet(
    input = cms.VInputTag(cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), 
                          cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"),
                          cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), 
                          cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), 
                          cms.InputTag("g4SimHits","TrackerHitsTECHighTof"), 
                          cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), 
                          cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"),
                          cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
                          cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), 
                          cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), 
                          cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
                          cms.InputTag("g4SimHits","TrackerHitsTOBLowTof")
    ),
    type = cms.string('PSimHit'),
    subdets = cms.vstring(
        'TrackerHitsPixelBarrelHighTof',
        'TrackerHitsPixelBarrelLowTof',
        'TrackerHitsPixelEndcapHighTof',
        'TrackerHitsPixelEndcapLowTof',
        'TrackerHitsTECHighTof',
        'TrackerHitsTECLowTof',
        'TrackerHitsTIBHighTof',
        'TrackerHitsTIBLowTof',
        'TrackerHitsTIDHighTof',
        'TrackerHitsTIDLowTof',
        'TrackerHitsTOBHighTof',
        'TrackerHitsTOBLowTof'
    ),
    crossingFrames = cms.untracked.vstring(),
#        'MuonCSCHits',
#        'MuonDTHits',
#        'MuonRPCHits'),
#)   
        ),
        mixHepMC = cms.PSet(
            mixHepMCProducts
        )
    )
)

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
#     simMuonCSCDigis = cms.PSet(
#        initialSeed = cms.untracked.uint32(1234567),
#        engineName = cms.untracked.string('TRandom3')
#    ),
     simSiPixelDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('TRandom3')
   )
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(
       'file:simHits1.root'
#       'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu/pt100_72/simhits/simHits1.root'
#       'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu/pt100_71_pre5/simhits/simHits2.root'
#       'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu/pt100_71_pre5/simhits/simHits1.root'
#       'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu/pt100_71_pre5/simhits/simHits3.root'
#       'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu/pt100_71_pre5/simhits/simHits4.root'
  )
)


process.o1 = cms.OutputModule("PoolOutputModule",
      outputCommands = cms.untracked.vstring('drop *','keep *_*_*_Test'),
#      fileName = cms.untracked.string('file:/afs/cern.ch/work/d/dkotlins/public/MC/mu/pt100_71_pre7/digis_trk/digis4_presta71.root')
      fileName = cms.untracked.string('file:digis.root')
)

process.g4SimHits.Generator.HepMCProductLabel = 'source'

# modify digitizer parameters
# pixel threshold
#process.simSiPixelDigis.digitizers.pixel.ThresholdInElectrons_BPix = 3500.0 
# use inefficiency from DB Gain calibration payload?
process.simSiPixelDigis.digitizers.pixel.useDB = cms.bool(False) 
# use LA from file 
process.simSiPixelDigis.digitizers.pixel.LorentzAngle_DB = cms.bool(False)
process.simSiPixelDigis.digitizers.pixel.TanLorentzAnglePerTesla_BPix = 0.1 
#process.simSiPixelDigis.digitizers.pixel.TanLorentzAnglePerTesla_BPix = 0.106 
#process.simSiPixelDigis.digitizers.pixel.TanLorentzAnglePerTesla=FPix = 0.106 
process.simSiPixelDigis.digitizers.pixel.AddPixelInefficiencyFromPython = cms.bool(False)

#This process is to run the digitizer:
process.p1 = cms.Path(process.simSiPixelDigis)

process.outpath = cms.EndPath(process.o1)


