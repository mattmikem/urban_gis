# Import arcpy module
import arcpy
from arcpy import env
import sys
import shapefile
import shpUtils
import csv
import timeit

#python path: C:\Python27\ArcGIS10.3\python.exe

path = "L:\\Research\\Resurgence\\GIS\\"
geo  = "L:\\Research\\Resurgence\\GIS\\Geography\\"

#Overwriting allowed
arcpy.env.overwriteOutput = True

#Working Directory
arcpy.env.workspace = "L:\\Research\\Resurgence\\GIS\\Working Files\\Output\\Test"
arcpy.env.qualifiedFieldNames = False

#--------------------------------------------------------------------

#Import Urban Area List for Loop

f = open(path+'Working Files\\ua_rank_2010.txt', 'r')

ua_list = []

for lines in f:
		ua_list = ua_list + [lines.replace("\n","")]


del ua_list[0]

#print ua_list[:n]

st_tuple = []
cty_tuple = []

for c in ua_list:
		st_tuple = st_tuple + [tuple(c[c.find(",")+2:].split("--"))]
		cty_tuple = cty_tuple + [tuple(c[:c.find(",")].split("--"))]

				
#city_tuple = []
#for c in 

# for c in range(N):
		# print ua[c]
		# st = st_tuple[c]
		# for s in range(len(st)):
				# print st[s]


		#sys.exit(0)

f.close()
#------------------------------------------------------------------------

f = open(geo+'StateCodes.csv', 'r')

state_list = []

for lines in f:
		state_list = state_list + [lines.replace("\n","")]

f.close()

del state_list[0]	

##state_tuple refers to the state FIPS lookup
##st_tuple refers to the tuple of states for a particular UA
	
state_tuple = []
	
for s in state_list:
		state_tuple = state_tuple + [tuple(s.split(","))]
		
state_dict = {}

for s in state_tuple:
		state_dict[s[2]] = s[1]


##Loop through UA

# Local variables:
tracts = "L:\\Research\\Resurgence\\GIS\\Working Files\\Output\\Test\\"
places = "L:\\Research\\Resurgence\\GIS\\Geography\\Places\\"
lines = "L:\\Research\\Resurgence\\Working Files\\Place Dissolve\\"
boundary = "L:\\Research\\Resurgence\\Working Files\\Boundary\\"

#ua_lehd_acs_1__2_ = ua_lehd_acs_1
#tl_2010_06_place10 = "tl_2010_06_place10"
#l_2010_06_place10_Layer = "tl_2010_06_place10_Layer"
#place_line_hold_shp = "L:\\Research\\Resurgence\\Working Files\\Place Dissolve\\place_line_hold.shp"
#boundary_tracts_hold_shp = "L:\\Research\\Resurgence\\Working Files\\Boundary\\boundary_tracts_hold.shp"

#Distance is set to meters (loop within a city)

n_s  = 0	
n_e  = 101

for c in range(n_s, n_e):

		start = timeit.default_timer()

		#Local variables for called city/urban area

		ua = ua_list[c]
		st = st_tuple[c][0]
		city = cty_tuple[c][0]
		
		ua_lehd_acs = tracts + "ua_lehd_acs_" + str(c) + ".shp"
		c_place = places + "tl_2010_" + state_dict[st] + "_place10.shp"
		c_place_hold = "place_hold"
		urban_area_lyr = "urban_area_lyr"
		place_line_hold = lines + "place_line_" + str(c) + ".shp"
		

		print "("+str(c)+") "+city+ ", " + st
		
		#Feature to Line for Central City in State 'st'
		
		name_select = "\"NAME10\" = '" + city+ "'"
		
		# Process: Make Feature Layer
		arcpy.MakeFeatureLayer_management(c_place, c_place_hold, name_select, "", "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;STATEFP10 STATEFP10 VISIBLE NONE;PLACEFP10 PLACEFP10 VISIBLE NONE;PLACENS10 PLACENS10 VISIBLE NONE;GEOID10 GEOID10 VISIBLE NONE;NAME10 NAME10 VISIBLE NONE;NAMELSAD10 NAMELSAD10 VISIBLE NONE;LSAD10 LSAD10 VISIBLE NONE;CLASSFP10 CLASSFP10 VISIBLE NONE;PCICBSA10 PCICBSA10 VISIBLE NONE;PCINECTA10 PCINECTA10 VISIBLE NONE;MTFCC10 MTFCC10 VISIBLE NONE;FUNCSTAT10 FUNCSTAT10 VISIBLE NONE;ALAND10 ALAND10 VISIBLE NONE;AWATER10 AWATER10 VISIBLE NONE;INTPTLAT10 INTPTLAT10 VISIBLE NONE;INTPTLON10 INTPTLON10 VISIBLE NONE")

		# Process: Feature To Line
		arcpy.FeatureToLine_management(c_place_hold, place_line_hold, "", "ATTRIBUTES")
		
		##This can be vastly improved by just computing a distance for each tract from boundary and merging on that one file!
		
		for d in range(200,3200, 200):
				
				boundary_tracts = boundary + "boundary_tracts_" + str(d) + "_" + str(c) + ".shp"
				
				dist_str = str(d) + " Meters"
		
				arcpy.MakeFeatureLayer_management(ua_lehd_acs, urban_area_lyr)
		
				# Process: Select Layer By Location
				arcpy.SelectLayerByLocation_management(urban_area_lyr, "WITHIN_A_DISTANCE", place_line_hold, dist_str, "NEW_SELECTION", "NOT_INVERT")
		
				# Process: Copy Features
				arcpy.CopyFeatures_management(urban_area_lyr, boundary_tracts, "", "0", "0", "0")
		
		stop = timeit.default_timer()

		print "Time:" + str((stop - start)/60)
