from hm31 import func


def f1(y):
    print('\tЭлемент', '|', '\tЧастота')
    for a in set(y):
        b = y.count(a)
        print('\t', a, '\t|', '\t', b)
y = func()
f1(y)
