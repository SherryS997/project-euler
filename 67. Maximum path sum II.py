import time

start = time.time()

a = ""
b = open("addons/triangle.txt", "r")
c = []
triangle = {}

for line in b:
    a = line.split()
    for x in a:
        c.append(int(x))

for x in range(1,101):
    y = int((x * (x - 1)) / 2)
    triangle[x] = c[y: (y + x)]

def triangle_path(triangle, path_no):
    max_value_no = 0
    max_value = []
    if path_no == 1:
        max_value.append(triangle[path_no][0])
    else:
        for x in range(path_no):
            y = x + 1
            if x == 0:
                if ((triangle[path_no][x]) + (triangle[(path_no - 1)][x])) > max_value_no:
                    max_value.append((triangle[path_no][x]) + (triangle[(path_no - 1)][x]))
                max_value_no = 0
            if (path_no - 1) > x > 0:
                if ((triangle[path_no][x]) + (triangle[(path_no - 1)][x])) > max_value_no:
                    max_value_no = (triangle[path_no][x]) + (triangle[(path_no - 1)][x])
                if ((triangle[path_no][x]) + (triangle[(path_no - 1)][x - 1])) > max_value_no:
                    max_value_no = (triangle[path_no][x]) + (triangle[(path_no - 1)][x - 1])
                max_value.append(max_value_no)
                max_value_no = 0
            if x == (path_no - 1):
                if ((triangle[path_no][x]) + (triangle[(path_no - 1)][x - 1])) > max_value_no:
                    max_value.append((triangle[path_no][x]) + (triangle[(path_no - 1)][x - 1]))
                max_value_no = 0
    return max_value
    max_value = 0

def max_path_sum(triangle):
    max_limit = len(triangle) + 1
    for x in range(2, max_limit):
        triangle[x] = triangle_path(triangle, x)
    b = triangle[len(triangle)]
    print(max(b))

max_path_sum(triangle)

total_time = time.time() - start

print("Done in " + str(total_time) + "s")