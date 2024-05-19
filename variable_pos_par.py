def sumar(*args):
    return sum(args)

resultado = sumar(2,3,4,5,6,7,8,9)
print(f"El resultado es {resultado}")

def suma(*args):
    resultado = 0
    for element in args:
        resultado += element
    return resultado
    
resultado_1 = suma(2,3,4,5,6,7,8,9)
print(f"El resultado es {resultado_1}")