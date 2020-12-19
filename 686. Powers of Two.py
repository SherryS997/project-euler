import math

def special_power_two(x):
    num = 44
    y = 12710
    while num != x:
        no = 2 ** y
        no = str(10 **(math.log10(math.log10(2)) + math.log10(y)))
        place = int(no.find('.'))
        no = no.replace(no[0:place], '2')
        no = int(10 ** (float(no)))
        if no == 123:
            num += 1
        y += 1
        print(y)
    return y - 1


print(special_power_two(678910))
