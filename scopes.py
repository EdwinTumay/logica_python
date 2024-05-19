#Scoope global
nombre = "Edwin"

def imprimir_nombre():
    global nombre
    nombre = "Catalina"
    print(f"Hola, como estas {nombre}")

imprimir_nombre()
print(f"El valor de mi variable global es {nombre}")

# Scoope local
def imprimir_nombre_2():
    local = "juan"
    print(f"Hola {nombre}, como estas?")

imprimir_nombre_2()

# Scoope

def imprimir_nombre_3():
    nombre_local = "Edwin"
    edad_local = 30
    print(f"Hola {nombre_local}, como estas?")
    def imprimir_edad():
        nonlocal edad_local
        edad_local = 40
        print(f"su edad es {edad_local}")

    imprimir_edad()
    print(f"la edad es igual a {edad_local}")

imprimir_nombre_3()

