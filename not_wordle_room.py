import random
from colorama import Fore, Back, Style

# ideas -> play again feature, right colours for X ? and letters


def not_wordle_room():
    word_to_guess, guesses = wordle_setup()

    print(word_to_guess, "WORD TO GUESS")
    while guesses < 5:
        guess = input(
            Fore.YELLOW
            + "YAML Yeti: "
            + Style.RESET_ALL
            + "Give me a 5 letter word and we will see if you have any matches!"
            + "If the letter is in the correct place you will be able to see it"
            + "Ff the letter is in the word but in the wrong place, you will see a ?"
            + "If the letter does not exist in the word, you will see a +"
            + "\n>>"
        ).lower()
        word = guess_word(guess, word_to_guess)
        print("*********************\n")
        print(f"\t{word.upper()}\n")
        print("*********************\n")
        if word == word_to_guess:
            print(
                Fore.YELLOW
                + "YAML Yeti: "
                + Style.RESET_ALL
                + "Well.. its about time.. "
            )
            score = calculate_score(guesses)
            return int(score)

        guesses += 1
        print(
            Fore.YELLOW
            + "YAML Yeti: "
            + Style.RESET_ALL
            + f"You guessed {guess}. You have {5 - guesses} guesses left. "
        )
    return calculate_score(guesses)


def calculate_score(guesses):
    print("GUESSES TAKEN: ", guesses + 1)
    scores = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0}
    print("**The YETI throws you across the room and through the open door..**")
    print("TOTAL SCORE: ", scores[guesses])
    return scores[guesses]


def guess_word(word, word_to_guess):
    if len(word) > 5:
        print(
            Fore.YELLOW
            + "YAML Yeti: "
            + Style.RESET_ALL
            + f"Please enter a 5 letter word. YOU LOSE AGO FOR YOUR SILLY MISTAKE."
        )
        return "+ + + + +"
    word_to_return = ""
    print(word, "guess")
    print(word_to_guess, "word to guess")
    for i, value in enumerate(word):
        if value == word_to_guess[i]:
            word_to_return += value + " "
        elif value in word_to_guess:
            word_to_return += "? "
        else:
            word_to_return += "+ "
    return word_to_return


def wordle_setup():
    word_to_guess = get_word()
    print(
        Fore.YELLOW
        + "YAML Yeti: "
        + Style.RESET_ALL
        + "Welcome to the NOT Wordle game. "
    )
    guesses = 0
    return (word_to_guess, guesses)


def get_word():
    words = [
        "build",
        "deploy",
        "fetch",
        "scale",
        "chain",
        "cache",
        "clone",
        "logon",
        "merge",
    ]
    return random.choice(words)
