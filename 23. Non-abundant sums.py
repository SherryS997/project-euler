sum_abundant_nos = set()
abundant_nos = set()
non_sum_abundant_nos = set()

def is_abundant_no(no):
    divisors = []
    for x in range(1, no):
        if no % x == 0:
            divisors.append(x)
    sumation = sum(divisors)
    if sumation > no:
        return True

for x in range(1, 29000):
    if is_abundant_no(x):
        abundant_nos.add(x)

for x in abundant_nos:
    for y in abundant_nos:
        z = x + y
        sum_abundant_nos.add(z)

for x in range(1, 29000):
    if x not in sum_abundant_nos:
        non_sum_abundant_nos.add(x)
        

print(sum(non_sum_abundant_nos))