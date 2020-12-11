factors = []

for x in range(1, 99999):
    if 100000 % x == 0:
        factors.append(x)

new_factors = []

for n in factors:
    for s in range(2, (n - 1)):
        if n % s != 0:
            new_factors.append(n)

print(max(new_factors))
