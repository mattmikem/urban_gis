# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# proj_cal.py
# Created on: 2014-04-28 15:29:38.00000
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
urban_area_tracts_0 = "urban_area_tracts_0.shp"
urban_area_tracts_prj_0 = "C:\\Users\\Matthew\\Desktop\\ECON\\Research\\Urban\\Papers\\City Center Resurgence\\GIS\\Working Files\\Output\\urban_area_tracts_prj_0.shp"
urban_area_tracts_prj_0_lyr = "C:\\Users\\Matthew\\Desktop\\ECON\\Research\\Urban\\Papers\\City Center Resurgence\\GIS\\Working Files\\Output\\urban_area_tracts_prj_0"
wac = "C:\\Users\\Matthew\\Desktop\\ECON\\Research\\Urban\\Papers\\City Center Resurgence\\GIS\\Working Files\\wac_trct.xlsx\\wac$"	
layerName = "urban_tracts_lyr"
valid_trcts = "valid_trcts"
	
urban_area_tracts = "urban_area_tracts_0.dbf"

#Top n Urban Areas to loop over

n = 10

#--------------------------------------------------------------------

#Import Urban Area List for Loop

f = open('M:\\Research\\Urban\\Resurgence\\ACS\\Output\\ua_rank_2010.txt', 'r')

ua_list = []
		
for lines in f:
		ua_list = ua_list + [lines.replace("\n","")]
		

del ua_list[0]

print ua_list[:n]

st = []

for c in ua_list:
		st = st + [c[c.find(",")+2:]]
		
st_tuple = []		
for s in st:
		st_tuple = st_tuple + [tuple(s.split("--"))]

# for c in range(N):
		# print ua[c]
		# st = st_tuple[c]
		# for s in range(len(st)):
				# print st[s]
				
				
		#sys.exit(0)

f.close()	
#------------------------------------------------------------------------
	
#ID UTM ZONE

#UTM Dictionary

# utm_dict = {}
# utm_dict['10'] = (120,126)
# utm_dict['11'] = (114, 119)	
# utm_dict['12'] = (108, 113)
# utm_dict['13'] = (102, 107)
# utm_dict['14'] = (96, 101)
# utm_dict['15'] = (90, 95)
# utm_dict['16'] = (84, 89)
# utm_dict['17'] = (78, 83)
# utm_dict['18'] = (72, 77)	

#UTM Tuple

utm_tuple = [(120, 127, '10')]+[(114,119,'11')]+[(108, 113, '12')]+[(102,107,'13')]\
           +[(96,101, '14')]+[(90,95, '15')]+[(84,89, '16')]+[(78,83,'17')]+[(72,77,'18')]+[(66,71,'19')]
		   
		  
print utm_tuple
	
#Pull longitude from tracts file	

#Import Urban Area List for Loop

f = open('C:\\Users\\Matthew\\Desktop\\ECON\\Research\\Urban\\Papers\\City Center Resurgence\\GIS\\urban_area_2010\\Urban_Areas_Long_2010.txt', 'r')

ua_list_2 = []
		
for lines in f:
		ua_list_2 = ua_list_2 + [lines.replace("\n","")]
		

del ua_list_2[0]
ua_tuple = []

for u in ua_list_2:
		ua_tuple = ua_tuple + [tuple(u.split("*"))]
		
#print ua_list[:n]

ua_dict = {}

for u in ua_tuple:
		#print u[1]
		ua_dict[u[0]] = abs(int(float(u[1])))

#print ua_dict['Boston, MA--NH--RI']

long_dict = {}

for u in ua_dict:
		for utm in utm_tuple:
				if ua_dict[u] >= utm[0] and ua_dict[u] <= utm[1]: long_dict[u] = utm[2]
				
#print ua_dict		
# print ua_dict['"Los Angeles--Long Beach--Anaheim, CA"']
# print ua_dict['"Santa Barbara, CA"']

# print long_dict['"Los Angeles--Long Beach--Anaheim, CA"']
# print long_dict['"Santa Barbara, CA"']

# print long_dict

#------------------------------------------------------------------

