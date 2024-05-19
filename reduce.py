from functools import reduce

numeros = [1,2,3,4,5]

def sumar(num1, num2):
    return num1 + num2

total = reduce(sumar,numeros)
print(total)

#lambda
total2 = reduce(lambda x, y : x + y,numeros)
print(total2)