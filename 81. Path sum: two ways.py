import numpy as np

# b = []
#
# with open('addons/p081_matrix.txt') as f:
# 	a = f.read()
#
# a = a.strip().split('\n')
#
# for x in a:
# 	b.append(x.split(','))

y,x = 0,0
b = np.random.randint(1000, size=(200, 200))

print(b)

def shortest_path(b, x = 0, y = 0, d = {}):
	'''
	b must be a 2d array
	'''
	# print(x,y)
	ans = int(b[y][x])
	dest = (len(b) - 1)
	if (x,y) in d:
		return d[(x,y)]
	elif x == dest and y == dest:
		d[(dest, dest)] = ans
		return b[dest][dest]
	else:
		if x < dest and y < dest:
			if (ans + int(shortest_path(b, (x + 1), y, d))) < (ans + int(shortest_path(b, x, (y + 1), d))):
				d[(x,y)] = (ans + int(shortest_path(b, (x + 1), y, d)))
				return (ans + int(shortest_path(b, (x + 1), y, d)))
			else:
				d[(x,y)] = (ans + int(shortest_path(b, x, (y + 1), d)))
				return (ans + int(shortest_path(b, x, (y + 1), d)))
		elif x == dest:
			d[(x,y)] = (ans + int(shortest_path(b, x, (y + 1), d)))
			return (ans + int(shortest_path(b, x, (y + 1), d)))
		else:
			d[(x,y)] = (ans + int(shortest_path(b, (x + 1), y, d)))
			return (ans + int(shortest_path(b, (x + 1), y, d)))

print(shortest_path(b))
