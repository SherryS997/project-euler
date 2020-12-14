def smallest_sum_no(num):
    no = '1'
    while True:
        result = 0
        for x in no:
            result += int(x)
        if result == num:
            return int(no)
        no = str(int(no) + 1)

def summation_above(limit):
    result = 0
    for x in range(1, limit + 1):
        result += smallest_sum_no(x)
    return result

prev1 = 0
prev2 = 0
cur = 1
seq = []
no = 1

while no <= 90:
    prev2 = prev1
    prev1 = cur
    cur = cur + prev2
    seq.append(cur)
    no += 1

print(seq)