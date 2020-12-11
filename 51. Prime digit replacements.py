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

def max_prime_value_family_no(no):
    num = str(no)
    length = len(num)
    print(length)

max_prime_value_family_no(13)