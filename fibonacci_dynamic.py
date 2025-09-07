# Approch 1 with memoization

# def fib(n):
#     f = [-1 for i in range(n + 1)]
#     f[0] = 0
#     f[1] = 1
#     for i in range(2, n + 1):
#         f[i] = f[i - 1] + f[i - 2]
#     return f[n]

# print(fib(10))

# Approch 2
def fib(n, a, b):
    if(n == 0):
        return a
    if(n == 1):
        return b
    c = a + b
    return fib(n - 1, b, c)

print(fib(10, 0, 1))