import random
def deal_card():
    """ Retorna una carta aleatoria de la baraja """
    cards = [11, 1, 2,3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ Calcula el puntaje de las cartas """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """ Compara los puntajes de usuario y computadora """
    if user_score == computer_score:
        return "Empate"
    elif computer_score == 0:
        return "Perdiste, la computadora tiene un Blackjack"
    elif user_score == 0:
        return "Ganaste con un Blackjack"
    elif user_score > 21:
        return "Perdiste, tienes más de 21 😠"
    elif computer_score > 21:
        return "Ganaste, la computadora tiene más de 21"
    elif user_score > computer_score:
        return "Ganaste"
    else:
        return "Perdiste 😠"

def play_game():
    """ Juego de Blackjack """
    print("Bienvenido a Blackjack")
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Tus cartas son: {user_cards}, puntaje: {user_score}")
        print(f" Cartas de la computadora: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Desea tomar otra carta? (y/n): ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f" Tus cartas son: {user_cards}, puntaje: {user_score}")
    print(f" Cartas de la computadora: {computer_cards}, puntaje: {computer_score}")
    print(compare(user_score, computer_score))

while input("Desea jugar de nuevo? (y/n): ") == "y":
    print("\n" * 20)
    play_game()