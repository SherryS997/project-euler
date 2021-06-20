import numpy as np

b = []

with open('addons/p081_matrix.txt') as f:
	a = f.read()

a = a.strip().split('\n')

for x in a:
	b.append(x.split(','))

y,x = 0,0
b = np.array(b)

def shortest_path(b, x = 0, y = 0):
	'''
	b must be a 2d array
	'''
	# print(x,y)
	dest = (len(b) - 1)
	if x == dest and y == dest: return b[dest][dest]
	else:
		ans = int(b[y][x])
		if x < dest and y < dest:
			if (ans + int(shortest_path(b, (x + 1), y))) < (ans + int(shortest_path(b, x, (y + 1)))):
				return (ans + int(shortest_path(b, (x + 1), y)))
			else:
				return (ans + int(shortest_path(b, x, (y + 1))))
		elif x == dest:
			return (ans + int(shortest_path(b, x, (y + 1))))
		else:
			return (ans + int(shortest_path(b, (x + 1), y)))

print(shortest_path(b))
