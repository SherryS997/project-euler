nos = range(100, 1000)
new_nos = range(100, 1000)

new_nos2 = []

for x in nos:
    for y in new_nos:
        new_nos2.append(x * y)

new_nos3 = []

for n in new_nos2:
    temp = n
    rev = 0
    while temp != 0:
	    rev = (rev * 10) + (temp % 10)
	    temp = temp // 10
    if n == rev:
        new_nos3.append(n)

# print(new_nos2)
print(max(new_nos3))