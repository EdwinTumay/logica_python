lista_numeros = [1,2,3,4]
lista_nombres = ['Edwin', 'Carlos', 'Daniel']
lista_bool = [True, False, True]

print(lista_nombres[2])

lista_numeros[2] = 100
print(lista_numeros[2])

#append
    #agrega elementos a final de la lista
lista_numeros.append(5)
lista_numeros.append(5)
print(lista_numeros)

#count
    #permite contar cuantos elementos con el mismo valor se encuentran en la lista
print(lista_numeros.count(5))

#entend
    #extiende la lista con otra uniendolas
lista_extendida = [101, 102]
lista_numeros.extend(lista_extendida)
print(lista_numeros)

#index
    #me permite buscar un elemento y si existe me lo trae
print(lista_numeros.index(100))

#insert
    # agrega tambien elementos en la posicion que queramos
print(lista_numeros)
lista_numeros.insert(0, 5000)
print(lista_numeros)

#pop
    #extrae los elementos de la lista y retornarlos y lo saca de la lista
print(lista_numeros)
print(lista_numeros.pop())
print(lista_numeros)

#remove
    # elimina elementos de mi lista
print(lista_numeros)
lista_numeros.remove(100)
print(lista_numeros)

#reverse
    #reversa la lista
print(lista_numeros)
lista_numeros.reverse()
print(lista_numeros)

#clear
    #limpia la lista
print(lista_numeros)
lista_numeros.clear()
print(lista_numeros)


#sort
    #organiza las listas
lista_numeros = [5,2,65,3,1,7]
print(lista_numeros)
lista_numeros.sort()
print(lista_numeros)
