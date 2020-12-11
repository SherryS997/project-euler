import time

start = time.time()

nos = []
prime_nos = set()

def eratosthenes(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            prime_nos.add(i)
            for j in range(i*i, n+1, i):
                multiples.add(j)

eratosthenes(1000000)

def rotations_no(no):
    noss = set()
    no = str(no)
    n = len(no)
    for x in range((n)):
        nx = (no[x:n]) + (no[0:x])
        nx = int(nx)
        noss.add(nx)
    return noss

def is_circular(no):
    nos = rotations_no(no)
    nos2 = set()
    for x in nos:
        if x in prime_nos:
            nos2.add(x)
    if nos2 == nos:
        return True

for x in prime_nos:
    if x not in nos and is_circular(x):
        nos.append(x)

print(len(nos))

total_time = time.time() - start

print("Done in " + str(total_time) + "s")