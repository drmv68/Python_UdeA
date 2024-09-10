# Algoritmo maquinaDispensadora
print('Ingrese el monto a devolver:')
amount = int(input())

coins1000 = amount // 1000
countWhitoutCoins1000 = amount % 1000
coins500 = countWhitoutCoins1000 // 500
coins200 = (countWhitoutCoins1000 % 500) // 200
coins100 = ((countWhitoutCoins1000 % 500) % 200) // 100
coins50 = (((countWhitoutCoins1000 % 500) % 200) % 100) // 50
restOfCoins = (((countWhitoutCoins1000 % 500) % 200) % 100) % 50

print('Monedas de mil:', coins1000)
print('Monedas de Quinientos:', coins500)
print('Monedas de docientos:', coins200)
print('Monedas de cien:', coins100)
print('Monedas de cincuenta:', coins50)

if restOfCoins > 0:
    print('El restante es:', restOfCoins)
else:
    print('Sin restante. (0)')
