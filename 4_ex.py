def sum_progress(a1, r, n):
    if n == 1:
        return a1
    else:
        return sum_progress(a1, r, n-1) + a1 + (n-1)*r

a1 = int(input('Введите первый член:'))  
r = int(input('Введите разность арифметической пррогрессии:'))
n = int(input('Введите номер члена прогрессии:'))
print(sum_progress(a1, r, n))
