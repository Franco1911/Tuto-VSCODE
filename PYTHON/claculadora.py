#Mi comentario.
"""Mi comentario 
de varias lineas """
def validar( message ): 
    #While. Se ejecutara varias veces, finalizara cuando se ejecute return.
    while True:
        try:
            #En esta linea pedimos un valor de tipo flotante.
            data = float (input("Coloca" +message))
            #Si el valor es de tipo flotante regresamos el valor.
            return data
        except ValueError:
            #Se imprime un mensaje cuando surge un error en try.
            print ("El dato debe ser entero o decimal")

#Datos de entrada.
largo =validar("el largo en metros: ")
ancho = validar("el ancho en metros: ")
m2Xcaja = validar("los metros cuadrados por caja: ")
precioXm2 = validar("el precio por metro cuadrado: ")
"""Regla de tres 
1m2=$162
1.5=&?"""
precioXcaja = (m2Xcaja * precioXm2)
#Estamos obteniendo los metros cuadrados que tiene el cuarto.
m2Cuarto = largo * ancho 
#Cuantas veces cabe las locetas de la caja en el cuarto.
cajas = m2Cuarto/m2Xcaja
#Obtener el precio a gastar en todas las cajas.
precioTotal = cajas * precioXcaja
print ("Total de cajas que se necesitan: ", cajas) 
print ("Precio total: ", precioTotal)
