a = int(input('Целое число'))
num1 = 0
for r in range(2, a+1):
    if a % r == 0:
     for j in range(2, i):
        if r % j == 0:
            num1 += 1
     if num1 == 0:
         print(r)
