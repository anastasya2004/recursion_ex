def is_prime(x, divisor=2):
    if x < 2:
        return 0
    if x == 2:
        return 1
    if x % divisor == 0:
        return 0
    if divisor * divisor > x:
        return 1
    return is_prime(x, divisor + 1)

def function1(x):
    return is_prime(x)

# Пример использования функции
print(function1(7))  # Выведет: 1 (так как 7 - простое число)
print(function1(10))  # Выведет: 0 (так как 10 - составное число)
