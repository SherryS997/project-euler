prime_nos = []

def eratosthenes(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            prime_nos.append(i)
            for j in range(i*i, n+1, i):
                multiples.add(j)

eratosthenes(2000000)
print(sum(prime_nos))