def saludar_usiario():
    print("Hola, como estas?")


def sumar(num1, num2):
    resultado = num1 + num2
    print(f"La suma entre {num1} y {num2} es: {resultado}")

def restar(num1, num2):
    resultado = num1 - num2
    print(f"La resta entre {num1} y {num2} es: {resultado}")

def multiplicar(num1, num2):
    resultado = num1 * num2
    print(f"La multiplicacion entre {num1} y {num2} es: {resultado}")

def dividir(num1, num2):
    resultado = num1 / num2
    print(f"La division entre {num1} y {num2} es: {resultado}")

continuar = True

while continuar:
    operacion = input("Qué operación desea ejecutar: ")
    primer_numero = int(input("Por favor ingrese el primer número: "))
    segundo_numero = int(input("Por favor ingrese el segundo número: "))

    if operacion == "sumar":
        sumar(primer_numero,segundo_numero)
    elif operacion == "restar":
        restar(primer_numero,segundo_numero)
    elif operacion == "multiplicar":
        multiplicar(primer_numero,segundo_numero)
    elif operacion == "dividir":
        dividir(primer_numero,segundo_numero)
    else:
        print("Acción invalida, seleccione: sumar, restar, multiplicar o dividir")

    desea_continuar = input("Desea continuar con la operación y/n : ")
    if desea_continuar == "n":
        continuar = False
    elif desea_continuar == "y":
        continuar = True
    else:
        print("selección  no valida")
        break