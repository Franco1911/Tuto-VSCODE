diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print('z' in diccionario)

"""
#Con el metodo de abajo accedemos a las llaves para conocer sus elementos. usamos esto [''].
valor = diccionario['z']
print(valor)
"""

# get nos devuelve el valor de la llave que queremos conocer del diccionario.
# get puede recibir un segundo valor o mensaje en el caso de que la llave no exista.
# get puede contener un valor entero int, flotante float, o boleano true o false. Etc.
#valor = diccionario.get('z', 'la llave no existe en el diccionario')
# setdefault este metodo almacena un valor en el diccionario. Si no existe lo almacena en el diccionario.
valor = diccionario.setdefault('e', 5)

print(valor)
print(diccionario)