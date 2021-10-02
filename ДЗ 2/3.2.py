n = int(input('Введите число:'))
for z in range(n):
    print("*" * (z + 1))
for z in range(n - 1, 0, -1):
    print("*" * z)