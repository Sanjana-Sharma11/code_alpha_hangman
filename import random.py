import random

def hangman():
    words = ["python", "hangman", "chatbot", "sanjana", "intelligence"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 7
    guessed_letters = []

    print("Welcome to Hangman!")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            print("Good guess!")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print("Incorrect guess!")
            attempts -= 1  # reduced penalty from 2 to 1 for balance, you can change it back if you prefer

        guessed_letters.append(guess)
        print(f"Attempts left: {attempts}")
        print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print("\nCongratulations, you guessed the word!")
    else:
        print(f"\nOut of attempts! The word was: {word}")

hangman()
