nos = set()

for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        nos.add(x)

print(sum(nos))