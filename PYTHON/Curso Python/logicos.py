#operadores logicos.
# and, or y not.

#Al usar el comparador logico (and:verdadero) todas las comparaciones logicas deben de ser verdaderas para que el valor final sea verdadero 
resultado_final = True and True and 100 > 20
print(resultado_final)

#Para que el comparaor logico or sea veradero al menos una de las comparaciones debe de ser verdadera.
#Uno de los valores es verdadero, entonces el resultado final sera verdadero.
resultado_final = False or False or 100 > 20
print(resultado_final)

#Uno de los valores es falso entonces el resultado final sera falso.
resultado_final = False or False or 10 > 20
print(resultado_final)

#Se pueden combinar los operadores logicos con el uso del parentesis. Python resuelve primero lo que hay entre parentesis.
#True and False.
resultado_final = True and (False or 5 > 10)
print(resultado_final)

#True and True.
resultado_final = True and (False or 50 > 10)
print(resultado_final)

#Nos permite negar un valor booleano, convierte false a true y viceversa.
resultado_final = not True
print(resultado_final)
