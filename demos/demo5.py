#!/usr/bin/env python3

import sys 

sys.path.append("..")

from qpy3 import Qpy 

Qpy.compute_edge_raster("demodata/gt30w020n90.tif", "demodata/shoreline.shp", -9999)