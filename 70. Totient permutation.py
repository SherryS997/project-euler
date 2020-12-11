minimum = 10 ** 7
p = []
NO_OF_CHARS = 256


def is_permutated(str1, str2):
    str1 = str(str1)
    str2 = str(str2)
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS
    for i in str1:
        count1[ord(i)] += 1
    for i in str2:
        count2[ord(i)] += 1
    if len(str1) != len(str2):
        return 0
    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0

    return 1


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

    # this loop runs sqrt(n / ln(n)) times
    i = 0
    while (p[i] * p[i] <= n):
        if (n % p[i] == 0):

            # subtract multiples of p[i] from r
            res -= int(res / p[i])

            # Remove all occurrences of p[i] in n
            while (n % p[i] == 0):
                n = int(n / p[i])
        i += 1

    # when n has prime factor greater
    # than sqrt(n)
    if (n > 1):
        res -= int(res / n)

    return res


n = 100

while n < 10 ** 7:
    if is_permutated(n, (phi(n))):
        num = n / phi(n)
        if num < minimum:
            minimum = num
            ans = n
    n += 1
    print(n)

print(ans)
