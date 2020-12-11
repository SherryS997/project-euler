import time

start = time.time()
prime_nos = set()
truncatable_primes = []

def eratosthenes(n):
    if n <= 2:
        return None
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples and i not in prime_nos:
            prime_nos.add(i)
            for j in range(i*i, n+1, i):
                multiples.add(j)

eratosthenes(1000000)

def is_truncatable(no):
    nos = set()
    primes = set()
    if no < 10:
        return False        
    no = str(no)
    num = str(no)
    while len(num) > 1:
        num = int(num)
        nos.add(num)
        num = str(int(num / 10))
    nos.add(int(num))
    num = str(no)
    while len(num) > 1:
        num = int(num)
        if num not in nos:
            nos.add(num)
        num = str(num)
        num = num[::-1]
        num = str(int(int(num) / 10))
        num = num[::-1]
    nos.add(int(num))
    for x in nos:
        if x in prime_nos:
            primes.add(x)
    if nos == primes:
        return True
    else:
        return False


for no in prime_nos:
    if len(truncatable_primes) < 11:
        if is_truncatable(no):
            truncatable_primes.append(no)

print(truncatable_primes)
print(sum(truncatable_primes))
total_time = time.time() - start

print("Done in " + str(total_time) + "s in Python")