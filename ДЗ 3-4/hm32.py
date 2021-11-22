def seasons(x):
    if x in [1, 2, 12]:
        return 'Это зима!'
    elif 3 <= x <= 5:
        return 'Это весна!'
    elif 6 <= x <= 8:
        return 'Это лето!'
    elif 9 <= x <= 11:
        return 'Это осень!'
    else:
        return 'Такого месяца нет!'

x = int(input('Введите месяц:'))
print(seasons(x))
