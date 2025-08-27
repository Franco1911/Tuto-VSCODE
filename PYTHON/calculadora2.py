largo= float (input ("Coloca el largo en metros:"))
ancho= float (input ("Coloca el ancho en metros:"))
m2Xcaja= float (input ("Coloca los metros cuadrados por caja:"))
precioXm2= float (input ("coloca el precio por metro cuadrado:"))     
precioXcaja= (m2Xcaja * precioXm2)
m2Cuarto= largo * ancho
cajas= m2Cuarto/m2Xcaja
precioTotal= cajas * precioXcaja
print("Total de cajas que se necesitan:", cajas)
print("Precio total:", precioTotal)