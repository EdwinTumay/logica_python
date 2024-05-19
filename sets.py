#Declaracion

mi_set = {1,2,3,4}
print(mi_set)

mi_set2 = set()
mi_set2.add(1)
mi_set2.add(2)
mi_set2.add(3)
mi_set2.add(4)

print(mi_set2)

#no permiten datos duplicados

lista_numeros = [1,1,3,4,6,6,1,7]
mi_set3 = set(lista_numeros)
print(mi_set3)

pertenece = 10 in mi_set3
print(pertenece)


# frozenSet

frutas = {'manzana',
          'banano',
          'pera',
          'uva'}


mi_frozenset = frozenset(frutas)
print(mi_frozenset)
