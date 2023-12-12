def pownum(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * pownum(a, n-1)
    else:
        return 1 / pownum(a, -n)

a = int(input('Напишите число: '))
n = int(input('Напишите в какую степень возвести число: '))
print(pownum(a, n))