for c in range(n):
		
		ua = ua_list[c]
		st = st_tuple[c]
		
		urban_area_tracts = "urban_area_tracts_"+str(c)+".shp"
		urban_area_join   = "urban_area_lehd_join_"+str(c)+".shp"
		urban_area_tracts_prj = "urban_area_tracts_prj.shp"
		uat_emp_hspt = "uat_emp_hspt_"+str(c)+".shp"
	
		print "("+str(c)+") "+ua
		print "- Project"
		# Process: Project
		#arcpy.Project_management(urban_area_tracts_0, urban_area_tracts_prj_0, "PROJCS['NAD_1983_UTM_Zone_18N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-75.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "", "GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
		 
		utm_zone = 'NAD 1983 UTM Zone '+long_dict[ua]+'N'
		print "- "+utm_zone
		outCS = arcpy.SpatialReference(utm_zone)
		arcpy.Project_management(urban_area_tracts, urban_area_tracts_prj, outCS)

		print "- Add Area Field"
		# Process: Add Field
		arcpy.AddField_management(urban_area_tracts_prj, "AREA", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

		print "- Compute Area"
		# Process: Calculate Field
		arcpy.CalculateField_management(urban_area_tracts_prj, "AREA", "!SHAPE.AREA@SQUAREMILES!", "PYTHON_9.3")

		print "- Join to LEHD"
		# Process: Feature Layer
		arcpy.MakeFeatureLayer_management (urban_area_tracts_prj,  layerName)
		# Process: Add Join
		arcpy.AddJoin_management(layerName, "GEOID", wac, "trct", "KEEP_COMMON")
		arcpy.CopyFeatures_management(layerName, urban_area_join)		

		print "- Limit to Non-Truncated Tracts"
		# Process: Make Feature Layer
		thr = 0.01
		name_select = "\"AREA\" > " + str(thr)
		#print name_select
		# Process: Make Feature Layer
		arcpy.MakeFeatureLayer_management(urban_area_join, valid_trcts, "\"AREA\" > 0.01", "", "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;STATEFP STATEFP VISIBLE NONE;COUNTYFP COUNTYFP VISIBLE NONE;TRACTCE TRACTCE VISIBLE NONE;GEOID GEOID VISIBLE NONE;NAME NAME VISIBLE NONE;NAMELSAD NAMELSAD VISIBLE NONE;MTFCC MTFCC VISIBLE NONE;FUNCSTAT FUNCSTAT VISIBLE NONE;ALAND ALAND VISIBLE NONE;AWATER AWATER VISIBLE NONE;INTPTLAT INTPTLAT VISIBLE NONE;INTPTLON INTPTLON VISIBLE NONE;AREA AREA VISIBLE NONE;state state VISIBLE NONE;trct trct VISIBLE NONE;trctname trctname VISIBLE NONE;ca01 ca01 VISIBLE NONE;ca02 ca02 VISIBLE NONE;ca03 ca03 VISIBLE NONE;ce01 ce01 VISIBLE NONE;ce02 ce02 VISIBLE NONE;ce03 ce03 VISIBLE NONE;cns01 cns01 VISIBLE NONE;cns02 cns02 VISIBLE NONE;cns03 cns03 VISIBLE NONE;cns04 cns04 VISIBLE NONE;cns05 cns05 VISIBLE NONE;cns06 cns06 VISIBLE NONE;cns07 cns07 VISIBLE NONE;cns08 cns08 VISIBLE NONE;cns09 cns09 VISIBLE NONE;cns10 cns10 VISIBLE NONE;cns11 cns11 VISIBLE NONE;cns12 cns12 VISIBLE NONE;cns13 cns13 VISIBLE NONE;cns14 cns14 VISIBLE NONE;cns15 cns15 VISIBLE NONE;cns16 cns16 VISIBLE NONE;cns17 cns17 VISIBLE NONE;cns18 cns18 VISIBLE NONE;cns19 cns19 VISIBLE NONE;cns20 cns20 VISIBLE NONE;cr01 cr01 VISIBLE NONE;cr02 cr02 VISIBLE NONE;cr03 cr03 VISIBLE NONE;cr04 cr04 VISIBLE NONE;cr05 cr05 VISIBLE NONE;cr07 cr07 VISIBLE NONE;ct01 ct01 VISIBLE NONE;ct02 ct02 VISIBLE NONE;cd01 cd01 VISIBLE NONE;cd02 cd02 VISIBLE NONE;cd03 cd03 VISIBLE NONE;cd04 cd04 VISIBLE NONE;cs01 cs01 VISIBLE NONE;cs02 cs02 VISIBLE NONE;cfa01 cfa01 VISIBLE NONE;cfa02 cfa02 VISIBLE NONE;cfa03 cfa03 VISIBLE NONE;cfa04 cfa04 VISIBLE NONE;cfa05 cfa05 VISIBLE NONE;cfs01 cfs01 VISIBLE NONE;cfs02 cfs02 VISIBLE NONE;cfs03 cfs03 VISIBLE NONE;cfs04 cfs04 VISIBLE NONE;cfs05 cfs05 VISIBLE NONE;emp_dens emp_dens VISIBLE NONE")

		print "- Add Emp Dens Field"
		# Process: Add Field
		arcpy.AddField_management(valid_trcts, "EMP_DENS", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

		print "- Compute Emp Dens"
		# Process: Calculate Field
		arcpy.CalculateField_management(valid_trcts, "emp_dens", "[ca01]/ [AREA]", "VB", "")

		print "- Employment Clusters - 500 m"
		# Process: Hot Spot Analysis (Getis-Ord Gi*)
		arcpy.HotSpots_stats(valid_trcts, "emp_dens", uat_emp_hspt, "FIXED_DISTANCE_BAND", "EUCLIDEAN_DISTANCE", "NONE", "500", "", "")



