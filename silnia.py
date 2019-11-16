def silnia(n):
    if n in (0,1):
        return 1
    else:
        silnia_tmp = 1
        for i in range(2, n+1):
            silnia_tmp *= i
        return silnia_tmp

for i in range(12):
    print(f'silnia({i}) = {silnia(i)}')
