# Algoritmo resolverEcuacion
print("Ingresa el valor para a:")
a = float(input())
print("Ahora, ingresa el valor para b:")
b = float(input())
print("Finalmente, ingresa el valor para c:")
c = float(input())

discriminante = (b ** 2) - (4 * a * c)

if discriminante > 0:
    x1 = (-b + discriminante ** 0.5)
    x2 = (-b - discriminante ** 0.5)
    print("Las dos posibles respuestas son:", x1, "y", x2)
else:
    x1_real = -b / (2 * a)
    x1_imag = ((4 * a * c - b ** 2) ** 0.5) / (2 * a)
    x2_real = x1_real
    x2_imag = -x1_imag
    print("Las posibles respuestas son:", x1_real, "+", x1_imag, "i y", x2_real, "+", x2_imag, "i")
