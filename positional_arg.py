def imprimir_nombre(primer_nombre,
                    segundo_nombre,
                    primer_apellido,
                    segundo_apellido):
    
    print(f" Hola {primer_nombre} {segundo_nombre} " \
            f"{primer_apellido} {segundo_apellido} " \
                "bienvenido al curso de Python")
    
#positional Args
imprimir_nombre("Carlos", "Alberto", "Gomez", "Rojas")

#Keyword Args
imprimir_nombre(segundo_apellido="Rojas", primer_nombre="Carlos",
                primer_apellido="Gomez", segundo_nombre="Alberto")

#iterable unpacking
estudiante = ("Carlos", "Alberto", "Gomez", "Rojas")
imprimir_nombre(*estudiante)

#Diccionary unpacking
estudiante_dic = {
    'segundo_apellido':"Rojas", 
    'primer_nombre':"Carlos",
    'primer_apellido':"Gomez",
    'segundo_nombre':"Alberto"
}

imprimir_nombre(**estudiante_dic)