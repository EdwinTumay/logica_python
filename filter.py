numbers = [1,2,3,4,5,6,7,8,9,10]

def retornar_par (numero):
    return numero % 2 == 0

lista_pares =list(filter(retornar_par, numbers))
print(lista_pares)


lista_pares2 =list(filter(lambda x:x % 2 == 0, numbers))
print(lista_pares2)

# Ejemplo 2
names = ['Alice', 'Bob','Ana', 'David', 'Amelia', 'Charlie']

def retornar_nombres_a(nombre):
    return nombre[0] == "A"

lista_nombres_a = list(filter(retornar_nombres_a, names))
print(lista_nombres_a)

lista_nombres_a2 = list(filter(lambda x : x[0] == "A", names ))
print(lista_nombres_a2)
