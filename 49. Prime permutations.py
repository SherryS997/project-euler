from itertools import permutations
import time

start = time.time()
prime_nos = set()
required_primes = set()
permutations_primes = []
answer = []

def eratosthenes(n):
    if n <= 2:
        return None
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples and i not in prime_nos:
            prime_nos.add(i)
            for j in range(i*i, n+1, i):
                multiples.add(j)

eratosthenes(10000)

for x in prime_nos:
    if x > 1000:
        required_primes.add(x)

def prime_permutations(no):
    pandigital_nos = set()
    primes = set()
    no = str(no)
    for x in permutations(no, len(no)):
        num = ''
        for y in x:
            num += y
            num = str(int(num))
            if len(num) == len(no):
                pandigital_nos.add(int(num))
    for x in pandigital_nos:
        if x in required_primes:
            primes.add(x)
    return primes

for k in required_primes:
    nos = prime_permutations(k)
    for x in nos:
        for y in nos:
            if x > y:
                for z in nos:
                    if y > z and (x - y) == (y - z) and (x, y, z) not in permutations_primes:
                        permutations_primes.append((x, y, z))

for y in permutations_primes[0]:
    if y not in answer:
        answer.append(y)
        answer = sorted(answer)

num = ''

for x in answer:
    x = str(x)
    num += x

num = int(num)

print(num)
total_time = time.time() - start

print("Done in " + str(total_time) + "s")