# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# proj_calc_emp.py
# Created on: 2014-04-28 00:42:07.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
import sys

try: 
		# Local variables:
		urban_tracts = "0urban_area_tracts"
		wac = "C:\\Users\\Matthew\\Desktop\\ECON\\Research\\Urban\\Papers\\City Center Resurgence\\GIS\\Working Files\\wac_trct.xlsx\\wac$"
		urban_area_tracts = "0urban_area_tracts"
		v0urban_area_tracts__2_ = "0urban_area_tracts"

		print "Define Projection"
		# Process: Define Projection
		arcpy.DefineProjection_management(v0urban_area_tracts, "PROJCS['NAD_1983_UTM_Zone_18N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-75.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]")
		
		print "Add and Compute Area"
		# Process: Add Field
		arcpy.AddField_management(v0urban_area_tracts__2_, "Area", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

		arcpy.CalculateField_management(v0urban_area_tracts__2_, Area,  "!shape.area", "PYTHON_9.3")

		print "Join to LEHD"
		# Process: Add Join
		arcpy.AddJoin_management(v0urban_area_tracts__4_, "GEOID", wac_, "trct", "KEEP_ALL")
		
except:
		print arcpy.GetMessages()