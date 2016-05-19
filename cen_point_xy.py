# Import arcpy module
import arcpy
from arcpy import env
import sys
import shapefile
import shpUtils
import timeit

path = "L:\\Research\\Resurgence\\GIS\\"

#Overwriting allowed
arcpy.env.overwriteOutput = True

#Working Directory
arcpy.env.workspace = "L:\\Research\\Resurgence\\GIS\\Working Files\\Output\\Test"
arcpy.env.qualifiedFieldNames = False

#Import Urban Area List for Loop

f = open(path+'Working Files\\ua_rank_2010.txt', 'r')

ua_list = []

for lines in f:
		ua_list = ua_list + [lines.replace("\n","")]


del ua_list[0]

n_s = 0
n_e = 101

for c in range(n_s, n_e):

		ua = ua_list[c]
		
		print "("+str(c)+") "+ua

		start = timeit.default_timer()
		
		uat_cen_point = "uat_cen_point_"+str(c)+".shp"
		uat_cen_xy    = "ua_cen_xy_"+str(c)+".shp"
		
		# Process: Project
		out_gcs = arcpy.SpatialReference('WGS 1984')
		arcpy.Project_management(uat_cen_point, uat_cen_xy, out_gcs)

		# Process: Add XY Coordinates
		arcpy.AddXY_management(uat_cen_xy)
		
		stop = timeit.default_timer()

		print "Time:" + str((stop - start)/60)