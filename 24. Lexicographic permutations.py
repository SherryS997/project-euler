import time
import itertools

start = time.time()
nos = []

nos_used = list('0123456789')

for c in itertools.combinations(nos_used, 10):
    for p in itertools.permutations(c):
        nos.append("".join(p))


nos.sort()

print(nos[999999])
total_time = time.time() - start

print("Done in " + str(total_time) + "s")