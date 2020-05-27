# Practica de if else
# else siempre tiene que estar acompañado de un if correspondiente

print("verificación de notas estudiantiles")

nota_alumno = int(input("Introduce tu nota: "))

if nota_alumno < 5:
    print("Insuficiente")

elif nota_alumno < 6:
    print("suficiente")

elif nota_alumno < 8:
    print("bien")

elif nota_alumno < 9:
    print("Notable")

elif nota_alumno > 10:
    print("No cumple con criterios de notas:")

else:                                                          
    print("sobresaliente")

print("El programa ha finalizado")