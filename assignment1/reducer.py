import sys

countTotalHit=0

for line in sys.stdin:
	data = line.strip().split(" ")
	hitIP= str(data[0])
	if "10.99.99.186" == hitIP:
		countTotalHit = countTotalHit+1


print countTotalHit
