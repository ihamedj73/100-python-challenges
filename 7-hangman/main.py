import random
from hangman_art import stages, logo2, logo3
from hangman_words import word_list

lives = 6
chosen_word = random.choice(word_list)
print(logo3)

placeholder = ""
for _ in chosen_word:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(
        f"****************************{lives}/6 Lives Left**************************")
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess in correct_letters:
        print(f"You already guessed {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's nt in the word. You lose a life")
        lives -= 1
        if lives == 0:
            game_over = True
            print("*******************************You lose*****************************")

    if "_" not in display:
        game_over = True
        print("*******************************You Win*****************************")

    print(stages[lives])


print(logo2)
