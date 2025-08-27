#El ciclo while se utiliza siempre y cuando nosotros no sepamos el numero de interacciones a realizar.
#El ciclo while se apoya de una condicion y cuando se cumpla la condicion no lo sabemos.
numero = 123456789
contador_digitos = 0

while numero >= 1:
    # contador_digitos = contador_digitos + 1
    contador_digitos += 1

    numero = numero / 10
else:
    print(contador_digitos)