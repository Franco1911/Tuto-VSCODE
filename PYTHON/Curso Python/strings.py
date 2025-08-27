"""
lenguajes = 'Python Ruby Java Rust C++ C'

#Con este metodo creamos un listado a partir de strings. 
#El metodo ".split" nos va a generar espacios dentro de el listado.
#Si usamos ".split('-')" esto cambia los giones dentro del string por espacios.
#El metodo ".split('/-/')" nos permite separar caracteres sin importar como esten espaciodos ej /-/, estos son cambiados por espacios
#Tambien es posible tomar solo unos elementos de la lista usanto este metodo ".spli('/-/',3)", tomo los 2 primeros valores del string.
listado_lenguajes = lenguajes.split('') # espacios 

print(listado_lenguajes)
"""

lenguajes = ['Python', 'Ruby', 'Java', 'Rust']
#Utilizando el metodo '-'.join podremos unir caracteres o strings.
string_lenguajes = '-'.join(lenguajes) 

print(string_lenguajes)
#Con esto sabremos a que tipo de caracter pertenece.
print(type(string_lenguajes))