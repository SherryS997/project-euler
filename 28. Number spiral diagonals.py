def g(n):
    s = (n-1) // 2
    return (16*s*s*s + 30*s*s + 26*s + 3) // 3

print(g(1001))