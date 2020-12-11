import time

start = time.time()
# triangular_nos = set()
pentagonal_numbers = set()
hexagonal_nos = set()
nos = 40755

for n in range(1, 100000):
    num = (n * ((3 * n) - 1) / 2)
    pentagonal_numbers.add(int(num))

for n in range(1, 100000):
    num = n * ((2 * n) - 1)
    hexagonal_nos.add(int(num))

while nos <= 40755:
    for x in pentagonal_numbers:
        if x in hexagonal_nos and x > 40755:
            nos = x

print(nos)
total_time = time.time() - start

print("Done in " + str(total_time) + "s in Python")