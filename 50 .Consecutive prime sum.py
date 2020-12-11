prime_nos = []
max_no = 0
limit = 1000000
length = 0


def eratosthenes(n):
    if n <= 2:
        return None
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples and i not in prime_nos:
            prime_nos.append(i)
            for j in range(i*i, n+1, i):
                multiples.add(j)

eratosthenes(limit)
length_primes = len(prime_nos)

for x in range(length_primes):
    for y in range((x + length), length_primes):
        nos = sum(prime_nos[x:y])
        if nos < limit:
            if nos in prime_nos:
                length = y - x
                max_no = nos
        else:
            length_primes = y + 1
            break
            
            

print(max_no)