nos = []

def is_pandigital(a, b, c):
    no = (str(a) + str(b) + str(c))
    num1 = {i for i in range(1, 10)}
    num2 = set()
    for x in no:
        num2.add(int(x))
    if num1 == num2:
        return True
    else:
        return False

for a in range(1, 100):
    for b in range(100, 10000):
        c = a * b
        if 1000 <= c <= 9999 and is_pandigital(a, b, c) and c not in nos:
            nos.append(c)


print(sum(nos))
# print(is_pandigital(39, 784, 1256))