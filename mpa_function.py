#Funciones de orden superior
lista_nombre = ['maria', 'carlos', 'pepe']

lista_nombre_mayus =list(map(str.upper, lista_nombre))
print(lista_nombre_mayus)

#ejemplo 2
lista_frutas = ['banano', 'per', 'manzana', 'uva']
sufix = '_fruta'

def agregar_sufix(fruta):
    return fruta+sufix

lista_frutas_sufix = list(map(agregar_sufix, lista_frutas))
print(lista_frutas_sufix)

lista_frutas_sufix_2 = list(map(lambda x:x+sufix, lista_frutas))
print(lista_frutas_sufix)


