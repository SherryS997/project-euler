nos = set()

def decimalToBinary(n): 
    return int(bin(n).replace("0b",""))

def is_palindrome(no):
    num1 = ''
    num2 = ''
    num = str(no)
    length = len(num)
    if length % 2 == 0:
        num1 = num[0:(length // 2)]
        num2 = num[((length // 2)): length]
        num2 = num2[::-1]
        if num1 == num2:
            return True
        else:
            return False
    else:
        num1 = num[0:(length // 2)]
        num2 = num[((length // 2) + 1): length]
        num2 = num2[::-1]
        if num1 == num2:
            return True
        else:
            return False

for x in range(1, 1000000):
    if is_palindrome(x) and is_palindrome(decimalToBinary(x)):
        nos.add(x)

print(sum(nos))