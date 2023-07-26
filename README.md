# SiPixelTools
This repository is cloned from the CMSTrackerDPG group. https://github.com/CMSTrackerDPG/SiPixelTools-HitAnalyzer
It is based on branch CMSSW_9_3_0_pre1 with some modifications to remove the bugs while compilation. 

cmsrel CMSSW_10_6_20
git clone https://github.com/rchudasa/SiPixelTools-HitAnalyzer.git SiPixelTools/HitAnalyzer
scram b -j8
cd SiPixelTools/HitAnalyzer/test

#### Produce the TTbar MC using 
cmsRun PhaseI_TTbar_13TeV_NoPu_RECO_cfg.py

#### Produce the PixelHit Ntuples
cmsRun readRecHits.py

