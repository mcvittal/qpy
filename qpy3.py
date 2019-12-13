#!/usr/bin/env python3

## The new home for qpy - qpy3. The old qpy is slated for removal and will be replaced with this
## class.

## Written 12/12/2019 by @mcvittal

from modules.Analysis import Analysis
from modules.License import LicenseManager
from xvfbwrapper import Xvfb
import sys
from qgis.core import QgsApplication, QgsVectorLayer


gui_flag = False

# For headless servers - fake x server so dummy QGIS instance can run 
vdisplay = Xvfb()
vdisplay.start()

#Create dummy instance 
app = QgsApplication([], gui_flag)

# Instantiate the dummy instance 
QgsApplication.setPrefixPath("/usr", True)
QgsApplication.initQgis()

# Add the processing plugin to the python path 
sys.path.append('/usr/share/qgis/python/plugins')

# Load processing package
from processing.core.Processing import Processing
import processing
Processing.initialize()

class Qpy(Analysis, LicenseManager):
    pass

Qpy = Qpy(processing, Processing)


# Helpful general functions go here 
def list_all_algorithms():
    for alg in QgsApplication.processingRegistry().algorithms():
        print("{}:{} --> {}".format(alg.provider().name(), alg.name(), alg.displayName()))
