import datetime

class Rickoso:

    def __init__(self, nombre, estado, especie, avatar, ultimaVez, primeraVez, episodios):
        self.nombre = nombre
        self.estado = estado
        self.especie = especie
        self.avatar = avatar
        self.ultimaVez = ultimaVez,
        self.primeraVez = primeraVez,
        self.episodios = episodios


    def to_json(self):
        return {
          "nombre": self.nombre,
          "estado" : self.estado,
          "especie": self.especie,
          "avatar": self.avatar,
          "ultimaVez": self.ultimaVez,
          "primeraVez": self.primeraVez,
          "episodios": self.episodios,
        }
        