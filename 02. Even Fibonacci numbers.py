nos = [x for x in range(1,400)]
new_nos = [nos[n] for n in range(2)]

for x in range(30):
    new_nos.append((new_nos[x] + new_nos[x + 1]))

new_nos2 = []

for n in new_nos:
    if n % 2 ==0:
        new_nos2.append(n)

print(sum(new_nos2))
