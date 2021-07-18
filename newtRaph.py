def newtRaph(num, exp, epsilon):
    '''
    The best algorithm to find roots of any number
    input: number, root, epsilon(to what decimal should the number be.
    output: the root.
    '''
    guess = int(num/2)
    def f(x):
        return x**exp - num
    def f_prime(x):
        return exp*x**(exp - 1)
    guess1 = 0
    while True:
        temp = guess
        guess = guess - f(guess)/f_prime(guess)
        guess1 = temp
        if abs(guess1 - guess) < epsilon:
            break
    return guess
