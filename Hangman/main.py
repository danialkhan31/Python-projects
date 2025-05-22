from words import word_list
from art import stages , logo
import random

lives = 6

print(logo)
choosen_word = random.choice(word_list)
print(choosen_word)   #Hacked

placeholder = ""
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

   
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    display = ""

    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    
    if guess not in choosen_word:
        lives -= 1
        print(f"you guessed {guess}, that's not correct.You lose a life.")
        if lives == 0:
            game_over = True

           
            print(f"It was {choosen_word}\n***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

   
    print(stages[lives])
