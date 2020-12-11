from math import gcd
from fractions import Fraction


def coprimes(num):
    coprimes = []
    coprimes.append(Fraction(1, num))
    multiples = set()
    if num == 2:
        coprimes.append(Fraction(1, 2))
        return coprimes
    for x in range(2, (num + 1)):
        if x not in multiples:
            if gcd(x, num) == 1:
                coprimes.append(Fraction(x, num))
            else:
                for j in range(x*x, num+1, x):
                    multiples.add(j)
    return coprimes


count = 0
num = 2

while num <= 12000:
    print(num)
    for x in coprimes(num):
        if x > Fraction(1, 3) and x < Fraction(1, 2):
            count += 1
    num += 1

print(count)
