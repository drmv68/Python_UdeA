
from utilidades import *
from datetime import datetime

print('menu')

print('1.usuario visitante')
print('2.usuario registrado')
print('3.salir del sistema')
opcion=(input('seleccione una opción: '))
caracter_validos='1','2','3'
    
while not opcion in caracter_validos:
    opcion=(input('ingrese un caracter correcto: '))
if opcion=='1':  
    visitante()
elif opcion=='2': 
    registrado()    
elif opcion=='3':                         
    print('')
        