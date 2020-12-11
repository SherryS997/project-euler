n = input("Power Digit Sum = ")
j = [2 ** int(n)]
j = str(j)
k = []

for x in range(1, (len(j) - 1)):
    k.append(int(j[x]))

print(k)
print(sum(k))