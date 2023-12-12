def count(n):
    if n < 10:
        return 1
    else:
        return 1 + count(n // 10)

n = int(input('Введите число: '))
print("Количество цифр в числе - ", count(n))
