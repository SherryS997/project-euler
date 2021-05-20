ques = int(input("Enter your num = "))
nums = [ques]
ans = 1

while True:
    test_val = 0
    test = []
    temp_nums= []
    for x in nums:
        if x > 3:
            no = int(x/2)
            temp_nums.append(no)
            temp_nums.append(x - no)
        else:
            temp_nums.append(x)
    nums = temp_nums
    for y in nums:
        if y not in test:
            test.append(y)
            if y > test_val:
                test_val = y
    if len(test) <= 2 and test_val <= 3:
        break

for z in nums:
    ans *= z

print(ans)