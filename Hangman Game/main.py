import random
import hangman_art
import hangman_words

print(hangman_art.logo)

list_length = len(hangman_words.word_list)
random_index = random.randint(0, list_length - 1)
chosen_word = hangman_words.word_list[random_index]
lives = 6

display = ['_ '] * len(chosen_word)
game = True
guess_list = []
while game:

    guess = input("Guess a letter: ").lower()
    found = False
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            found = True

    if guess in guess_list:
        print(f"You have already guessed {guess}.")
        found = True
    else:
        guess_list.append(guess)

    if not found:
        lives -= 1
        print(f"You guessed {guess}, that\'s not in the word. You lose a life.")
        if lives < 1:
            print('You lose!')
            print(f"The correct word is {chosen_word}")
            game = False

    if not '_ ' in display:
        game = False
        print("You win!")

    print(f"{''.join(display)}")
    print(hangman_art.stages[lives])
