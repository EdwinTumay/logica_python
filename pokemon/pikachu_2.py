from tiopoelectrico import TipoElectrico

class Pikachu(TipoElectrico ):
    __tipo = 'Electrico' # atributo de clase

    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color, longitud_cola): #inicializador variables de instancia  
        super().__init__(nombre = nombre, 
                         nivel = nivel, 
                         salud = salud, 
                         color = color, 
                         voltaje_max = voltaje_max, 
                         amperaje_max = amperaje_max)
        
        self.__longitud_cola = None

        self.longitud_cola = longitud_cola


    @property
    def longitud_cola(self):
        return self.__longitud_cola
    
    #forma setter
    @longitud_cola.setter
    def longitud_cola(self, longitud_cola):
        if longitud_cola > 0:
            self.__longitud_cola = longitud_cola
        else:
            print("La longitud de la cola no puede ser negativa")


    def atacar_cola_hierro(self):
        print(f"Pikachu ataca y genera {self.longitud_cola/0.5}")

# metodo java getters and setters
    def get_salud(self):
        return self._Pokemon__salud
    
    def set_salud(self, salud):
        if salud > 0 and salud < 100:
            self._Pokemon__salud = salud
        else:
            print("La salud no puede ser negativa",
                  "La sauld no puede ser mayor a 100")
            

if __name__ == '__main__':
    pikachu_1 = Pikachu('Pepe',780,100,160,2,'Amarillo', 1)

    # pikachu_1.nivel = 900
    #pikachu_1.set_salud(600)

    # modo python setter
    #pikachu_1.salud = 500

    #print(f"El pikachu llamado {pikachu_1.nombre}, tiene una salud de {pikachu_1.get_salud()}")
    #print(f"El pikachu llamado {pikachu_1.nombre}, tiene una salud de {pikachu_1.salud}")

    pikachu_1.atacar()
    pikachu_1.atacar_cola_hierro()