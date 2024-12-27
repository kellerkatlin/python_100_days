print(''' 
                      .---.   .---.
              ,';'   `.';'   `..
              f               :Bo.
              `               d88:
               `\           /d88P'
                 `\     ; /d888P'
                   `.  ',d8&8P'
                     : ;d8&7'
                      | :8:
                         |  qx
      ''')

print('Bienvenido a la Isla de los Tesoros')
print('Tu mision es encontrar el tesoro escondido')
choice1 = input('Eres valiente? Presiona Enter para comenzar? Tipo "left" o "right" para elegir tu camino').lower()

if choice1 == 'left':
    choice2 = input('Has llegado a un lago. Hay una isla en el medio del lago. Tipo "wait" para esperar un bote. Tipo "swim" para nadar')
    if choice2 == 'wait':
        choice3 = input('Has llegado a la isla ileso. Hay una casa con 3 puertas. Tipo "red", "blue" o "yellow" para elegir una puerta')
        if choice3 == 'red':
            print('Felicidades! Encontraste el tesoro')
        elif choice3 == 'blue':
            print('Te comio un dragon. Game Over')
        elif choice3 == 'yellow':
            print('Te comio un leon. Game Over')
        else:
            print('Game Over')
    else:
        print('Te comio un cocodrilo. Game Over')