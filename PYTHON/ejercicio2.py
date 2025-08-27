mensaje = 'hola mundo desde python en su version 3.154540'

contador = 0

for caracter in mensaje:
    if caracter in '12345678890':
        contador+=1 # contador = contador + 1


if contador == 1:
    print('El string solo posee un numero entero.')
elif contador > 1:
    print('El string posee ' + str(contador) + ' numeros enteros.')
else:    
    print('Lo sentimos, el string no posee un numero entero.')
