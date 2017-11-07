
import sys

countTotalHit=0

for line in sys.stdin:
	data = line.strip().split(" ")
	if "/assets/js/the-associates.js" in str(data[0]):
		countTotalHit = countTotalHit+1
		
		print countTotalHit
