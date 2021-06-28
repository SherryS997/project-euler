def product(List):
    result = 1
    for x in List:
        result = result * x
    return result


for x in range(1, 500):
    for y in range(1, 500):
        for z in range(1, 500):
            if x < y < z and x + y + z == 1000 and x**2 + y**2 == z**2:
                nos = [x, y, z]

print(product(nos))
