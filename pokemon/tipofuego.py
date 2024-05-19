from pokemon import Pokemon

class TipoFuego(Pokemon):

    def __init__(self, nombre, nivel, salud, color, temperatura_max):
        super().__init__(nombre = nombre, 
                         nivel = nivel, 
                         salud = salud, 
                         color = color) 
        
        self.__temperatura_maxima = None
        
        self.temperatura_maxima = temperatura_max


    @property
    def temperatura_maxima(self):
        return self.__temperatura_maxima
    
    @temperatura_maxima.setter
    def temperatura_maxima(self, temperatura_max):
        if temperatura_max > 0:
            self.__temperatura_maxima = temperatura_max
        else:
            print("La temperatura no puede ser negativa")

    def atacar(self):
          print(f'Ataque con fuego y genera {self.temperatura_maxima * 0.5} de daño')
