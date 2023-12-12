def mod_number(a, b):
    if a < b:
        return a
    else:
        return mod_number(a - b, b)

a = int(input('Введите число: '))
b = int(input('Введите делитель: '))
print("Остаток от деления - ", mod_number(a, b))
