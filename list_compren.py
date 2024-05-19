lista = [ 1,2,3,4,5]

# Ciclo normal
cuadrado = []
for x in lista:
    cuadrado.append(x**2)

#List comprehension
cuadrados = [x**2 for x in lista]
print(cuadrados)

cuadrados = [x**2 for x in lista if x % 2 == 0]
print(cuadrados)

# List comprehension anidado
matrix = []
for _ in range(3):
    lista_interna = []
    for i in range(1,4):
        lista_interna.append(i)
    matrix.append(lista_interna)

print(matrix)

matrix = [[i for i in range(1,4)] for _ in range(3)]
print(matrix)

#Dictionary comprehension
lista = [1,2,3,4,5]

cuadrados_dict = {}
for x in lista:
    cuadrados_dict[x] = x**2

print(cuadrados_dict)

cuadrados_dict = { x : x**2 for x in lista}
print(cuadrados_dict)

# Set comprehension
lista = [1,2,3,4,5]

cuadrados_set = set()
for x in lista:
    cuadrados_set.add(x**2)

print(cuadrados_set)

cuadrados_set = {x**2 for x in lista}
print(cuadrados_set)
