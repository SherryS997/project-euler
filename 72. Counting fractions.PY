minimum = 1000000
p = []


def sieve():
    isPrime = [0] * (minimum + 1)
    for i in range(2, minimum + 1):
        if (isPrime[i] == 0):
            p.append(i)
            j = 2
            while (i * j <= minimum):
                isPrime[i * j] = 1
                j += 1


sieve()


def phi(n):
    res = n
    i = 0
    while (p[i] * p[i] <= n):
        if (n % p[i] == 0):
            res -= int(res / p[i])
            while (n % p[i] == 0):
                n = int(n / p[i])
        i += 1
    if (n > 1):
        res -= int(res / n)
    return res


no = 2
count = 0

while no <= minimum:
    count += phi(no)
    no += 1

print(count)
