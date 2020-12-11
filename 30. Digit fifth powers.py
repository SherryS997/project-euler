import time

start = time.time()
sumation = 0
no = 2
no_1 = ''
nos = []
nos_1 = []

while no < 355000:
    no = str(no)
    for x in no:
        nos.append(((int(x)) ** 5))
    if sum(nos) == int(no) and sum(nos) not in nos_1:
        nos_1.append(sum(nos))
    nos = []
    no = int(no)
    no += 1

print(sum(nos_1))
total_time = time.time() - start

print("Done in " + str(total_time) + "s")