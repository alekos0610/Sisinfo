# practica de concatenación de operadores de comparación

salario_presidente=int(input("introduce salario presidente: "))
print("Salarios presidente: " + str(salario_presidente))


salario_director=int(input("introduce salario director: "))
print("Salarios presidente: " + str(salario_director))

salario_jefe_area=int(input("introduce salario jefe de area: "))
print("Salarios presidente: " + str(salario_jefe_area))

salario_administrativo=int(input("introduce salario administrativo: "))
print("Salarios presidente: " + str(salario_administrativo))



if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("todo funciona correctamente")
else:
    print("Algo falla en esta empresa")