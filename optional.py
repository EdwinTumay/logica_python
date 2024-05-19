def calcular_precio(nombre_producto, cantidad, precio_u, descuento=0):
    precio_final = (cantidad * precio_u) * (1-descuento)
    return nombre_producto, cantidad, precio_final

nombre, cantidad, precio = calcular_precio('medias', 3, 10)
print(nombre)
print(cantidad)
print(precio)


