from tipofuego import TipoFuego

class Charmander(TipoFuego):

    def __init__(self, nombre, nivel, salud, color, temperatura_max):
            super().__init__(nombre = nombre, 
                             nivel = nivel, 
                             salud = salud, 
                             color = color,
                             temperatura_max = temperatura_max)
            
if __name__ == '__main__':
    charmander_1 = Charmander('Chori', 500, 100, 'Naranja', 1000)
    print(charmander_1.nivel)
    charmander_1.atacar()