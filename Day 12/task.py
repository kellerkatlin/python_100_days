from random import randint

FACIL = 10
DIFICIL = 5


def adivina_el_numero(usuario_adivina, respuesta_actual, turnos):
    """Compara el número que el usuario adivina con el número que el programa ha pensado"""
    if usuario_adivina > respuesta_actual:
        print("Muy alto")
        return turnos - 1
    elif usuario_adivina < respuesta_actual:
        print("Muy bajo")
        return turnos - 1
    else:
        print(f"Correcto, el número es {respuesta_actual}")


def dificultad():
    nivel = input("Elige una dificultad. Escribe 'fácil' o 'difícil': ")
    if nivel == "facil":
       return FACIL
    else:
        return DIFICIL
        
    
def game():
    print("Bienvenido a Adivina el número")
    print("Estoy pensando en un número entre 1 y 100")
    respuesta = randint(1, 100)
    turnos = dificultad()
    adivinar = 0
    while adivinar != respuesta:
        print(f"Tienes {turnos} intentos para adivinar el número")
        
        adivinar = int(input("Adivina el número: "))
        turnos = adivina_el_numero(adivinar, respuesta, turnos)
        if turnos == 0:
            print("Te has quedado sin intentos, has perdido")
            return
        elif adivinar != respuesta:
            print("Intenta de nuevo")
        
        
    
game()