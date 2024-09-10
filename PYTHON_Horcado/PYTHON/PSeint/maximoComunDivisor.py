# Algoritmo maximoComunDivisor
print('Ingrese el primer número:')
a = int(input())
print('Ingrese el segundo número:')
b = int(input())

for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        mcd = i
        break

print('El máximo común divisor de los números es:', mcd)
