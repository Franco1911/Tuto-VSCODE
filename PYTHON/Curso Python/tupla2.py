cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')
#           0           1       2          3        4

#Para acceder a los elementos dentro de una lista se hace de la misma manera que una lista, se menciona la lista y el orden numerico.
primer_curso = cursos[0]
print(primer_curso)

ultimo_curso = cursos[-1]
print(ultimo_curso)

#sub_tupla = cursos[0:3]
#Esta forma es lo mismo que la de arriba.[start:end].
sub_tupla = cursos[:3]
#Con esta forma accede a todos los elementos dentro de la tupla.
#sub_tupla = cursos[:]
print(sub_tupla)