triangle=[]
num=6
triangle.append([1])
print(triangle)
for i in range (num):
    temp = triangle[-1]
    print('temp', temp)
    lst = [1]
    for i in range(1, len(temp)):
        lst.append(temp[i]+ temp[i-1])
    lst.append(1)
    triangle.append(lst)
for tr in triangle:
    print(tr)