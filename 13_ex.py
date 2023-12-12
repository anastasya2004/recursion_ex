def add_list(a,n):
    if n==0:
        return a
    y = a.pop(0)
    if y % 2 == 0:
        a.append(y)
    return add_list(a,n-1)

x = [1,3,2,5,8,3,110]
add_list(x,len(x))
print(x)

#Если попросят написать рекрсивный алгоритм, где будет 1 параметр - список
'''
def add_ligh(a):
    return add_list(a,len(a))
'''