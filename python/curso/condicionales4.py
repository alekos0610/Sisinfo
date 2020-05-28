print("MATERIAS OPCIONALES AÑO 2020 ")
print("Informática gráfica - pruebas de software - usabilidad y accesibilidad")
opcion = input("Escribe la asignatura introducida: ")

Asignatura = opcion.lower()

if Asignatura in ("Informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + Asignatura)
else:
    print("la asignatura elegida no está contemplada")



"""
print("PROGRAMA DE BECAS AÑO 2020")
distancia_escuela = int(input("Introduce la distancia a la escuela en kilometros "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce cantidad de hermanos en el centro "))
print(numero_hermanos)

salario_familiar = int(input("introduce salario anual bruto "))
print(salario_familiar)

# declarar los condicionales

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <=20000:
    print("tienes derecho a beca")
else:
    print("no tienes derecho a beca")

print("el programa ha terminado")

"""