def search(a, x):
    if len(a) == 0:  
        return 0
    if a[0] == x:  
        return 1
    return search(a[1:], x)  

list = [1, 2, 3, 4, 5]
print(search(list, 3)) 