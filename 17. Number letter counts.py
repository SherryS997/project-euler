from num2words import num2words
from collections import Counter

n = input("Max No = ")
j = []
k = 'a'

for x in range(1, (int(n) + 1)):
    j.append(num2words(x))

for x in range(len(j)):
    l = j[x]
    if "-" or " " in l:
        f = l.replace("-", "")
        g = f.replace(" ", "")
    k += g

length = len(k) - 1
    
print(k)
print(length)