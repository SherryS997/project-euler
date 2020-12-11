import fractions


nthans = 0


def squareroottwo(x):
    f1 = fractions.Fraction(2, 1)
    f2 = fractions.Fraction(1, 2)
    f3 = fractions.Fraction(1, 1)
    ans = 1
    while x != 1:
        if ans == 1:
            ans = f1 + f2
            ans = fractions.Fraction(1, ans)
            x -= 1
        else:
            ans = ans + f1
            ans = fractions.Fraction(1, ans)
            x -= 1
    ans = f3 + ans
    x = len(str(ans.numerator))
    y = len(str(ans.denominator))
    if x > y:
        return True
    else:
        return False


for x in range(1, 1001):
    print(squareroottwo(x))
    if squareroottwo(x):
        nthans += 1


print(nthans)
