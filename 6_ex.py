def degree5(n):
    if n == 1:
        return 0
    elif n % 5 == 0:
        return 1 + degree5(n // 5)
    else:
        return -1

n = int(input('Введите число: '))
print(degree5(n))

