lista = [8, 5, 90, 1, 5, 44, 132, 600, 3, 4, 5]
#".sort" nos permite ordenar la lista de menor a mayor.
#"reverse=True" ordena la lista de mayor a menor.
"""lista.sort(reverse=True)

print(lista)"""

#lista.sort()

#"0" nos va a mostrar el menor de los numeros.
#print(lista[0])
#"-1" nos va a mostrar el mayor de los numeros.
#print(lista[-1]) 

#Con "min" y "max" conoceremos el numero menor y el mayor, si acceder a las listas por numeros.
#print(min(lista))
#print(max(lista))

#Con esta expresion sabremos si un elemento se encuentra o no en el listado. Respuesta sera True o False.
print(5 in lista)

#Con "not" negamos el valor booleano.
#print(11 not in lista)

#".index" nos permite conocer el indice o lugar en el que se encuentra el elemento.
#Aunque haya mas de un elemento en la lista ".index" siempre nos retornara el primer elemento encontrado.
index = lista.index(5)
print(index)