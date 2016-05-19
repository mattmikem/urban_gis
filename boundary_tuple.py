# Import arcpy module
import arcpy
from arcpy import env
import sys
import shapefile
import shpUtils
import csv
import timeit

#python path: C:\Python27\ArcGIS10.3\python.exe

path  = "L:\\Research\\Resurgence\\GIS\\"
geo   = "L:\\Research\\Resurgence\\GIS\\Geography\\"
condo = "C:\\Users\\mmiller\\Dropbox\\Research\\Urban\\Papers\\Condos\\"

urban_10 = path+"urban_area_2010\\"
urban_areas_2010_shp = urban_10 + "urban_areas_2010.shp"

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

#Open city list from Justin

f = open(condo+'city_list.txt', 'r')

place_list = []

for lines in f:
		place_list = place_list + [lines.replace("\n","")]

f.close()

del place_list[0]

city_list = []
cs_list   = []

for c in place_list:
		city_list = city_list + [c[1:c.find(",")]]
		cs_list   = cs_list + [c[c.find(",")+2:-1].strip(" ")]

#city_list = str(tuple(city_list))		
#print city_list
		
#sys.exit(0)	
		

#------------------------------------------------------------------------

#State codes

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
		
state_dict  = {}
state_dict2 = {}

#print state_tuple[1:3]

#sys.exit(0)

for s in state_tuple:
		state_dict[s[2]] = s[1]
		state_dict2[s[0]]= s[2]

#print state_dict2['New York']
#print state_dict['NY']		
#sys.exit(0)		

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

n_s  = 40	
n_e  = 41

for c in range(n_s, n_e):

		start = timeit.default_timer()

		#Local variables for called city/urban area

		ua = ua_list[c]
		st = st_tuple[c]
		#l_city = len(city_tuple[c])+1
		
		print str(c)+" - "+ua
		
		#All states for UA to pull all possible places
		
		st_place_list = []
		for s in range(len(st)):
				st_place_list = st_place_list + [places + "tl_2010_" + state_dict[st[s]] + "_place10.shp"]

		print "- Merge for Multi-state Areas"
		
		ua_lehd_acs = tracts + "ua_lehd_acs_" + str(c) + ".shp"
		state_place_merge = "state_place_merge.shp"
		state_place_clip  = "state_place_clip.shp"
		ua_places = "ua_places"
		c_place_hold = "place_hold"
		urban_area = "urban_area"
		
		# # Process: Merge
		# #arcpy.Union_analysis(st_list[:len(st)], state_tracts_union_shp, "ALL", "", "GAPS")
		arcpy.Merge_management(st_place_list[:len(st)], state_place_merge)
		
		## Clip places with UA of interest
		
		name_select = "\"NAME10\" = '" + ua + "'"
		arcpy.MakeFeatureLayer_management(urban_areas_2010_shp, urban_area, name_select, "")
		
		arcpy.Clip_analysis(state_place_merge, urban_area , state_place_clip, "")
		
		clist = ["XXXX", "YYYY"]
		for i in range(len(city_list)):
				if state_dict2[cs_list[i]] in st:
						clist = clist + [city_list[i]]
		
		
		#if len(clist) == 1:
		#		clist = tuple(clist)+tuple("XXXX")
				
		print "- "+ str(clist)
		
		name_select = " \"NAME10\" IN " + str(tuple(clist))
		arcpy.MakeFeatureLayer_management(state_place_clip, ua_places, name_select, "")

		place_line_hold = lines + "places_line_" + str(c) + ".shp"
		
		# Process: Feature To Line
		arcpy.FeatureToLine_management(ua_places, place_line_hold, "", "ATTRIBUTES")
		
		# Process: Near calculation
		
		print "- Near Calculations"
		
		arcpy.Near_analysis(ua_lehd_acs, place_line_hold, "", "NO_LOCATION", "NO_ANGLE", "PLANAR")
		
		
		
		##This can be vastly improved by just computing a distance for each tract from boundary and merging on that one file!
		
		#for d in range(200,3200, 200):
				
		#		boundary_tracts = boundary + "boundary_tracts_" + str(d) + "_" + str(c) + ".shp"
				
		#		dist_str = str(d) + " Meters"
		
		#		arcpy.MakeFeatureLayer_management(ua_lehd_acs, urban_area_lyr)
		
				# Process: Select Layer By Location
		#		arcpy.SelectLayerByLocation_management(urban_area_lyr, "WITHIN_A_DISTANCE", place_line_hold, dist_str, "NEW_SELECTION", "NOT_INVERT")
		
				# Process: Copy Features
		#		arcpy.CopyFeatures_management(urban_area_lyr, boundary_tracts, "", "0", "0", "0")
		
		stop = timeit.default_timer()

		print "Time:" + str((stop - start)/60)
