pentagon_numbers = set()
difference = set()

for n in range(1, 10000):
    num = (n * ((3 * n) - 1) / 2)
    pentagon_numbers.add(int(num))

while len(difference) == 0:
    for x in pentagon_numbers:
        for y in pentagon_numbers:
            if y > x and (y + x) in pentagon_numbers and (y - x) in pentagon_numbers:
                num = y - x
                difference.add(num)

print(difference)