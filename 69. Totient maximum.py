def totient_max(num):
    n = num
    result = n
    p = 2
    while(p * p <= n):
        if (n % p == 0):
            while (n % p == 0): n = int(n / p)
            result -= int(result / p)
        p += 1
    if (n > 1):
        result -= int(result / n)
    return num / result


no = 2
max = 1

while no <= 1000000:
    t_max = totient_max(no)
    if t_max > max:
        max = t_max
        ans = no
    no += 1

print(ans)
