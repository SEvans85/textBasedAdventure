import requests
import random
from hangmanart import hang_1, hang_2, hang_3, hang_4, hang_5, hang_6
from pyfiglet import Figlet
from colorama import Fore, Back, Style
import time

#let user choose kind of word they want
#ascii hangman after each guess
#print chosen topic in figlet

def hangman_room():
    guesses = 0
    word = input(Fore.BLUE + "Terraform Titan: " + Style.RESET_ALL + "Ohh there you are... I hear you like DevOps? Whats your favourite tool? ")
    print(Fore.BLUE + "Terraform Titan: " + Style.RESET_ALL + "I see.. welcome to.. *drum roll please*.. ")
    # time.sleep(2)
    print(title(word))
    hidden_word, masked_word = get_word(word)


def guess_letter(hidden_word):
    while not guess.isalpha():
        guess = input("What letter do you choose? ")
    if guess in hidden_word:
        return True
    else:
        return False

    # if yes return masked word with _E__ instead of _____
    # if no return what was passed in


def get_word(word):
    words = []
    response = requests.get(f"https://api.datamuse.com/words?ml={word}")
    o = response.json()
    for result in o:
        if result["word"].isalpha():
            if 6 < len(result["word"]) < 14 and len(words) < 8:
                words.append(result["word"])
    hidden_word = random.choice(words)
    return (hidden_word, len(hidden_word) * "_")



def draw_man(guesses):
    function = f"hang_{guesses}"
    print(globals()[function]())


def title(word):
    figlet = Figlet()
    figlet.setFont(font="chunky")
    return figlet.renderText(f"{word} hangman")
