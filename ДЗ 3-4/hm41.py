from hm31 import func


def shift(y, x):
    for i in range(x):
        y = y[-1:] + y[:-1]
    return y


y = func()
x = int(input('Смещение на:'))
print(shift(y, x))


assert shift([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
assert shift([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
assert shift([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
assert shift([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
assert shift([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]
