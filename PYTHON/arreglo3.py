# Arreglo multidimensional 
"""shoes = [
    ["tenis1","tenis2","tenis3"],
    ["tenis4","tenis5","tenis6"],
    ["tenis7","tenis8","tenis9"]]

print(shoes[2][1])"""

# Arreglo Tipo Diccionario. Un diccionario usa claves ej. Nike, Adidas, Reebok.
"""shoes = [
    {"Nike":"tenis1","Adidas":"tenis2","Reebok":"tenis3"},
    {"Nike":"tenis4","Adidas":"tenis5","Reebok":"tenis6"},
    {"Nike":"tenis7","Adidas":"tenis8","Reebok":"tenis9"}]

print(shoes[2]["Reebok"])"""
# Arreglo Tipo Diccionario Principal.
"""shoes = {
"Nike":["tenis1", "tenis2", "tenis3"],
"Adidas":["tenis4" ,"tenis5" ,"tenis6"],
"Reebok":["tenis7", "tenis8", "tenis9"]}    

print(shoes["Reebok"][1])"""
 #Arreglo de tipo Multidimensional, recorre todos los elementos de un diccionario.
"""shoes = {
"Nike":["tenis1", "tenis2", "tenis3"],
"Adidas":["tenis4" ,"tenis5" ,"tenis6"],
"Reebok":["tenis7", "tenis8", "tenis9"]}    

for key, list in shoes.items():
    for value in list:
        print("Estos son los Tenis disponibles", key, value)"""

#Obtener la posicion de un valor dentro de una lista.
numbers = [1,2,3,4,5,6,7,8,9]

for oposition, value in enumerate (numbers):
    print ("Posicion",position,"",value)
    