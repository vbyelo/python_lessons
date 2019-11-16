# https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(12):
    print(f'fibonacci({i}) = {fibonacci(i)}')
