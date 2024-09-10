# Solicitar al usuario una palabra
palabra = input('Ingrese una palabra: ')
palabra_invertida = ''

for i in range(len(palabra) - 1, -1, -1):
    palabra_invertida += palabra[i]

if palabra == palabra_invertida:
    print('La palabra es un palíndromo.')
else:
    print('La palabra no es un palíndromo.')
