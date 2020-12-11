nos = []
num = 1

def factorial(no):
    num = 1
    for x in range(2, (no + 1)):
        num *= x
    return num

def combinations(n, r):
    ans = (factorial(n)) / ((factorial(r)) * (factorial(n - r)))
    return int(ans)

while num <= 100:
    for r in range(1, (num + 1)):
        if combinations(num, r) > 1000000:
            nos.append(combinations(num, r))
    num += 1

print(len(nos))