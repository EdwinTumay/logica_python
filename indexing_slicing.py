cadena = "Hola, mundo!"

print(cadena[0:4]) #toma del 0 al 4 imprime hola
print(cadena[6:11]) #imprime mundo
print(cadena[:4]) #toma del 0 al 4 imprime hola
print(cadena[6:]) #imprime mundo!
print(cadena[:]) #impirime desde el inicio hasta el final
print(cadena[::2]) #impirime desde el inicio hasta el final con saltos de 2 en 2

telefono = "4-5-6-3-2-4-7-9"
print(telefono[::2])
telefono = "-4-5-6-3-2-4-7-9"
print(telefono[1::2])

print(cadena[-6:-1]) # imprime mundo pero de atras para delante
print(cadena[::-1])
