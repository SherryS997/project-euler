import time

start = time.time()
nos = []

def is_palindromic(n):
    n = str(n)
    return n == n[::-1]


def num_reverse(no):
    num = str(no)
    num2 = num[::-1]
    return int(num2)

def is_Lychrel_num(no):
    number = 1
    required_num = no + num_reverse(no)
    if is_palindromic(required_num):
        return False
    else:
        while number < 50:
            required_num += num_reverse(required_num)
            if is_palindromic(required_num):
                return False
            else:
                number += 1
        return True

for x in range(1, 10000):
    if is_Lychrel_num(x):
        nos.append(x)

print(len(nos))
total_time = time.time() - start

print("Done in " + str(total_time) + "s")