# Ejercicio de creación de tuplas

# se puede crear sin parentesis, pero no se recomienda para evitar errores



mitupla = ("Juan", 13, 1, 1995) # a diferencia de la lista va encerrada en parentesis
nombre, dia, mes, agno = mitupla  #desempaquetado de tupla.

print(nombre)
print(agno)
print(mes)
print(dia)



# milista = list(mitupla) # convertir una tupla en una lista


# Proceso donde se convirtió una lista en una tupla

""" milista = ["juan", 13, 1, 13, 1995]

mitupla = tuple(milista)

print(len(mitupla))"""