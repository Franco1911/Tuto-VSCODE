#Generar nuevos strings a partir de otros.
nombre = 'Eduardo Ismael'
apellido = 'García'

#Con este metodo generamos un string a partir de otro usando la variable nombre + apellido. Esto +''+ genera espacios en el string final.
# nombre_completo = 'Mr.' +  nombre + ' ' + apellido + '.'

#Este es otro metodo para generar strings a partir de otros. Los "%s" son reemplazados por los valores que se indiquen en ()
# nombre_completo = 'Mr. %s %s %s.' %(nombre, apellido, 'Pérez')

"""
#los {} seran reemplazados por los valores que se indiquen.
#El orden varia segun los strings base.
#Usando el metodo .format() podemos generar un nuevo string a partir de diferentes string y de un string base. Asignamos valores segun su posicion.
nombre_completo = 'Mr. {nombre} {primer_apellido} {segundo_apellido}.'.format(
    nombre=nombre,
    primer_apellido=apellido,
    segundo_apellido='Pérez'
)
"""
#Al poner la "f" le indicamos a python que se trata de un fstring
#En este metodo se pueden almacenar enteros "int", flotantes "float", "True-False", etc.
nombre_completo = f'Mr. {nombre} {apellido} { 10 * 20 }'

print(nombre_completo)