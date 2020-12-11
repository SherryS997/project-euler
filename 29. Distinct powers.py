no = (int(input("No please = "))) + 1
nos = []
 

for a in range(2, no):
    for b in range(2, no):
        num = a ** b
        if num not in nos:
            nos.append(num)

nos.sort()
print(len(nos))