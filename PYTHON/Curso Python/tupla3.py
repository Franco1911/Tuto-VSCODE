#Una variable es de tipo lista si al definirla se usa [].
#Si los elemenetos a almacenar van a cambiar se usa listas.
cursos = ['Python', 'Django', 'Flask']

#Usando esta funcion podemos generar una tupla a partir de ina lista pasar de "[]" a esto "()".
cursos_tupla = tuple(cursos)

print(cursos_tupla)
#Con esta funcion podemos comprabar que la lista ahora es una tupla.
print(type(cursos_tupla))

#Una variable es de tipo tupla si al defiinirla se usa ().
#Si los elemenetos a almacenar queremos que se conserven por el resto del programa se usan tuplas.
niveles = ('Básico', 'Intermedio', 'Avanzado')

#Con esta funcion podemos crear una lista y convertirla en tupla, pasar de "()" a esto "[]"
niveles_lista = list(niveles)

print(niveles_lista)
#Con esto combrobamos que la tupla ahora es una lista.
print(type(niveles_lista))