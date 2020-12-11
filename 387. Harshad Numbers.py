def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_harshad(x):
    no = 0
    for i in str(x):
        no += int(i)
    if x % no == 0:
        return True
    else:
        return False


def is_strong(x):
    no = 0
    for i in str(x):
        no += int(i)
    if is_prime((x / no)):
        return True
    else:
        return False


def is_right_truncatable_harshad(x):
    for
