import time

# def num_divisors(n):
#     f = True
#     divisors = set()
#     while f is True:
#         z = 0
#         if n == 1:
#             a = 1
#             return a
#         else:
#             for i in range(1, n+1):
#                 if n % i == 0:
#                     divisors.add(i)
#                     a = len(divisors)
#                     if a > z:
#                         z = a
#                     else:
#                         f = False
#                         return a
def num_divisors(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors

# def triangle_no(factor_limit):
#     i = 1
#     j = 1
#     n = num_divisors(i)
#     while n < factor_limit:
#         j += 1
#         i += j
#         n = num_divisors(i)
#     return i

def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, num_divisors(n+1)
    return n

start = time.time()
index = find_triangular_index(500)
triangle = (index * (index + 1)) / 2
elapsed = (time.time() - start)
 
print ("result %s returned in %s seconds." % (triangle,elapsed))