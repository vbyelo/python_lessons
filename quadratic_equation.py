# https://www.testdome.com/d/python-interview-questions/9

import math
def find_roots(a,b,c):
    determinant =b**2 -4*a*c
    
    
    #print('determinant',determinant)
    if determinant >0:
        x1 = (-b + math.sqrt(determinant))/(2*a)
        x2 = (-b - math.sqrt(determinant))/(2*a)
        return x1,x2
    elif determinant ==0:
        x1 = -b/(2*a)
        return x1
    else:
        print('nie ma rozwiązań')
print(find_roots(1,2,1))
