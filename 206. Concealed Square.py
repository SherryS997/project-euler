def is_special_form(integer):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ans = []
    if len(str(integer)) == 17:
        for x in range(0, len(str(integer)), 2):
            no = str(integer)[x]
            ans.append(int(no))
        if ans == nums:
            return True
    return False


n = 138902663

while True:
    num = n ** 2
    if is_special_form(num):
        break
    n -= 2

ans = n * 10

print(ans)
