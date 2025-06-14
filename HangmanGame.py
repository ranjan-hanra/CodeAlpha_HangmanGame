import random

def hangman():
    words = ["python", "java", "ruby", "swift", "html"]
    chosen_word = random.choice(words).lower()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    # Initialize the display word with underscores
    display_word = ["_"] * len(chosen_word)

    print("Welcome to Hangman!")
    # Added line to inform the user about the word category
    print("Hint: The words are programming languages/technologies.")
    print(" ".join(display_word))

    while incorrect_guesses < max_incorrect_guesses and "_" in display_word:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display_word[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        print(" ".join(display_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:")
        print("".join(display_word))
        print("You win!")
    else:
        print("\nGame over! You ran out of guesses.")
        print(f"The word was: {chosen_word}")
        print("You lose!")

if __name__ == "__main__":
    hangman()