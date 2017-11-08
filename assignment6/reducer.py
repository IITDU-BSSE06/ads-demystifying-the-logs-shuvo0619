import sys

path = {}

count9=0
count10=0
count11=0

for line in sys.stdin:
	file_hits = line.strip()
	
	if "2009" in path:
		count9 = count9+1
	else if "2010" in path:
		count10 = count10+1
	else if "2011" in path:
		count11 = count11+1
	
print "2009" count9
print "2010" count10
print "2011" count11
