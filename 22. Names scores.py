import time

start = time.time()

with open('addons/p022_names.txt') as f:
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

def total_name_score(name_list):
	name_scores = []
	for x in name_list:
		score = (alphabetical_value(x) * (name_list.index(x) + 1))
		name_scores.append(score)
	return sum(name_scores)

print(total_name_score(a))

total_time = time.time() - start

print("Done in " + str(total_time) + "s")