num = 1
Triangle_set = []
Square_set = []
Pentagonal_set = []
Hexagonal_set = []
Heptagonal_set = []
Octagonal_set = []
actual_num = 1

while actual_num < 10000:
    triangular = int(num * (num + 1) / 2)
    actual_num = triangular
    square = num * num
    pentagonal = int(num * ((3 * num) - 1) / 2)
    hexagonal = int(num * ((2 * num) - 1))
    heptagonal = int(num * ((5 * num) - 3) / 2)
    octagonal = int(num * ((3 * num) - 2))
    if triangular < 10000 and triangular > 1000:
        Triangle_set.append(triangular)
    if square < 10000 and square > 1000:
        Square_set.append(square)
    if pentagonal < 10000 and pentagonal > 1000:
        Pentagonal_set.append(pentagonal)
    if hexagonal < 10000 and hexagonal > 1000:
        Hexagonal_set.append(hexagonal)
    if heptagonal < 10000 and heptagonal > 1000:
        Heptagonal_set.append(heptagonal)
    if octagonal < 10000 and octagonal > 1000:
        Octagonal_set.append(octagonal)
    num += 1


def is_cyclical(list):
    front_set = []
    back_set = []
    for x in list:
        front = int(str(x)[0:2])
        back = int(str(x)[2:4])
        front_set.append(front)
        back_set.append(back)
    front_set.sort()
    back_set.sort()
    if front_set == back_set:
        return True
    return False


numbers = {
    1: Triangle_set,
    2: Square_set,
    3: Pentagonal_set,
    4: Hexagonal_set,
    5: Heptagonal_set,
    6: Octagonal_set
}


def is_different_polygonal(list):
    truth_test = set()
    for b in list:
        for a in range(1, 7):
            if b in numbers[a]:
                truth_test.add(a)
                break
    if len(truth_test) == len(list):
        return True
    else:
        return False


required_set = []


print(required_set)
