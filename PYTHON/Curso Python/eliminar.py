diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(len(diccionario))
#Antes de eliminar cualquier elemento de la llave debemos comprobar que existe en el diccionario.
#Con esto eliminamos una llave del diccionario.
del diccionario['a'] # 1
#Este metodo muestra el elemento antes de ser eliminado del diccionario.
valor = diccionario.pop('b') # 2

#Esto elimina todos los elemntos de un diccionario.
diccionario.clear()

print(valor)

print(diccionario)
print(len(diccionario))