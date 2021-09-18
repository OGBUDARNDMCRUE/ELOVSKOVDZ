x = int(input('Введите x:'))
y = int(input('Введите y:'))
if x>0 and y>0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
elif x == 0 or y == 0:
    print('Точка лежит на оси')
