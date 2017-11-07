
import sys

for line in sys.stdin:
    data = line.strip().split(" ")

    if (len(data) >1):
        hit = data[0]

        print hit
