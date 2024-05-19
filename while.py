nombre = ""
correo = ""
mensaje = ""

condicion_salida ="CONTINUAR"

while condicion_salida == "CONTINUAR":
    nombre = input("Por favor ingrese nombre: ")
    correo = input("Por favor ingrese correo: ")
    mensaje = input("Por favor ingrese el mensaje a enviar: ")

    print(f"""
        Mensaje enviado a {nombre},

        destinatario: {correo}

        mensaje a enviar: {mensaje}
        """)
    
    condicion_salida = input("En caso de continuar con el programa escriba CONTINUAR:")