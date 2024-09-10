# Algoritmo piramidalDeAsteriscos
print('Ingrese un número impar:')
TAMANO = int(input())

if TAMANO % 2 == 0:
    print('El número debe ser impar')
else:
    # Parte superior de la pirámide
    for a in range(1, TAMANO + 1, 2):
        for b in range(1, a + 1):
            print('*', end='')
        print('')

    # Parte inferior de la pirámide
    for a in range(TAMANO - 2, 0, -2):
        for b in range(1, a + 1):
            print('*', end='')
        print('')
