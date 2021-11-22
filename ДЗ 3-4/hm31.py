def func():
    x = input('Введите что - нибудь:')
    y = list()
    while x != '':
        y.append(x)
        x = input('Введите ещё что - нибудь:')
    return y

print(func())
