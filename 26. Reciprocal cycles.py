target = 1000
prime_nos = []
max_digit = 1

def eratosthenes(n):
    if n <= 2:
        return None
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples and i not in prime_nos:
            prime_nos.append(i)
            for j in range(i*i, n+1, i):
                multiples.add(j)

eratosthenes(target)

def is_digit_length(no):
    for n in range(1, 1000):
        if ((10 ** n) - 1) % no == 0:
            return True
        else:
            False

def digit_length(no):
    for n in range(1, 1000):
        if ((10 ** n) - 1) % no == 0:
            return n

for x in prime_nos:
    if is_digit_length(x):
        if digit_length(x) > max_digit:
            max_digit = x


print(max_digit)