nums = 1
eightynine_set = set()
one_set = set()


def last_num_in_chain(x):
    nos = set()
    num = x
    while True:
        num = str(num)
        no = 0
        for i in num:
            no += (int(i) ** 2)
        num = no
        if num in one_set:
            one_set.update(nos)
            return 1
        elif num in eightynine_set:
            eightynine_set.update(nos)
            return 89
        else:
            if num not in nos:
                nos.add(num)
            else:
                if num == 1:
                    one_set.update(nos)
                else:
                    eightynine_set.update(nos)
                return num


for n in range(1, 10000000):
    if last_num_in_chain(n) == 89:
        nums += 1

print(nums)
