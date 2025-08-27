diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# keys(llaves).
# values(valores).
# items(elementos).
#Este metodo retornara un objeto donde se encuentran todas las llaves del diccionario.
#Me retorna las llaves, no sus valores. Osea a,b,c,d.
llaves = tuple(diccionario.keys())
print(llaves)

#Esto me devuelve los valores que hay en las llaves ej 1,2,3,4.
#Estos se imprimen con sus respectivos valores del diccionario {}.
valores = tuple(diccionario.values())
print(valores)

#Este metodo me devuelve su llave con su respectivo valor.
elementos = tuple(diccionario.items())
print(elementos)