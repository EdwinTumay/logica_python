edad = 10

if edad >= 0 and edad <= 12:
    print("Usted es un niño")
elif edad >= 13 and edad <= 17:
    print("Usted es un adolecente")
elif edad >= 18 and edad <= 59:
    print("Usted es un adulto")
else:
    print("Usted es un adulto mayor")

#If anidados
# Desarrolla un Script que pida la edad y altura del usuario
# Si la persona es mayor de edad puede participar 
# Si la persona no mide 170 podra participar si es mayor a 25 años
# si la altura es mayor a 165

edad = int(input("Ingresa tu edad: "))
altura = int(input("Ingresa tu altura: "))

if edad >= 18:
    if (altura >= 170) or (edad >= 25 and altura >= 165):
        print("Puedes participar en el equipo de baloncesto.")
    else:
        print("No cumples con los requisitos para el equipo de baloncesto.")
else:
    print("Debes ser mayor de edad para participar en el equipo de baloncesto.")


# ejercicio operador ternario
edad = int(input("Ingresa tu edad: "))
mensaje = ""
if edad >= 18:
    mensaje = "Usted es mayor de edad"
else:
    mensaje= "Usted es menor de edad"

print(mensaje)

#operador ternario
mensaje = "Usted es mayor de edad" if edad >= 18 else "Usted es menor de edad"
print(mensaje)
