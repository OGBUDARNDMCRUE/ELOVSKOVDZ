def arith_mean(x):
    s = sum(x) / len(x)
    print('Среднее арифметическое:', s)
y = input('Введите число:')
x = list()
while y != '':
    x.append(float(y))
    y = input('Введите ещё что - нибудь:')

arith_mean(x)