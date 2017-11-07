import sys

for line in sys.stdin:
    data = line.strip().split("GET ")
    if (len(data) >1):
        hit = data[1]
        print hit
