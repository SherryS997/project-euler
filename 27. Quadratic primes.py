max_consecutive_primes = 1
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

eratosthenes(100000)

def consecutive_primes(a, b):
    primes = []
    max_primes = []
    for n in range(1000):
        no = ((n ** 2) + (a * n) + b)
        if no in prime_nos:
            primes.append(no)
        else:
            break
    if len(primes) > len(max_primes):
        max_primes = primes
    return len(max_primes)

for a in range(-999, 1000):
    for b in range(-1000, 1000):
        if consecutive_primes(a, b) > max_consecutive_primes:
            max_consecutive_primes = consecutive_primes(a, b)
            max_product = a * b

print(max_consecutive_primes, max_product)