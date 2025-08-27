#Esta funcion sirve para multiplicar los parametros dentro de una funcion.
numbers = [1,2,3,4,5]
update = []
for value in numbers:
    update.append(value*2)
print(update)

def operation(value):
    return value*2
print((list(map(operation,numbers))))

print(list(map((lambda value: value*2),numbers)))