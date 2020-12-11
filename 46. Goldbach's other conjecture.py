prime_nos = set()
odd_composite_nos = set()
num = 1000000

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
for x in range(2, 10000):
    if x % 2 != 0 and x not in prime_nos:
        odd_composite_nos.add(x)

def is_Goldbachs_composite(no):
    for y in range(1, 100):
        for x in prime_nos:
            if x < no:
                    if no == x + (2 * (y ** 2)): 
                        return True


for x in odd_composite_nos:
    if not is_Goldbachs_composite(x) and x < num:
        num = x

print(num)
