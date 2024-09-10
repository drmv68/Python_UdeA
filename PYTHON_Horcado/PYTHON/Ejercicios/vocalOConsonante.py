# Solicitar al usuario que ingrese un caracter
caracter = input('Ingrese un carácter (un solo carácter): ')

# Convertir el caracter ingresado a minuscula para simplificar la comparacion
caracter = caracter.lower()

# Verificar si el carácter es una vocal o una consonante
if caracter.isalpha() and len(caracter) == 1:
    if caracter in 'aeiou':
        print('Vocal')
    else:
        print('Consonante')
else:
    print('No es un carácter válido')