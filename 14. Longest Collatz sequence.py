import time

g = int(input('Max collatz sequence no under = '))
nos = []
k = []

start = time.time()

for a in range(1, g):
    n = a
    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            n = n / 2
            k.append(int(n))
        else:
            n = 3 * n + 1
            k.append(int(n))
        # nos.append(int(n))
        if len(k) > len(nos):
            nos = k
    k = []

no2 = nos[0]
ans = no2

if ans < g:
    ans = 2 * no2
else:
    ans = (no2 - 1) / 3
ans = int(ans)
length = len(nos)


total_time = time.time() - start

print("The no is " + str(ans))
print("The length of the sequence is " + str(length))
print("Total time taken = " + str(total_time) + "s")
