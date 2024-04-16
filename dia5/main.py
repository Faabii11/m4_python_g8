import random
from personaje import Personaje
#metodo constructor del personaje
class Orco:
    def __init__(self, nivel):
        self.nivel = nivel

def batalla(personaje, orco):
    print(f"¡Oh no!, ¡Ha aparecido un Orco!\nNOMBRE: Orco NIVEL: {orco.nivel} EXP: 0")
    while True:
        print(f"\nCon tu nivel actual, tienes {personaje.nivel * 10}% de probabilidades de ganarle al Orco.")
        accion = input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n")
        if accion == '1':
            if random.random() < personaje.nivel * 0.1:
                print("¡Le has ganado al orco, felicidades!")
                print("¡Recibirás 50 puntos de experiencia!")
                personaje.experiencia += 50
                orco.nivel += 1
                break
            else:
                print("¡Oh no! ¡El orco te ha ganado!")
                print("¡Has perdido 30 puntos de experiencia!")
                personaje.experiencia -= 30
                break
        elif accion == '2':
            print("¡Has huido! El orco ha quedado atrás.")
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    # Crear personaje instancias
    nombre_personaje = input("Por favor, indica el nombre de tu personaje: ")
    personaje = Personaje(nombre_personaje, 1, 0)

    # Iniciar batallas y validar 
    while True:
        orco = Orco(personaje.nivel)
        print(f"\n¡Bienvenido a Gran Fantasía!\n{personaje}")
        batalla(personaje, orco)
        print(f"\n{personaje}")
        if personaje.experiencia < 0:
            print("¡Tu personaje ha perdido toda su experiencia y ha sido derrotado!")
            break
        continuar = input("¿Deseas continuar jugando? (si/no): ").lower()
        if continuar != 'si':
            print("¡Gracias por jugar a Gran Fantasía!")
            break