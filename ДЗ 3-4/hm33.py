def fibon(x):
    a = 1
    b = 1
    print(a, b, end='')
    for i in range(2, n):
        a, b = b, a + b
        print(b, end='')


n = int(input('Введите количество чисел Фибоначчи:'))
fibon(n)
