import math

num = 9

def binominal_coefficient(n, m):
    factorial = math.factorial
    value = factorial(n) / (factorial(m) * factorial(n-m))
    return int(value)
     
triangle = []
for n in range(num):
    lst = [binominal_coefficient(n, i) for i in range(n+1)]
    triangle.append(lst)

for tr in triangle:
    print(tr)