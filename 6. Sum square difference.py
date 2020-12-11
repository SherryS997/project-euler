set1 = []
set2 = []
set3 = []
set4 = []
set5 = []


for x in range(1, 101):
    set1.append(int(x**2))
    set2.append(int(x))

set1 = int(sum(set1))
set2 = int(sum(set2))
set3.append(set1)
set4.append(set2)

for x in set4:
    set5.append(x**2)

for x in set5:
    set3.append(x)

ans = set3[1] - set3[0]

print(ans)