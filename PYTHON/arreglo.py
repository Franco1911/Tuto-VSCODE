colors = ["rojo", "azul", "verde","azul"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
person = {"nombre":"franco", "apellido":"toledo", "edad":"33"}
animal = {"nombre":"lobo", "color":"negro", "edad":"5"}
colors[1] = "azula"

#numbers.extend(colors) Sirve para fusionar dos listas.

#numbers.reverse() Invierte el numero o elemnetos de una lista.

#print(person.get("edad"))

#print(colors.pop(2)) Imprime valores fuera de los arreglos, quitandolos del arreglo.

#colors.append("blanco") Agrega un Valor al final de la lista o arreglo.

#colors.insert(1,"blanco") Agrega un valor en la lista y se le asigna un lugar en la lista.

#colors.remove("azul") Elimina un valor a asignar de la lista.

#print(colors.count("azul")) Me indica el numero de valores que hay en una lista.
print(len(colors))
print(len(person))
#Me indica la cantidad de elementos que hay en una lista o diccionario.
for value in colors:
    print(value)

#print(person.pop("apellido")) Quitar un elemento del diccionario.

#person.update({"phone":"1234567"}) Sirve para agregar un dato a el diccionario.
#person.update({"profesion":"docente"})

#person.update(animal) Sirve para fusionar diccionarios, los elementos con valores similares seran reemplazados.

for key, value in person.items():
    print(key,"",value)