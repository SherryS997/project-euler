limit = int(input("The sum of amicable nos upto which no = "))
prime_nos = set()

def eratosthenes(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            prime_nos.add(i)
            for j in range(i*i, n+1, i):
                multiples.add(j)

def divisors_sum(no):
    divisors = []
    for x in range(1, no):
        if no % x == 0:
            divisors.append(x)
    return sum(divisors)

def amicable_nos(limit):
    eratosthenes((limit * 2))
    regular_list =set()
    proposed_list = []
    amicable_nos_list = []
    for x in range(1, (limit * 2)):
        y = divisors_sum(x)
        if y not in prime_nos:
            regular_list.add(y)
    for x in regular_list:
        if x < limit:
            if x != 1:
                proposed_list.append(x)
    for y in proposed_list:
        if divisors_sum(y) != y:
            z = divisors_sum(y)
            if z != 1:
                if divisors_sum(z) != z:
                    x = divisors_sum(z)
                    if x != 1:
                        if x == y and x not in amicable_nos_list:
                            amicable_nos_list.append(x)
                            if y not in amicable_nos_list:
                                amicable_nos_list.append(y)
    return amicable_nos_list

print(sum(amicable_nos(limit)))

# print(divisors_sum(40))