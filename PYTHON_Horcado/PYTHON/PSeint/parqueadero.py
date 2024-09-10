timeOnParking = int(input("Ingrese minutos en parqueadero: "));

if timeOnParking < 1400:
    print("El monto a pagar es: $96.000");
elif timeOnParking < 100 :
    totalPay = int(timeOnParking * 7);
    print("El total a pagar es: ", totalPay);
else:
    costLimit = 700;
    timeOnParking = timeOnParking-100;
    payParkingWhitExtraCost = (timeOnParking*50)+costLimit;
    print("total a pagar es: ", payParkingWhitExtraCost);
