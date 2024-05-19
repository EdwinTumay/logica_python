def conectar_bd(**kwargs):
    nombre = kwargs.get('nombre_bd', 'default')
    user = kwargs['usuario']
    password = kwargs['password']
    port = kwargs['port']
    dir_bd = kwargs['dir_bd']
    print(F"conectando con la base de datos: {nombre}")

conectar_bd(nombre_bd='produccion',
             usuario='root',
               password='12345',
               port='5002',
               dir_bd='10.25.47.3',
               query = "SELECT * FROM tabla")