import time

start = time.time()
number = 1

def digits(no):
    digit_list = []
    num = str(no)
    for x in num:
        digit_list.append(int(x))
    digit_list.sort()
    return digit_list

def is_Permuted_Multiples(no, multiples):
    nos = set()
    nums = []
    for x in range(1, (multiples + 1)):
        nums.append((no * x))
    for y in nums:
        nos.add(str(digits(y)))
    if len(nos) == 1:
        return True
    else:
        False

while True:
    if is_Permuted_Multiples(number, 6) == True:
        break
    else:
        number += 1


print(number)
total_time = time.time() - start

print("Done in " + str(total_time) + "s")