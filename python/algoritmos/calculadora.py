# Hacer una calculadora de operaciones básicas en python

print("CALCULADORA DE OPERACIONES BÁSICAS")
print("Elige una opción de la lista")
print("1-Suma")
print("2-Resta")
print("3-Multiplicación")
print("4-División")

# Pedir un valor para X (lista)
x= input("Escribe tu elección:")   

# Declarar variable Y para que tomé el valor de X
y=float(x)

# opción 1 - Suma
if(y==1):
    a=input("Introduce el primer numero\n")
    b=input("Introduce el segundo numero\n")
    a2=float(a)
    b2=float(b)
    resultado= a2+b2
    print("El resultado de la suma es:",resultado)

# opción 2 - Resta
elif(y==2):
    a=input("Introduce el primer numero\n")
    b=input("Introduce el segundo numero\n")
    a2=float(a)
    b2=float(b)
    resultado= a2-b2
    print("El resultado de la resta es:",resultado)

# opción 3 - Multiplicación
elif(y==3):
    a=input("Introduce el primer numero\n")
    b=input("Introduce el segundo numero\n")
    a2=float(a)
    b2=float(b)
    resultado= a2*b2
    print("El resultado de la multiplicación es:",resultado)

# opción 4 - División
elif(y==4):
    a=input("Introduce el primer numero\n")
    b=input("Introduce el segundo numero\n")
    a2=float(a)
    b2=float(b)
    resultado= a2/b2
    print("El resultado de la división es:",resultado)

else:
    print("El valor seleccionado no es valido")