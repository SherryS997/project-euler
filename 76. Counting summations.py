n = 100

table = [0] * 101
table[0] = 1

for coin in range(1, 101):
    for i in range(coin, 101):
        table[i] += table[i - coin]

print(table[-1]-1)