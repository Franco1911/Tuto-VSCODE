#Para acceder a los elementos de una lista se debe hacer atraves del orden numerico que tienen a partir de "0".
#Accedemos a ellos atraves del indice 0,1,2,3,4.
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']
#                  0          1        2       3        4     Esta lectura es de derecha a izquierda.
#                 -5         -4       -3      -2       -1     Esto de lee de izquierda a derecha.
primer_curso = lista_cursos[0]
print(primer_curso)

segundo_curso = lista_cursos[1]
print(segundo_curso)

ultimo_curso = lista_cursos[4]
print(ultimo_curso)

#Tambien se puede hacer mediante numeros negativos, solo que se lee de derecha a izquierda.
ultimo_curso = lista_cursos[-1]
print(ultimo_curso)
#Si intentamos acceder a un elemento fuera del listado nos va a marcar error en la consola.