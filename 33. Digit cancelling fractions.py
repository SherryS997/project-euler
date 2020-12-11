fractions = []
numerator = 1
denominator = 1

def is_non_trivial_fraction(numerator):
    no = str(numerator)
    denominator = ''
    for x in range(1, 10):
        denominator = no[1] + str(x)
        no1 = int(no)
        no2 = int(denominator)
        common_no = int(no[1])
        if no1 != no2 and no1 < no2:
            for y in range(1,10):
                for z in range(1, 10):
                    if y != common_no and z != common_no:
                        a, b = str(y), str(z)
                        if (no1 / no2) == (y / z) and a in no and b in denominator:
                            return True
    else:
        return False


def non_trivial_fraction(numerator):
    no = str(numerator)
    denominator = ''
    for x in range(1, 10):
        denominator = no[1] + str(x)
        no1 = int(no)
        no2 = int(denominator)
        for y in range(1,10):
            for z in range(1, 10):
                a, b = str(y), str(z)
                if (no1 / no2) == (y / z) and a in no and b in denominator:
                    return no1, no2

for x in range(11, 100):
    if is_non_trivial_fraction(x):
        fractions.append(non_trivial_fraction(x))

for x in fractions:
    numerator *= x[0]
    denominator *= x[1]
answer = int(denominator/numerator)

print(answer)