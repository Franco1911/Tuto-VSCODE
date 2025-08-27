#Esta es una forma de descomprimir tuplas.
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#El "*" asterisco denota lsitas
#La forma *resto_valores sirve para los elementos de una tupla que no son desempaquetados.
#Para omitir un valor de una tupla se usa el "_".
uno, _, tres, cuatro, *_, nueve, diez = numeros

print(uno)

print(tres)
print(cuatro)
print(nueve)
print(diez)
#print(resto_valores)