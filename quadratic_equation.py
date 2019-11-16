# https://www.testdome.com/d/python-interview-questions/9

import math
def find_roots(*args):
    print('typ parametrów', type(args), 'wartosci', args)

    if len(args) == 3: 
        a, b, c = args
    elif len(args) > 3:
        a, b, c, *_ = args
    else:
        print('Wrong argument number')
        return 

    print(f'coefficients a={a}, b={b}, c={c}')
    
    determinant =b**2 -4*a*c
    if determinant >0:
        x1 = (-b + math.sqrt(determinant))/(2*a)
        x2 = (-b - math.sqrt(determinant))/(2*a)
        return x1,x2
    elif determinant ==0:
        x1 = -b/(2*a)
        return x1
    else:
        return 'nie ma rozwiązań'


print(find_roots(1, 2, 1))
