import time

start = time.time()
multiplicants = [i for i in range(1, 10)]
num = ''
pandigits = set()
x = 1

while x < (10000):
    for y in multiplicants:
        digits = []
        no = x * y
        if len(num) < 9:
            num += str(no)
        if len(num) == 9:
            for z in num:
                if int(z) != 0:
                    if int(z) not in digits:
                        digits.append(int(z))
                    if len(digits) == len(multiplicants):
                        pandigits.add(int(num))
    num = ''
    digits = []
    x += 1

print(max(pandigits))
total_time = time.time() - start

print("Done in " + str(total_time) + "s in Python")