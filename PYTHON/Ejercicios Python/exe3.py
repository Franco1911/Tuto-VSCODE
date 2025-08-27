horastrabajadas = float(input("Horas Trabajadas?"))

costeporhora  = float(input("Coste por Hora?"))

salario = horastrabajadas * costeporhora

print("Tu sueldo es", salario)

if salario == 180000:
    print("Cobras minimo vital y movil.")
