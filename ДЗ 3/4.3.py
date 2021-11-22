def func():
    x = input('Введите что - нибудь:')
    y = list()
    while x != '':
        y.append(x)
        x = input('Введите ещё что - нибудь:')
    return y
def f1(y):
    print('\tЭлемент','|', '\tЧастота')
    for a in set(y):
        b = y.count(a)
        print('\t', a, '\t|', '\t', b)
y = func()
f1(y)