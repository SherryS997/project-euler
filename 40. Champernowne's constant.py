Champernowne_constant = []

while len(Champernowne_constant) < 100010:
    for x in range(1000000):
        for y in str(x):
            Champernowne_constant.append(y)

ans = int(Champernowne_constant[1]) * int(Champernowne_constant[10]) * int(Champernowne_constant[100]) * int(Champernowne_constant[1000]) * int(Champernowne_constant[10000]) * int(Champernowne_constant[100000]) *  int(Champernowne_constant[1000000])

print(ans)