from math import sqrt
import math

def smallest_sum_no(num):
    nines = int(num / 9)
    init = int(num % 9)
    result = int(((init + 1) * (10 ** nines)) - 1)
    raised = 1
    req = 0
    sol = int(math.exp(math.log(1000000007) * raised)) + 1
    while sol <= result:
        req = raised
        raised *= 2
        sol = int(math.exp(math.log(1000000007) * raised)) + 1
        # print(raised)
    if req > 0:
        sol2 = result - (1000000007 ** (req))
        sol2 = (result % 1000000007) + req
    else:
        sol2 = (result % 1000000007)
    return sol2


def summation_above(limit):
    limit = limit
    result = 0
    for x in range(1, limit + 1):
        # print(x)
        result += smallest_sum_no(x)
    return int(result)

print(summation_above(1000000))
