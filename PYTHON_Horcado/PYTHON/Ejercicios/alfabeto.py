palabra = input('Ingrese una palabra: ')
numero = int(input('Ingrese un número entero menor que 26: '))

if 0 <= numero < 26:
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    nueva_palabra = ''

    for letra in palabra:
        if letra.isalpha():
            posicion = alfabeto.index(letra.lower())
            nueva_posicion = (posicion + numero) % 26
            nueva_letra = alfabeto[nueva_posicion]
            if letra.isupper():
                nueva_letra = nueva_letra.upper()
            nueva_palabra += nueva_letra
        else:
            nueva_palabra += letra

    print('Palabra codificada:', nueva_palabra)
else:
    print('El número debe ser un entero entre 0 y 25.')
