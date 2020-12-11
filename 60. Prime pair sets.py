import time

start = time.time()
required_list = [1000000000]

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_concatenated_prime(no1, no2):
    num1 = int(str(no1) + str(no2))
    num2 = int(str(no2) + str(no1))
    if is_prime(num1) and is_prime(num2):
        return True
    else:
        return False

def is_remarkable_primes(list):
    for x in range(1, len(list)):
        for y in range(x):
            if not is_concatenated_prime(list[x], list[y]):
                return False
    else:
        return True

def remarkable_primes(prime_no, limit):
    final_list = [10000000000]
    concatenable_primes = [prime_no]
    num = prime_no + 1
    while num < 10000:
        if is_prime(num) and is_concatenated_prime(prime_no, num):
            concatenable_primes.append(num)
        else:
            pass
        num += 1
    count = 1
    if len(concatenable_primes) >= limit:
        while count <= len(concatenable_primes):
            required_list = [prime_no]
            for x in range(count, len(concatenable_primes)):
                required_list.append(concatenable_primes[x])
                if is_remarkable_primes(required_list):
                    pass
                else:
                    required_list.remove(concatenable_primes[x])
            if len(required_list) == limit and sum(required_list) < sum(final_list):
                final_list = required_list
            count += 1
    return final_list

    
count = 2

while count < 20:
    if is_prime(count):
        test_list = remarkable_primes(count, 5)
        if sum(test_list) < sum(required_list):
            required_list = test_list
    count +=1

print(sum(required_list))
total_time = time.time() - start

print("Done in " + str(total_time) + "s")