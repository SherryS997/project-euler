no = int(input("Factorial no for? = "))
factorial_no = 1
factorial_no_list = []

for x in range(1, (no + 1)):
    factorial_no *= x

factorial_no = str(factorial_no)

for x in range(len(factorial_no)):
    factorial_no_list.append(int(factorial_no[x]))

print(sum(factorial_no_list))