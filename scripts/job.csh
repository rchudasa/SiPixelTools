#!/bin/tcsh
echo $home

source /afs/cern.ch/cms/LCG/LCG-2/UI/cms_ui_env.csh

#rfdir /castor/cern.ch/cms/store/data

setenv SCRAM_ARCH slc6_amd64_gcc493
cd /afs/cern.ch/user/d/dkotlins/public/CMSSW/CMSSW_8_0_12/src

#source /afs/cern.ch/cms/sw/cmsset_default.csh
source /afs/cern.ch/project/gd/apps/cms/cmsset_default.csh   # this works with gcc462

# must be run frm the release area
eval `scram runtime -csh`

cd DPGAnalysis-SiPixelTools/HitAnalyzer/scripts
pwd

#  RAW
#cmsRun testGainPayload.py 
#cmsRun runRawDumper.py 
#cmsRun runRawDumper_lumi.py 
#cmsRun runRawToDigi_cfg.py 
cmsRun runRawToTracksPlusTriplets.py 
# cmsRun runFedErrorDumper.py

#cmsRun testPxdigi.py

#cmsRun PixClusterAna.py
#cmsRun PixClusterTest.py
#cmsRun PixClusterAna_260627.py

#cmsRun PixClusterAna_Phys_254227.py
#cmsRun PixClusterAna_Comm_248025.py

#cmsRun PixClusterAna_Lumi.py

#cmsRun testTracks.py
#cmsRun SimsToClus.py

# ls /tmp/dkotlins

 




