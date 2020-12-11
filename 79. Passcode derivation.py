text_file = open('addons/p079_keylog.txt', 'r')
nums = text_file.read().split('\n')
ans = []
answer = '00000000'
total = []

for x in nums:
    for y in x:
        if y not in total:
            total.append(y)


def index_determiner(string):
    identifier = set()
    identifier.add(string)
    for num in nums:
        if string in num:
            for x in num:
                if x != string and num.index(x) > num.index(string):
                    identifier.add(x)
    index = len(total) - len(identifier)
    return index


def string_replacer(string, replacement, index):
    ans = ''
    word = []
    for x in string:
        word.append(x)
    word[index] = replacement
    for x in word:
        ans += x
    return ans


for x in total:
    index = index_determiner(x)
    answer = string_replacer(answer, x, index)

print(answer)
