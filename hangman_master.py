import random

# List of words to guess from
WORD_LIST = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

def hangman():
    word_to_guess = random.choice(WORD_LIST)
    word_length = len(word_to_guess)
    display = ['_'] * word_length
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(' '.join(display))
    print("\n")

    while '_' in display and tries > 0:
        guess = input("Guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word_to_guess:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_to_guess)
                indices = [i for i, letter in enumerate(word_as_list) if letter == guess]
                for index in indices:
                    display[index] = guess
        elif len(guess) == word_length and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word_to_guess:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                display = list(guess)
        else:
            print("Not a valid guess.")
        
        print(display_hangman(tries))
        print(' '.join(display))
        print("\n")

    if '_' not in display:
        print("Congratulations, you guessed the word!")
    else:
        print("Sorry, you ran out of tries. The word was " + word_to_guess)

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

if __name__ == "__main__":
    hangman()
