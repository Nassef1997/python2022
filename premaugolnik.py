m = int(input('введите значение 1: '))
c = int(input('введите значение 2: '))
print('*' * m)
for i in range (c-2):
    print('*' + ' ' * (c - 2) + '*')
print('*' * m)
