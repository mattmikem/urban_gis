# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# max_cluster_ext.py
# Created on: 2014-05-09 01:15:45.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
from arcpy import env
import sys
import shapefile
import shpUtils

#Overwriting allowed
arcpy.env.overwriteOutput = True

#Working Directory
arcpy.env.workspace = "C:\\Users\\Matthew\\Desktop\\ECON\\Research\\Urban\\Papers\\City Center Resurgence\\GIS\\Working Files\\Output\\"
arcpy.env.qualifiedFieldNames = False


# Local variables:

uat_hspt_hi = "uat_hspt_hi"
uat_hspt_lyr = "uat_hspt_lyr"
uat_split_lyr = "uat_split_lyr"
uat_cen_cluster = "uat_cen_cluster"

c = 2

uat_emp_hspt = "uat_emp_hspt_"+str(c)+".shp"
uat_emp_hspt_1__2_ = "uat_emp_hspt_1"
uat_emp_hspt_1_selection = "uat_emp_hspt_1 selection"
uat_emp_hspt_split__2_ = "uat_emp_hspt_split"
uat_emp_hspt_dis = "C:\\Users\\Matthew\\Desktop\\ECON\\Research\\Urban\\Papers\\City Center Resurgence\\GIS\\Working Files\\Output\\uat_emp_hspt_dis.shp"
uat_emp_hspt_split = "C:\\Users\\Matthew\\Desktop\\ECON\\Research\\Urban\\Papers\\City Center Resurgence\\GIS\\Working Files\\Output\\uat_emp_hspt_split.shp"
uat_hspt_max = "C:\\Users\\Matthew\\Desktop\\ECON\\Research\\Urban\\Papers\\City Center Resurgence\\GIS\\Working Files\\Output\\uat_hspt_max.dbf"
uat_emp_hspt_1_Layer = "uat_emp_hspt_1_Layer"
uat_emp_hspt_0_Layer__2_ = "uat_emp_hspt_1_Layer"

# Process: Select Layer by Attribute

# Make a layer from the feature class
#arcpy.MakeFeatureLayer_management(uat_emp_hspt, uat_hspt_lyr) 

print "High Density Select"

name_select = "\"GiZScore\" > 2.58"
arcpy.MakeFeatureLayer_management(uat_emp_hspt, uat_hspt_hi, name_select)
		
# Within selected features, further select only those cities which have a population > 10,000   
#arcpy.SelectLayerByAttribute_management(uat_hspt_lyr, "SUBSET_SELECTION", ' "GiZScore" > 2.58 ')
 
# Write the selected features to a new featureclass
#arcpy.CopyFeatures_management(uat_hspt_lyr, uat_hspt_hi)

print "Dissolve"

# Process: Dissolve
arcpy.Dissolve_management(uat_hspt_hi, uat_emp_hspt_dis, "FID", "", "MULTI_PART", "DISSOLVE_LINES")

# Process: Multipart To Singlepart
arcpy.MultipartToSinglepart_management(uat_emp_hspt_dis, uat_emp_hspt_split)

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(uat_emp_hspt, uat_hspt_lyr, "", "", "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;SOURCE_ID SOURCE_ID VISIBLE NONE;emp_dens emp_dens VISIBLE NONE;GiZScore GiZScore VISIBLE NONE;GiPValue GiPValue VISIBLE NONE")

print "Max"

# Process: Summary Statistics
arcpy.Statistics_analysis(uat_hspt_lyr, uat_hspt_max, "GiZScore MAX", "")

# Process: Add Join
arcpy.AddJoin_management(uat_hspt_lyr, "GiZScore", uat_hspt_max, "MAX_GiZSco", "KEEP_COMMON")

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(uat_emp_hspt_split, uat_split_lyr, "", "", "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;SOURCE_ID SOURCE_ID VISIBLE NONE;emp_dens emp_dens VISIBLE NONE;GiZScore GiZScore VISIBLE NONE;GiPValue GiPValue VISIBLE NONE")

print "Overlap - Extract Cluster"

# Process: Select Layer By Location
arcpy.SelectLayerByLocation_management(uat_split_lyr, "INTERSECT", uat_hspt_lyr, "", "NEW_SELECTION")

# Write the selected features to a new featureclass
arcpy.CopyFeatures_management(uat_split_lyr, uat_cen_cluster)