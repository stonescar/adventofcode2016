from collections import defaultdict
import hashlib

salt = "ahsbgdzn"
trips = defaultdict(dict)
keys = []

x = 0
stop = 99999999


while x < stop:
	hash = hashlib.md5(salt+str(x)).hexdigest()
	for i in range(len(hash)-2):
		if hash[i] * 2 == hash[i+1:i+3] and hash[i] *3 != hash[i+1:i+4] and not trips.has_key(x):
			trips[x] = hash[i]
		if hash[i] * 4 == hash[i+1:i+5]:
			for j in trips.items():
				if hash[i] == j[1]:
					keys.append(j[0])
					if len(keys) == 64:
						stop = x+1000
		for j in trips.items():
			if j[0]+1000 < x:
				del trips[j[0]]
	x += 1
	
print sorted(keys)[63]
