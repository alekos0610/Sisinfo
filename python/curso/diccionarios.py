# Practica de creación de diccionarios y trabajo con ellos.

# La sintaxis se compone de: nombre del diccionario y llaves

""" midiccionario = {"Alemania":"Berlín", "Francia":"París", "Reino unido":"Londres", "España":"Madrid"}

# print(midiccionario["España");    se imprime valor de la clave = España

midiccionario["Italia"] = "lisboa"          # Agregar elementos a un diccionario


midiccionario["Italia"] = "Roma"            # Para modificar un elemento hay que volver a escribirlo para cambiar el valor, imprimirá el último ingresado

print(midiccionario)

del midiccionario ["Reino unido"]

print(midiccionario) """

""" midiccionario = {"Alemania":"Berlín", 23:"Jordan", "Mosqueteros": 3}
print(midiccionario)"""

# Pueden asignar claves a cada uno de los valores a través de tuplas

""" mitupla = ["España", "Francia", "Reino unido", "Alemania"]

midiccionario = {mitupla[0]:"Madrid", mitupla[1]:"París", mitupla[2]:"Londres", mitupla[3]:"Berlín"}

print(midiccionario) """


# Guardar una Tupla dentro de un diccionario

"""midiccionario = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}

print(midiccionario["anillos"])"""



# Guardar un diccionario dentro de un diccionario

midiccionario = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}

print(midiccionario.keys())             # Cita las claves
print(midiccionario.values())           # Cita los valores de las claves
print(len(midiccionario))               # Hace un recuento de la cantidad de valores
print(midiccionario)

