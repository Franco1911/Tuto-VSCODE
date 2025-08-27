#Caber los valores que el usuario ha ingresado a traves de su teclado.
#Los mensajes a solicitar a el usuario deben de ser los mas decriptivos posibles.
#Imput se encarga de pausar la ejecucion de un programa hasta que se le da "enter" en el teclado.
#la variable input nos permite saber todo lo que el usuario ingrso por teclado hasta que presiona la tecla "enter"
#Inpuy simpre nos retorna un tipo de dato "string"
"""nombre_completo = input('Ingresa tu nombre completo: ')

print(nombre_completo)
print(type(nombre_completo))"""

"""nombre_completo = input('Ingresa tu nombre completo: ')

edad = input('Ingresa tu edad: ')
edad = int(edad) #con esto pasamos un "string" a un "int"

altura = input('Ingresa tu altura: ')
altura = float(altura)#con esto convierto un "string" a "float"

#print(altura)
#print(type(altura))

#Ingresamos un dato de tipo "booleano"
autorizacion = input('¿Autorizas el programa? (si/no)')
autorizacion = autorizacion == 'si'

print(autorizacion)"""

#Lo mismo que lo de arriba pero en menos lineas de codigo.
nombre_completo = input('Ingresa tu nombre completo: ')

edad = int(input('Ingresa tu edad: '))

altura = float(input('Ingresa tu altura: '))


autorizacion = input('¿Autorizas el programa? (si/no)') == 'si'

print(nombre_completo)
print(edad)
print(altura)
print(autorizacion)

