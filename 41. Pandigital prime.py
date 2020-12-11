import time

start = time.time()
largest_no = 1
nos = set()
multiples = set()
prime_nos = set()

def eratosthenes(n):
    if n <= 2:
        return None
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples and i not in prime_nos:
            prime_nos.add(i)
            for j in range(i*i, n+1, i):
                multiples.add(j)

eratosthenes(7654321)

def is_pandigital(no):
    length = len(str(no)) + 1
    num1 = {i for i in range(1, length)}
    num2 = set()
    no = str(no)
    for x in no:
        num2.add(int(x))
    if num1 == num2:
        return True
    else:
        return False


for num in prime_nos:
    if is_pandigital(num) and num > largest_no:
        largest_no = num

print(largest_no)
total_time = time.time() - start

print("Done in " + str(total_time) + "s in Python")