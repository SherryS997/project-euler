max_no = 1
max_digits = []

for a in range(1, 100):
    for b in range(1, 100):
        digits = []
        no = (a ** b)
        no = str(no)
        for x in no:
            digits.append(int(x))
        sumation = sum(digits)
        if sumation > max_no:
            max_no = sumation

print(max_no)
