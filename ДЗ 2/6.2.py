x = []
y = input()
k = int(input())
for i in y:
    if i.isdigit():
        x.append(i) 
print(x[k - 1])