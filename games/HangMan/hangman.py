import random
from words import words
import string
from hangman_visual import lives_visual_dict


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # get user input
    while len(word_letters) > 0 and lives > 0:
        # print used letters
        print(f'You have {lives} lives left and you have used these letters: ', ' '.join(
            used_letters))
        # what current word is
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # takes away a life
                print("Letter is not in the word.")
                print(lives_visual_dict.get(lives))
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when word letters array is empty
    if lives == 0:
        print(f"You died. The word was {word}")
    else:
        print(f'You guessed the word {word} !!')


if __name__ == '__main__':
    validation = True
    while validation:
        hangman()
        response = input("Do you want to play again? (yes/no) ").upper()
        if response == "NO":
            validation = False
