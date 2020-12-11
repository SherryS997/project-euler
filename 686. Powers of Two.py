def special_power_two(x):
    num = 0
    y = 7
    while num != x:
        no = str(2 ** y)
        no = int(no[0:3])
        if no == 123:
            num += 1
        y += 1
    return y - 1


print(special_power_two(678910))
