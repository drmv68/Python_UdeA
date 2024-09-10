import words
import random
import time

def printIntro(archivo):
    with open (archivo,"r") as intro:
        t=intro.read()
        print(t)

def rule(rules):
    while rules == "y" or rules== "n" or (rules != "y" and "n"):
        rules = rules.lower()
        if rules == "y":
            return True
        elif rules == "n": 
            print("")
            print("El ahorcado (también llamado colgado) es un juego para dos o más personas. Un jugador piensa en una palabra, frase u oración y el otro trata de adivinarla según lo que sugiere por letras o dentro de un cierto número de oportunidades. Tendras 8 oportunidades de errar tu letra, si fallas dichas veces el juego acabo.")
            print("")
            return True
        else:
            rules = input("Tu respuesta ingresada no es valida, vuelve a ingresarla para continuar: ")
            
def canti(cant):
    while cant == 1 or cant==2 or (cant != 1 and 2):
        if cant == 1:
            print("El programa encontrara una palabra para que la intentes adivinar")
            print("")
            time.sleep(1.5)
            numPa = len(words.list1)
            numRan = random.randrange(0, numPa)
            
            palabraA = words.list1[numRan]
            
            return palabraA
        
        elif cant >= 2:
            palabraA = input("Ingresa la palabra que quieres que la otra persona encuentre: ")
            return palabraA
        else: 
            cant = input("El numero de participntes es invalido") 
    