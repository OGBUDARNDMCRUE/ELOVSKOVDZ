x = input('Введите что-нибудь:')
a = list()
while x != '':
    a.append(x)
    x = str(input())
else:
    print(a)   