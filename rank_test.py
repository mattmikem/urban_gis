import sys

def ua_list(n):

		f = open('M:\\Research\\Urban\\Resurgence\\ACS\\Output\\ua_rank_2010.txt', 'r')

		print f

		ua = []
		
		for lines in f:
				ua = ua + [lines.replace("\n","")]
		

		del ua[0]

		print ua[:n]

		st = []

		for c in ua:
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
				
		return ua[:n]
		return st_tuple[:n]
		
		