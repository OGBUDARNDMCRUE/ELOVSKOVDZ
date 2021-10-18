x = []
y = input('Введите что-нибудь:')
k = int(input('Введите порядковый номер числа:'))
for i in y:
    if i.isdigit():
        x.append(i) 
print(x[k - 1])