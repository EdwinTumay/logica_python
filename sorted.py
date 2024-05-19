estudiante = [
    ('Juana', 22, 95, '555-1234'),
    ('Pedro', 18, 89, '555-5678'),
    ('Juan', 25, 94, '555-9876')
]
def ordenar_por_edad(estudiante):
    return estudiante[1]

lista_estudiantes_edad = sorted(estudiante, key= ordenar_por_edad)
print(lista_estudiantes_edad)

#ordenado al contrario por edad
lista_estudiantes_edad2 = sorted(estudiante, key= ordenar_por_edad, reverse=True)
print(lista_estudiantes_edad2)

#lambda
lista_estudiantes_edad3 = sorted(estudiante, key= lambda x : x[2])
print(lista_estudiantes_edad3)