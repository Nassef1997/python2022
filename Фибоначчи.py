l = int(input('Введите число'))
def primenumb(m):
    for i in range(2, m):
        if m % i == 0:
            return 0
    return 1
def search_prime(z):
    while z >= 2:
        if primenumb(z) == 1:
            return z
        else:
          z -= 1
def Fib(f1, f2):
    print(f1, f2, '', end='')
    for i in range(1, 14):
        F = f1 + f2
        f1 = f2
        f2 = F
        print(f2, '', end='')
T1 = search_prime(l - 1)
T2 = search_prime(l)
Fib(T1, T2)
