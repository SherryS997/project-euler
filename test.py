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

print(smallest_sum_no(10000000070))