mi_tupla = (1, False, "Edwin", 0.125)

print(type(mi_tupla))

def retornar_estudiante():
    return 'Edwin', 28, 8.6

tupla_estudiante = retornar_estudiante()
nombre_estudiante = tupla_estudiante[0]
edad_estudiante = tupla_estudiante[1]
promedio_estudiante = tupla_estudiante[2]

#pero eso se puede mejorar con 

nombre_estudiante, edad_estudiante, promedio_estudiante = tupla_estudiante()
# el orden de las variables en las que quiere que sea desempaquetado los valores


# one-line swapping
variable_1 = 1.0
variable_2 = 2.0
    # queremos cambiar el valor de las variables 
variable_temp = variable_1
variable_1 = variable_2
variable_2 = variable_temp
print(variable_1, variable_2)

    # mejor respuesta con tuplas
variable_1, variable_2 = variable_2, variable_1