from pokemon import Pokemon

class TipoElectrico(Pokemon):

    def __init__(self, nombre, nivel, salud, color, voltaje_max, amperaje_max):
        super().__init__(nombre = nombre, 
                         nivel = nivel, 
                         salud = salud, 
                         color = color) 
        self.__voltaje_maximo = None
        self.__amperaje_maximo = None

        self.voltaje_maximo = voltaje_max
        self.amperaje_maximo = amperaje_max


    @property
    def voltaje_maximo(self):
        return self.__voltaje_maximo
    
    @voltaje_maximo.setter
    def voltaje_maximo(self, voltaje_max):
        if voltaje_max > 0:
            self.__voltaje_maximo = voltaje_max
        else:
            print("El voltaje no puede ser negativo")


    
    @property
    def amperaje_maximo(self):
        return self.__amperaje_maximo
    
    @amperaje_maximo.setter
    def amperaje_maximo(self, amperaje_max):
        if amperaje_max > 0:
            self.__amperaje_maximo = amperaje_max
        else:
            print("El amperaje no puede ser negativo")

    def atacar(self):
        print(f"Ataca y genera {(self.voltaje_maximo + self.amperaje_maximo)/4} de daño")