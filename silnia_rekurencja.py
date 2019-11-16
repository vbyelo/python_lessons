def silnia(n):
    if n == 0:
        return 1
    else:
        return silnia(n-1) * n

for i in range(5):
    print(f'silnia({i}) = {silnia(i)}')
