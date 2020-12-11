p = 1000
max_set = set()
max_value = 1

def possible_sides(perimeter):
    sides = []
    for x in range(perimeter):
        for y in range(perimeter):
            if y < x:
                z = perimeter - (x + y)
                if 0 < z <= y:
                    sides.append([x, y, z])
    return sides
    


def is_right_angled(p):
    x, y, z = p[0], p[1], p[2]
    if y**2 + z**2 == x**2:
        return True
    else:
        return False

while p > 0:
    right_set = []
    for x in possible_sides(p):
        if is_right_angled(x):
            right_set.append(x)
            if len(right_set) > len(max_set):
                max_set = right_set
                max_value = p
    right_set = []
    p -= 1

print(max_value, max_set)
