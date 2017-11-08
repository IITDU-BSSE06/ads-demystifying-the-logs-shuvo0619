from urlparse import urlparse
import sys

for line in sys.stdin:
    data = line.strip().split("GET")
    if len(data) == 2:
	
	print urlparse(data[0]).path
