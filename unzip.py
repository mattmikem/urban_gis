#Generic code to unzip large set of files.
#This is done for 'place' census files which are by state.

import zipfile
import os

#'path' - directory where files are located
#'zip' - 0 for unzip, 1 for zip

def unzip(path):
	for f in os.listdir(path):
		if ".zip" in f:
			f = path + "\\" + f
			zfile = zipfile.ZipFile(f,"r")
			zfile.extractall(path)
		

###IMPLEMENT BELOW THIS LINE, CALL 'UNZIP'
		
#test_path = "L:\\Research\\Resurgence\\GIS\\Geography\\Places\\Test"
#unzip(test_path)

place = "L:/Research/Resurgence/GIS/Geography/PUMA/"

unzip(place)