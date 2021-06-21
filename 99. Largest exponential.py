from math import *

with open('addons/p099_base_exp.txt') as f:
	a = f.read()

a = a.strip().split('\n')
b = {}

for x in a:
    y = x.split(',')
    b[int(y[0])] = int(y[1])

temp = 0
ans = 0

for a in b.keys():
    if (b[a] * log(a)) > temp:
        temp = b[a] * log(a)
        ans = a

print(ans)
