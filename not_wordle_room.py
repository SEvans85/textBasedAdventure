import random
from colorama import Fore, Back, Style

# ideas -> play again feature, right colours for X ? and letters


def not_wordle_room():
    word_to_guess, guesses = wordle_setup()

    print("WORD TO GUESS: ", word_to_guess)
    print(yeti("Give me a 5 letter word and we will see if you have any matches with my secret word!"))
    print(yeti("If the letter is in the correct place you will be able to see it"))
    print(yeti("If the letter is in the word but in the wrong place, you will see a ?"))
    print(yeti("If the letter does not exist in the word, you will see a +"))
    while guesses < 5:
        guess = input("\n>> ").lower()
        word = guess_word(guess, word_to_guess)
        print("*********************\n")
        print(f"\t{word.upper()}\n")
        print("*********************\n")
        if guess == word_to_guess:
            print(yeti("Well.. its about time.. "))
            score = calculate_score(guesses)
            return int(score)
        guesses += 1
        print(yeti(f"You guessed {guess}. You have {5 - guesses} guesses left. "))
    return calculate_score(guesses)


def calculate_score(guesses):
    print("GUESSES TAKEN: ", guesses + 1)
    scores = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0}
    print("**The YETI throws you across the room and through the open door..**")
    print("TOTAL SCORE: ", scores[guesses])
    return scores[guesses]


def guess_word(word, word_to_guess):
    if len(word) != 5:
        print(yeti("Please enter a 5 letter word. YOU LOSE AGO FOR YOUR SILLY MISTAKE."))
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
    print(yeti("Welcome to the NOT Wordle game. "))
    guesses = 0
    return (word_to_guess, guesses)


def get_word():
    words = [
        "build",
        "fetch",
        "scale",
        "chain",
        "cache",
        "clone",
        "logon",
        "merge",
    ]
    return random.choice(words)


def yeti(phrase):
    return Fore.YELLOW + "YAML Yeti: " + Style.RESET_ALL + f"{phrase}"
