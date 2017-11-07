import sys

path = {}

for line in sys.stdin:
	file_hits = line.strip()	

	if file_hits in path:
		path[file_hits] += 1
	else:
		path[file_hits] = 1

count, max_hits_path = max(zip(path.values(), path.keys()))
print count
