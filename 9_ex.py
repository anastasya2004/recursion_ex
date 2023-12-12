def combin(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return combin(n-1, k-1) + combin(n-1, k)

n = int(input('Введите число n: '))
k = int(input('Введите число k: '))
print(combin(n, k))

