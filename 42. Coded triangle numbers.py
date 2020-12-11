triangle_words = set()
n = 1
triangle_nos = set()

while n < 200:
    num = (1 / 2) * n * (n + 1)
    triangle_nos.add(num)
    n += 1

with open('addons/p042_words.txt') as f:
	a = f.read()

a = a.strip().split(',')
a = [x[1:-1] for x in a]
a.sort()

def alphabetical_value(name):
	name = name.lower()
	letters = []
	letter_value = []
	alphabets = [
		"a", "b", "c", "d", "e",
		"f", "g", "h", "i", "j",
		"k", "l", "m", "n", "o",
		"p", "q", "r", "s", "t",
		"u", "v", "w", "x", "y", "z"
		]
	for x in name:
		letters.append(x)
	for x in letters:
		if x in alphabets:
			letter_value.append((alphabets.index(x))+ 1)
	return (sum(letter_value))



for x in a:
    if alphabetical_value(x) in triangle_nos:
        triangle_words.add(x)

print(triangle_words, len(triangle_words))