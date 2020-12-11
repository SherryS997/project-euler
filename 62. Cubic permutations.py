def cubic_permutations(num):
    cube_set = []
    cubic_permutations = set()
    cubic_permutations.add(num)
    cube = num ** 3
    for x in str(cube):
        cube_set.append((int(x)))
    cube_set.sort()
    checker_set = []
    while len(checker_set) <= len(cube_set):
        checker_set = []
        num += 1
        cube_new_num = num ** 3
        for x in str(cube_new_num):
            checker_set.append((int(x)))
        checker_set.sort()
        if checker_set == cube_set:
            cubic_permutations.add(num)
    print(cubic_permutations)
    return len(cubic_permutations)


count = 0
num = 1

while True:
    no = cubic_permutations(num)
    if no > count:
        print(num, no)
        count = no
        if count >= 6:
            break
    num += 1

print((num ** 3))
