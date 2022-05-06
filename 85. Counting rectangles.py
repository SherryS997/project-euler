curr = 1
i = 2

while curr <= 2 * 10 ** 8:
    curr += i ** 3
    i += 1

print(i - 1)