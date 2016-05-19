##Download Census Tiger Files

import urllib

#states = ["AL", "AK", "AL", "AR", "AZ", "CO", "DE", "DC", "FL", "GA", "IA", "ID", "IL", "IN", "KS"\
#          , "KY", "LA", "MA", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH"\
#		  , "NM", "NV", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT"\
#		  , "WA", "WI", "WV", "WY"]


##Area Water

#link = "ftp://ftp2.census.gov/geo/tiger/TIGER2010/AREAWATER/"
#path = "C:\\Users\\Matthew\\Desktop\\ECON\\Research\\Urban\\GIS\\General\\Hydrography\\Census Tiger\\"

#for i in range(70,78):
	
#	if i < 10:
#		s = "0"+str(i)
#	else:
#		s = str(i)
		
#	for j in range(1,500):
		
#		if j < 10:
#			c = "00"+str(j)
#		elif j < 100:
#			c = "0" + str(j)
#		else:
#			c = str(j)

#		print s+" , "+c

#		url  = link + "tl_2010_"+s+c+"_areawater.zip"
#		name = path + "tl_2010_"+s+c+"_areawater.zip"
	
#		try:
#			urllib.urlretrieve (url, name)

#		except IOError:
#			print "Next"
 
	
##Place

# link = "ftp://ftp2.census.gov/geo/tiger/TIGER2010/PLACE/2010/"
# path = "C:\\Users\\Matthew\\Desktop\\ECON\\Research\\Urban\\GIS\\General\\Places\\"

# for i in range(1,78):
	# if i < 10:
		# s = "0"+str(i)
	# else:
		# s = str(i)
	
	# url  = link + "tl_2010_"+s+"_place10.zip"
	# name = path + "tl_2010_"+s+"_place10.zip"
	
	# try:
		# urllib.urlretrieve (url, name)
		
	# except IOError:
		# print "No " + str(i) + "- Onto the next"


#PUMA

##Can vary type of geography and location (this, like place, loops through states, the above loops through counties as well)

link = "ftp://ftp2.census.gov/geo/tiger/TIGER2010/PUMA5/2010/"
path = "L:/Research/Resurgence/GIS/Geography/PUMA/"
stem = "puma"
year = 2010

for i in range(1,78):
		if i < 10:
				s = "0"+str(i)
		else:
				s = str(i)
	
		url  = link + "tl_"+str(year)+"_"+s+"_"+stem+"10.zip"
		name = path + "tl_"+str(year)+"_"+s+"_"+stem+"10.zip"
	
		try:
				urllib.urlretrieve (url, name)
		
		except IOError:
				print "No " + str(i) + "- Onto the next"
			
			

	