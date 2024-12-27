# Task: Hangman
import random

word_list = ["aardvark", "baboon", "camel"]
stages = [r'''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
        |
        |
    =========
    ''', r'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
        |
        |
        |
    =========
    ''', r'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        |
        |
        |
    =========
    ''', r'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        |
        |
        |
    =========
    ''', r'''
    +---+
    |   |
    O   |
    |   |
        |
        |
        |
        |
        |
    =========
    ''', r'''
    +---+
    |   |
    O   |
        |
        |
        |
        |
        |
        |
    =========
    ''', r'''
    +---+
    |   |
        |
        |
        |
        |
        |
        |
        |
    =========
    ''']

print( '''
Welcome to Hangman!

             _
            | |
            | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
            | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |   
                            |___/  
      ''')

lives = 6
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for _ in range(word_length):
    placeholder += "_"
    
print(chosen_word)
print(placeholder)


game_over = False
correct_letters = []

while not game_over: 
    
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        continue
    
    
    display = ""
    
    for letter in chosen_word:
        if letter == guess: 
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
            
    print("Word to guess: " +  display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        if lives == 0:
            game_over = True
            print("You lose!")
            print(f"The word was {chosen_word}")
            
    
    if "_" not in display:
        game_over = True
        print("You win!")
    
    print(stages[lives])
        
        
print(display)