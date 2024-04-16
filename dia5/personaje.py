#creamos el personaje  mediante una clase de objeto
import random
#creamos la clase
class Personaje:
    def __init__(self, nombre, nivel, experiencia):
        self.nombre = nombre
        self.nivel = nivel
        self.experiencia = experiencia
    
    def __str__(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"