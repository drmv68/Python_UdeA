palabra_frase = input('Ingrese una palabra o frase: ')
letra_ocultar = input('Ingrese una letra para ocultar: ')

# Inicializar una variable para almacenar la versión oculta de la palabra o frase
nuevaPalabra = ''

for caracter in palabra_frase:
    
    if caracter.lower() == letra_ocultar.lower():
        nuevaPalabra += '*'
        
    else:
        nuevaPalabra += caracter

print('Palabra o frase oculta:', nuevaPalabra)
