import random

# Definición de las opciones
opciones = ['piedra', 'papel', 'tijera']
piedra = '''
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
'''
papel = '''
    _______
---'   ____)____
            ______)
            _______)
              _______)  
---.__________)
'''
tijera = '''
    _______
---'   ____)____
            ______)
        __________)
        (____)
---.__(___)
'''

# Mensaje de victoria
WIN_MESSAGE = "You win!"

# Diccionario para las combinaciones ganadoras
ganadoras = {
    (0, 2): WIN_MESSAGE,
    (1, 0): WIN_MESSAGE,
    (2, 1): WIN_MESSAGE,
}

# Mensaje de bienvenida
print("Welcome to Rock, Paper, Scissors!")

# Elección del usuario
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Elección de la computadora
computer_choice = random.randint(0, 2)

# Mostrar elección del usuario
print(f"You chose:\n{opciones[user_choice]}")

# Mostrar elección de la computadora
print(f"Computer chose:\n{opciones[computer_choice]}")

# Determinar el resultado
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice, computer_choice) in ganadoras:
    print(ganadoras[(user_choice, computer_choice)])
else:
    print("You lose!")