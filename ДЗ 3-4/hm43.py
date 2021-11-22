from hm31 import func


def seq(y):
    lst1 = list(set(y))
    if y == lst1:
        return "True"
    else:
        return "False"
y = func()
print(seq(y))
assert seq([1, 2, 2, 4]) == "False"
assert seq([1, 2, 3, 4]) == "True"