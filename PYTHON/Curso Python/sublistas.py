lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']
#                  0          1        2       3        4     Esta lectura es de derecha a izquierda.
#                 -5         -4       -3      -2       -1     Esto de lee de izquierda a derecha.
#Esto crea una nueva lista a partir de otras listas, este arreglo inlcuye el 0,1,2 y no el 3.
#Nunca se imprime el ultimo elemento que se menciona en el arreglo [start:end]
#[start:end] Esta es la forma en que obtenemos elementos dentro de una lista.
#[start:] -> Obtenemos los ultimos elementos de la lista.
#[:end] -> Obtenemos los primeros elementos de la lista.
#[start:end:skip] De esta forma obtenemos elementos con saltos en las listas.
#[::-1] De esta forma podemos invertir una lista.
sub_lista = lista_cursos[0:3:2]
print(sub_lista)