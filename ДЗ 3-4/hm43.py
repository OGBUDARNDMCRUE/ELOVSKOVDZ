def func1(x):
    try:
        assert len(x) == len(set(x))
        return True
    except AssertionError:
        return False
b = list()
print('Введите числа:')
f = input()
b.append(f)
while f != '':
    f = input()
    b.append(f)
b.pop()
print(func1(b))
