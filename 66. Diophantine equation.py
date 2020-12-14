from math import sqrt

def is_square(n):
    return sqrt(n).is_integer()

def diophantine_x(d):
    if is_square(d):
        return 0
    y = 0
    while True:
        y += 1
        y_sq = y * y
        eq = d * y_sq + 1
        req = 0
        if y > 1000000:
            break
        if is_square(eq):
            req = sqrt(eq)
            break
    return int(req)

result = 1
num = 1
max = 1

while num <= 1000:
    sol = diophantine_x(num)
    if sol > max:
        max = sol
        result = num
    num += 1
    print(num)

print(result)