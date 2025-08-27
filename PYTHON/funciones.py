#Esta funcion "abs" regresa los numeros en valores positivos.
print(abs(-4/3))

#Esta funcion nos devulve numeros enteros 
print(round(4/3))

#Esta funcion nos devulve el menor de una lista de numeros.
print(min(2,3,4,5,6))

#Esta funcion nos devulve el mayor de una lista de numeros.
print(max(2,3,4,5,6))

#Esta funcion nos permite ordenar una lista de numeros.
numbers = [3,4,5,2,1,6,7,8]
print(sorted(numbers))

#Esta funcion nos permite sumar una lista de numeros.
numbers = [3,4,5,2,1,6,7,8]
print(sum(numbers))

#Siempre investigar las funciones de python.

#Esta funcion se puede aplica a cadenas.
#Devuelve las mayusculas en minusculas.
color = "MORADO"
print(color.lower())

#devulve todo en minusculas.
color = "morado"
print(color.upper())

#Esto sirve para quitar los espacios en un caracter.
color = " morado "
print(color.strip())

#Esto sirve para remplazar un carcter por otro.
color = "morado"
print(color.replace("morado","Rojo"))

#Tambien sirve para reemplazar letras dentro de un caracter.
color = "morado"
print(color.replace("o","i"))

#Este metodo nos refresa una lista de manera que se indique.
color = "Codigo-Facilito"
print(color.split("-"))

#CONCLUSION.
"""Nos rgresa un valor positivo
abs(-4/3)
Regresa un numero entero
round(4/3)
Obtiene el valor mas pequeño 
min(2,3,4,5)
Obtiene el valor mas grande 
max(2,3,4,5)
Sumar los numeros de una lista
sum(numbers)"""
