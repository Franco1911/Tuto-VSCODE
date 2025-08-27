lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos_2 = ['C', 'C++', 'Docker']
#Me indica el numero de elementos dentro de una lista.
print(len(lista_cursos))
#Este metodo agrega un elemneto al final de la lista.
lista_cursos.append('MongoDB')
lista_cursos.append('C#')
#Se pueden agregar elementos de diferente tipo, pero lo mejor es que sean del mismo tipo.
lista_cursos.append('10')
#"Insert" añade elementos a la lista al asignarle un lugar en la lista por medio de orden numerico.
lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'Pygame')
#".extend" nos permite extender una lista.
lista_cursos.extend(lista_cursos_2)

#Al colocarlo despues de un "append" me dira el numero de la lista mas los elementos agregados.
#print(len(lista_cursos))

print(lista_cursos)
#".remove" nos permite eliminar un elemento de la lista.
lista_cursos.remove('MongoDB')
#"del" elimina elementos de la lista atraves de su orden numerico. Tambien funciona con numeros negativos ej -5.
"""del lista_cursos[-1]"""

#".clear" elimina todos los elementos de una lista.
lista_cursos.clear()

print(lista_cursos)

print(len(lista_cursos))