def self_power_sum(no):
    nos = set()
    for x in range(1, (no + 1)):
        nos.add((x ** x))
    return (sum(nos))

no = str(self_power_sum(1000))
length = len(no)
num = int(no[(length - 10):length])

print(num)