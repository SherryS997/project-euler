import time

start = time.time()
quadruple_factor_nos = set()
prime_nos = set()

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

def is_quadruple_prime_factors(no):
    factors = set()
    for x in prime_nos:
        if x < no and no % x == 0:
            factors.add(x)
            if len(factors) == 4:
                return True
            else:
                False

no = 1

while True:
    if is_quadruple_prime_factors(no) and is_quadruple_prime_factors(no + 1) and is_quadruple_prime_factors(no + 2) and is_quadruple_prime_factors(no + 3):
        break
    else:
        no += 1

print(no)
total_time = time.time() - start

print("Done in " + str(total_time) + "s in Python")