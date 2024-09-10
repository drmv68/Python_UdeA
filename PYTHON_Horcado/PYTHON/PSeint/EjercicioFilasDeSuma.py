# Algoritmo EjercicioFilasDeSuma
print('Ingrese un número impar:')
N = int(input())

for fila in range(1, (N + 1) // 2 + 1):
    for cont in range(1, N * 2 + 1):
        if cont <= N - (fila - 1) * 2:
            print('+', end='')
        else:
            if cont <= ((N - (fila - 1) * 2) + 4 * (fila - 1)):
                print(' ', end='')
            else:
                print('+', end='')
    print('')
