def retornar_nota(estudiante):
    return estudiante[1]

lista_estudiantes = [('Edwin', 5.0),
                     ('Duvan',3.1),
                     ('Catalina', 4.2),
                     ('Maria', 4.8)]

lista_ordenada = sorted(lista_estudiantes, key=retornar_nota, reverse=True)
print(lista_ordenada)


lista_ordenada2 = sorted(lista_estudiantes, key= lambda x:x[1], reverse=True)
print(lista_ordenada2)