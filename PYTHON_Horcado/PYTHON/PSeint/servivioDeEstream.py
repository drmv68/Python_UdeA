# Algoritmo servicioDeStream
print('Ingrese la hora de inicio del servicio (HH:MM:SS): ')
startHours = int(input())
startMinutes = int(input())
startSeconds = int(input())

print('Ingrese la hora de finalización del servicio (HH:MM:SS): ')
finalHours = int(input())
finalMinutes = int(input())
finalSeconds = int(input())

diferenceHours = (finalHours - startHours) * 3600
diferenceMinutes = (finalMinutes - startMinutes) * 60
diferenceSeconds = finalSeconds - startSeconds

totalTimeInSeconds = diferenceHours + diferenceMinutes + diferenceSeconds
totalPay = totalTimeInSeconds * 2

if totalPay > 1000:
    print('------- Total a pagar: $', totalPay, '---------')
else:
    print('---- Total a pagar es: $1000 ----')
