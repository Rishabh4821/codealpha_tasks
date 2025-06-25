import random

# Hangman ASCII art for 6 to 0 lives
hangman_stages = [
    '''
     _______
    |       |
    |       O
    |      /|\\
    |      / \\
    |
    =========
    ''',
    '''
     _______
    |       |
    |       O
    |      /|\\
    |      / 
    |
    =========
    ''',
    '''
     _______
    |       |
    |       O
    |      /|\\
    |      
    |
    =========
    ''',
    '''
     _______
    |       |
    |       O
    |      /|
    |      
    |
    =========
    ''',
    '''
     _______
    |       |
    |       O
    |       |
    |      
    |
    =========
    ''',
    '''
     _______
    |       |
    |       O
    |      
    |      
    |
    =========
    ''',
    '''
     _______
    |       |
    |       
    |      
    |      
    |
    =========
    '''
]

word_list = ["Gladiator", "Inception", "Titanic", "Avatar", "Interstellar"]
words = random.choice(word_list).lower() 

display = ['_' for _ in words]
lives = 6
game_over = False
guessed_letters = []

print("Welcome to Hangman!")
print(hangman_stages[6])
print(" ".join(display))

while not game_over:
    guessed_letter = input("GUESS A LETTER: ").lower()

    if not guessed_letter.isalpha() or len(guessed_letter) != 1:
        print("Please enter a single valid letter.")
        continue

    if guessed_letter in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guessed_letter)

    if guessed_letter in words:
        for position in range(len(words)):
            if words[position] == guessed_letter:
                display[position] = guessed_letter
    else:
        lives -= 1
        print("Wrong! Lives left:", lives)

    print(hangman_stages[6 - lives])
    print("Guessed letters:", ", ".join(guessed_letters))
    print(" ".join(display))

    if '_' not in display:
        print("You Win! The word was:", words)
        game_over = True
    elif lives == 0:
        print("You Lose!! The word was:", words)
        game_over = True