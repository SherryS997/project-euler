def factorial_sum(no):
    sum = 0
    no = str(no)
    for x in no:
        num = 1
        for y in range(1, ((int(x)) + 1)):
            num *= y
        sum += num
    return sum


def chain_len(no):
    chain = set()
    chain.add(no)
    while True:
        num = factorial_sum(no)
        if num not in chain:
            chain.add(num)
        else:
            break
        no = num
    return len(chain)


limit = 1000000 - 1
count = 0

while limit != 0:
    if chain_len(limit) == 60:
        count += 1
    limit -= 1
    print(limit)

print(count)
