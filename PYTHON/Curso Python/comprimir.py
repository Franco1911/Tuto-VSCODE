#Comprimiremos elementos para generar tuplas.
#Si alguna tupla o lista posee mas elementos que otras, estos seran omitidos. Deben poseer igual cantidad de elementos.
lista = [1, 2, 3, 4, 5, 6, 7]

tupla = (10, 20, 30, 40, 50)

lista_2 = [100, 200, 300, 400, 500, 600, 700]

tupla_2 = (1000, 2000, 3000, 4000, 5000)

#Con este metodo podemos comprimir listas y tuplas con "zip"
resultado = zip(lista, tupla, lista_2, tupla_2) # -> zip
resultado = tuple(resultado)

print(resultado)