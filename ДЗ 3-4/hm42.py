def factorial(a):
    x = 1
    for i in range(2, a + 1):
        x *= i
    return x


a = int(input('Введите число:'))
print(factorial(a))


assert factorial(5) == 120
assert factorial(6) == 720
