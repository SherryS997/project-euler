from itertools import permutations

pandigital_nos = set()
prime_nos = []
special_pandigital_nos = set()

def eratosthenes(n):
    if n <= 2:
        return None
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples and i not in prime_nos:
            prime_nos.append(i)
            for j in range(i*i, n+1, i):
                multiples.add(j)

eratosthenes(18)

for x in permutations('0123456789', 10):
    num = ''
    for y in x:
        num += y
        num = str(int(num))
        if len(num) == 10:
            pandigital_nos.add(int(num))

for x in pandigital_nos:
    check = set()
    x = str(x)
    for y in range(1, 8):
        num = x[y:(y + 3)]
        num = int(num)
        if num % prime_nos[(y - 1)] == 0:
            check.add(prime_nos[(y - 1)])
        if len(check) == len(prime_nos):
            special_pandigital_nos.add(int(x))
    check = set()
            
print(sum(special_pandigital_nos))