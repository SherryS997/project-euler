nthnum = 0


for n in range(1, 10):
    x = 1
    while True:
        if x == len(str(n ** x)):
            nthnum += 1
        else:
            break
        x += 1

print(nthnum)

# print(ispossible(25))
