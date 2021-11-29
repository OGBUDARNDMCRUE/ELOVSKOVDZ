l = [1, 9, 2, 8, 3, 7, 4, 6, 5]
l = sorted(l)
def search(l, x):
    lower = 0
    upper = len(l) - 1
    while lower <= upper:
        center = (lower + upper) // 2
        if l[center] == x:
            return center
        elif l[center] > x:
            upper = center - 1
        elif l[center] < x:
            lower = center + 1
    return None


x = int(input("Что ищем: "))
print(search(l, x))
assert search([], 4) == None
assert search([1, 9, 2, 8, 3, 7, 4, 6, 5], 1) == 0
assert search([1, 9, 2, 8, 3, 7, 4, 6, 5], 0) == None
assert search([1, 9, 2, 8, 3, 7, 4, 6, 5], 4) == 4