nos = []

def factorial(no):
    if no < 2:
        return 1
    else:
        for x in range(1, no):
            no = no * x
        return no

def is_curious(no):
    nos = []
    str_no = str(no)
    for x in str_no:
        x = int(x)
        nos.append(factorial(x))
    if no == sum(nos):
        return True
    else:
        return False

no = 3

while no < 100000:
    if is_curious(no):
        nos.append(no)
    no += 1

print(sum(nos))