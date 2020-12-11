import fractions


def hcfnaive(a, b):
    if(b == 0):
        return a
    else:
        return hcfnaive(b, a % b)


smallest_fraction = fractions.Fraction(0, 1)
num = 1000000


while num != 0:
    no = int(((3 * num) - 1) / 7)
    number = fractions.Fraction(no, num)
    x = hcfnaive(no, num)
    if x == 1 and number > smallest_fraction:
        smallest_fraction = number
        y = no
    else:
        num -= 1

print(y)
