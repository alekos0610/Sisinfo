# Leer tres números A, B, C, determinar si todos los valores son o no iguales.
# determinar valor mínimo y valor máximo


# ingresar los números deseados por entrada de teclado
valor_A = int(input("Ingrese el primer valor: "))
valor_B = int(input("Ingrese el segundo valor: "))
valor_C = int(input("Ingrese el tercer valor: "))


# Determinar si son iguales o no
if valor_A == valor_B and valor_B == valor_C:
    print (bool("Los números son iguales: "))
else:
    print (bool("los números son diferentes: "))


# Determinar el valor mínimo
if valor_A <= valor_B and valor_B <= valor_C:
    print("El valor mínimo es: " + str(valor_A))

elif valor_B <= valor_A and valor_A <= valor_C:
    print("El valor mínimo es: " + str(valor_B))

else:
    print("El valor mínimo es: " + str(valor_C))


#determinar el valor máximo
if valor_A >= valor_B and valor_B >= valor_C:
    print("El valor máximo es: " + str(valor_A))

elif valor_B >= valor_A and valor_A >= valor_C:
    print("El valor máximo es B: " + str(valor_B))

else:
    print("El valor máximo es: " + str(valor_C))


# imprimir resultados
print("el valor de A es: " + str(valor_A))
print("el valor de B es: " + str(valor_B))
print("el valor de C es: " + str(valor_C))
print("el programa ha finalizado")
