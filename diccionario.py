#Declarar
mi_diccionario = {
    'edwin': [1.4, 4.5, 5.0],
    'carla': [4.4, 5.0, 5.0],
    'daniel': [0.4, 3.0, 3.4],
}

#Dict
mi_diccionario_2 = dict(edwin = [1.4, 4.5, 5.0],
                        carla = [4.4, 5.0, 5.0],
                        daniel = [0.4, 3.0, 3.4])

#dict_vacio
mi_diccionario_3 = {}
mi_diccionario_4 = dict()
mi_diccionario_4['edwin'] = [1.4, 4.5, 5.0]
mi_diccionario_4['carla'] = [4.4, 5.0, 5.0]
mi_diccionario_4['daniel'] = [0.4, 3.0, 3.4]

print(mi_diccionario)
print(mi_diccionario_2)
print(mi_diccionario_4)

mi_diccionario['maria'] = [1.4, 4.5, 5.0]
print(mi_diccionario)

print(mi_diccionario['maria'])
mi_diccionario['maria'] = [3.4, 5.0, 5.0]
print(mi_diccionario['maria'])

del mi_diccionario['daniel']
print(mi_diccionario)


#keys
print(mi_diccionario.keys())

#values
print(mi_diccionario.values())

#both
print(mi_diccionario.items())

