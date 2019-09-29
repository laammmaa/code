def recursion(n, p):
    if (p == 0):
        return 1
    else:
        return n * recursion(n, p - 1)


print(recursion(5, 3))
print(recursion(4, 2))

num = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
result = list(filter(lambda x: (x > 0), num))
print(result)
