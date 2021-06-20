M = 1000000007

def smallest_sum_no(num):
    if num < 10: return num
    zeros = (num // 9)
    tens = 1
    if zeros > 10000:
        if zeros > M:
            print(True)
            zeros = zeros % (M - 1)
        while zeros > 100000:
            tens *= (10 ** 100000) % M
            zeros -= 100000
        tens *= (10 ** zeros) % M
    else: tens *= (10 ** zeros) % M
    tens = tens % M
    no = int(str(num % 9)) + 1
    no = (no * tens) - 1
    return no % M

def fib(n):
    a = 0
    b = 1
    if n == 0: return 0
    elif n == 1: return 1
    for x in range(n-1):
        c = a + b
        a = b
        b = c
    return c

def sum_small_nums(n):
    ans = 0
    for x in range(n + 1):
        ans = (ans + smallest_sum_no(x)) % M
    return ans % M

# print(sum_small_nums(fib(90)))
# print(smallest_sum_no(fib(90)))
# print(smallest_sum_no(fib(50)))
print(sum_small_nums(fib(30)))
