def validar(mensaje):
    while True:
        try:
            data = float(input("coloca" + mensaje+": "))
            return data;
        except ValueError:
            print("el dato debe ser un numero entero o decimal")

producto = input("¿Que compraras?")
precio = validar("Coloca el precio de lo que compraras") 
ahorroActual = 0

while precio > ahorroActual:
    mesada = validar("Coloca tu mesada")
    ahorroActual = ahorroActual + mesada
    restante = precio - ahorroActual
    tiempoTotal = precio/mesada
    tiempoActual = ahorroActual/mesada
    tiempoRestante = tiempoTotal - tiempoActual
    print ("actualmente tienes ahorrado: ", ahorroActual)
    print ("el dinero que te falta es $", restante)
    print ("los meses que te faltan para cumplir tu meta son", tiempoRestante )

print ("Felicidades ya llegaste a tu meta ya puedes comprar", producto)

