# Evaluar peso estatura y sexo

#Solicitar entradas de teclado para las variables
print("ENCUESTA DE SELECCIÓN DE MODELOS")

nombre = input("por favor ingrese su nombre: ")
print("bienvenid@, " + nombre)

print("SELECCIONE SU SEXO SEGÚN LA LISTA")
print("M - para Masculino")
print("F - Para femenino")
opcion = input("Ingresar su selección: ")

print("Por favor ingrese su peso en Kilogramos")
print("ejemplo: 50")
masa = (int(input("por favor ingrese su masa corporal: ")))

print("Por favor ingrese su estatura en metros")
print("ejemplo: 1,50")
talla = float(input("estatura: "))

sexo = opcion.lower()

# Determinar si la persona es apta para ser seleccionada

if sexo == "M" and talla >= 1.79 and masa <= 75:
    print("Ha sido seleccionado")
    
elif sexo == "F" and talla >= 1.75 and masa <= 68:
    print("Ha sido seleccionado")

else:
    print("No ha sido seleccionado")

print("El programa ha finalizado")