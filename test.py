import math


def pythagorean_triplet(n):
    triplets = []
    b = 2
    c = 0
    while c <= n:
        if b not in triplets:
            for a in range(1, b):
                c = math.sqrt(a * a + b * b)
                if c % 1 == 0:
                    triplets.append(a)
                    triplets.append(b)
                    triplets.append(c)
        b += 1
        print(b)
    return len(triplets) / 3


print(pythagorean_triplet(1500000))
