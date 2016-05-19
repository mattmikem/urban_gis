##Quick computation of distances from City Center of Tracts

from qgis.core import *

# supply path to where is your qgis installed
QgsApplication.setPrefixPath("C:\\OSGeo4W64\\apps\\qgis\\bin", True)

# load providers
QgsApplication.initQgis()

path    = "C:\\Users\\Matthew\\Desktop\\ECON\\Research\\Urban\\Papers\\City Center Resurgence\\GIS\\Working Files\\Output"
db_path = "C:\Users\\Matthew\\Dropbox\\Research\\Urban\\Data\\Analysis\\UA_ACS"

for c in range(0,1):
	
	vectorlayer_tracts = path + "ua_lehd_acs_" + str(c) + ".shp"
	vectorlayer_point  = path + "uat_cen_point_" + str(c) + ".shp"
	output_layer_alg0  = path + "ua_acs_points_" + str(c) + ".shp"
	distance_matrix_alg1= db_path + "distance_cc_" + str(c) + ".csv"
	
	outputs_0=Processing.runalg("qgis:polygoncentroids", vectorlayer_tracts, output_layer_alg0)
	outputs_1=Processing.runalg("qgis:distancematrix", outputs_0['OUTPUT_LAYER'], GEOID, vectorlayer_point, ID, 0, 0, distance_matrix_alg1)