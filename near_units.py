# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# near_units.py
# Created on: 2016-03-07 09:49:55.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
# import arcinfo


# Import arcpy module
import arcpy


# Local variables:
ua_lehd_acs_0 = "ua_lehd_acs_0"
ua_lehd_acs_0__2_ = ua_lehd_acs_0
places_line_99 = "places_line_99"

# Process: Near
arcpy.Near_analysis(ua_lehd_acs_0, "places_line_99", "", "NO_LOCATION", "NO_ANGLE", "PLANAR")

