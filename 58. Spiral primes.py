spiral_corners = []
prime_spiral_corners = []
checker = 100
ratio = 10
constant = 1
num = 1


def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


while checker >= ratio:
    if len(spiral_corners) != 0 and len(spiral_corners) % 4 == 0:
        constant += 1
    num += constant * 2
    if is_prime(num):
        prime_spiral_corners.append(num)
    spiral_corners.append(num)
    checker = (len(prime_spiral_corners) / len(spiral_corners)) * 100
    print(checker)

ans = (2 * constant) - 1

print(ans)
