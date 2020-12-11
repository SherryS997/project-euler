import time

start = time.time()
n = 1
nos = [1]
no = 0

while n < (10 ** 999):
    nos.append(n)
    n += nos[(nos.index(n)) - 1]
    
nos.append(n)

print(len(nos))
total_time = time.time() - start

print("Done in " + str(total_time) + "s")