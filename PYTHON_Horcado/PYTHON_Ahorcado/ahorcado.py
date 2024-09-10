from fallosMuneco import fallosMuneco
from funciones import printIntro 
import funciones
import time #nos servira para que haya tiempo entre las impresiones de bienvenida


printIntro("intro.txt")

nombre = input("¿Como te llamas? ")

print("¡Hola, " + nombre,"estas apunto de jugar el mitico juego del ahorcado! ")
print("¡Te deseo mucha suerte!")
print(" ")

rules = input("¿Conoces las reglas del juego? (Y/N): ")
rules = rules.lower()

rul = funciones.rule(rules)

otraVez = "y"

while otraVez == "y":
    otraVez = ""
    
    letrasDispo="a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"
    
    letrasUsadas = ""

    #cant = 2
    cant = int(input("¿Cuantas personas Jugaran en esta ronda? 1 / 2: "))
    cant = funciones.canti(cant)

    #palabra = "hola"
    palabra = cant
    print("")
    print("")
    print("")
    print("")
    printIntro("intro.txt") #Inicia la Jugabilidad


    time.sleep(1)
    print("")
    print("Comienza a adivinar")
    time.sleep(0.5)

    palabra = palabra  #aqui va la palabra que queremos que adivinen
    palabraAux=palabra
    tupalabra = "" #aqui se va a ir guardando la palabra que estamos adivinando
    letrasUsAux =""
    
    vidas = 8
    while vidas > 0:
        falloMune = fallosMuneco(vidas)
        letrasUsAux = letrasUsAux + letrasUsadas
        fallas = 0
        for letra in palabra:
            if letra in tupalabra:
                print(letra, end="")
            elif letra == " ":
                    print("  ", end="")
            else:
                print("_ ", end="")
                fallas +=1
                       
                
        if fallas == 0:
            print("")
            print(" !FELICIDADES, HAZ GANADO!")
            print("")
            break
        print("")
        print("Letras Disponibles: ", letrasDispo)
        print("Letras Usadas: ", letrasUsadas)
        print("")
        tuletra=input("Intoduce una letra: ")
        tuletra=tuletra.lower()
        if tuletra in letrasDispo:
            letrasDispo = letrasDispo.replace(tuletra, "")
            letrasUsadas = letrasUsadas + tuletra + " "
            
        tupalabra += tuletra
        
        if tuletra in letrasUsAux:
            print("")
            print("¡CUIDADO! esa letra ya la usaste")
            print("¡Pero tranquilo! aun te quedan ", vidas, "vidas")
            
        #if tuletra not in palabra:
        elif tuletra not in palabra:
            vidas -= 1
            print("")
            print("La letra", tuletra, "lamentablemente no esta en la oracion")
            if vidas!=0:
                print("¡Pero tranquilo!, aun te quedan", vidas, "vidas.")
           
           
            if vidas == 0:
                fallosMune=fallosMuneco(0)
                print("Oh Perdiste")
                print("La palabra era: " , palabraAux.upper())
                print("¡Suerte para la proxima!")
    
    otraVez = str(input("¿Quieres volver a jugar? (Y/N): "))
    otraVez = otraVez.lower()
    
 










