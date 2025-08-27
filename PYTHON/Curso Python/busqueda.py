titulo_curso = 'Curso profesional de Python, donde aprenderemos Python'

"""
#.Count nos dice la cantidad de concidencias que hay en el string.
contador = titulo_curso.count('a')

print(contador)
"""
#In nos dira si el valor que le pedimos esta en el string pero solo si en el mismo valor solicitado, solo nos da 'True' o 'False'
#El metodo .lower nos permite estandariza o buscar mayusculas o minusculas.
#Tambien podemos negar si usamos el metodo "not in".
#print('python' in titulo_curso.lower())
# startswith este metodo nos retorna un valor booleano "True-False" si encuentra el String o no al comienzo.
# endswith con este metodo podemos conocer si un String finaliza con lo solicitado.

print(titulo_curso.endswith('Python'))