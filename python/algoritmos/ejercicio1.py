# Creación de un programa que permita ingresar un número entero y determine su signo.

print("Determinació de signo de números enteros")

numero = int(input("Ingrese un número: "))

print("El número digitado es: " + str(numero))

if numero < 0:
    print("El signo del número es: " + "-")

else:
    print("El signo del número es: " + "+")



print ("El programa ha finalizado")

