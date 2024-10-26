from pyfiglet import Figlet
from asciiart import magart, warart, jesterart, manart, map, side_by_side_hero
from maths_room import (
    get_level,
    generate_problem,
    get_user_answer,
    calculate_answer,
    maths_room,
)
from hangman_room import hangman_room, get_word, draw_man
from hangmanart import hang_1, hang_2, hang_3, hang_4, hang_5, hang_6, hang_7
from not_wordle_room import not_wordle_room, get_word, guess_word
from heros import Hero, Mage, Warrior
from colorama import Fore, Back, Style
import random
import time

# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.RESET_ALL) resets all style


def main():
    title = "Devops Dungeon"
    print(game_title(title))
    my_hero = choose_your_destiny()
    my_hero = build_hero(
        name=my_hero["name"], hero=my_hero["hero"], special=my_hero["special"]
    )
    print(my_hero)
    print(my_hero.special_move())
    print(
        Fore.RED
        + "Jenkins Jester: "
        + Style.RESET_ALL
        + "OK Okay! Well roll the dice then, lets see what grusome mystery awaits you!"
    )
    print(
        Fore.RED
        + "Jenkins Jester: "
        + Style.RESET_ALL
        + "Im waiting.. if you're ready to meet your doom just 'roll' the dice."
    )
    roll = ""
    while roll != "roll":
        roll = input(">>")
    print(roll_dice())
    time.sleep(1)
    maths_score = maths_room()
    jenkins_response(maths_score)
    print(
        Fore.RED
        + "Jenkins Jester: "
        + Style.RESET_ALL
        + "Im waiting.. if you're ready to meet your doom just 'roll' the dice."
    )
    roll = ""
    while roll != "roll":
        roll = input(">>")
    print(roll_dice())
    time.sleep(1)

    wordle_score = not_wordle_room()
    jenkins_response(wordle_score)


def roll_dice():
    rooms = {
        1: "maths room",
        2: "not wordle room",
        3: "maths room",
        4: "not wordle room",
        5: "maths room",
        6: "not wordle room",
    }

    die = [1, 2, 3, 4, 5, 6]
    roll = random.choice(die)
    return (
        Fore.RED
        + "Jenkins Jester: "
        + Style.RESET_ALL
        + f"You rolled a {roll}, oh boy you are in trouble! .. \n"
    )


def jenkins_response(value):
    # WORK NEEDED - ADD IN QUOTES FOR DIFFERENT SCORES, FIX SCORE NUMBER IN ASCII,
    print(jesterart(value))
    response = {
        5: [
            "A perfect 5! Well i doubt you will be so lucky next time!",
            "LOL GOOD ONE",
            "NICEEE",
        ],
        4: ["Theres always room for improvement.."],
        3: ["Average.. thats what you are little one.. distinctly average!"],
        2: ["YOU SCORED 2"],
        1: ["YOU SCORED 1"],
        0: ["Thats just pathetic", "Oh dear, oh dear.. not good"],
    }
    # more options needed
    if value > 3:
        print(
            Fore.RED + "Jenkins Jester: " + Style.RESET_ALL + "heHeheHe.. You're good!"
        )
        print(
            Fore.RED
            + "Jenkins Jester: "
            + Style.RESET_ALL
            + random.choice(response[value])
        )
    else:
        print(
            Fore.RED
            + "Jenkins Jester: "
            + Style.RESET_ALL
            + "uhh ohh, you're in trouble!!"
        )
        print(
            Fore.RED
            + "Jenkins Jester: "
            + Style.RESET_ALL
            + random.choice(response[value])
        )


def choose_your_destiny():
    name = ""
    while not name:
        name = input("What is your name young hero? ").strip().title()
        if len(name) > 20:
            raise ValueError(
                "The maximum characters for your hero's name is 20 characters."
            )
        if not all(char.isalpha() or char.isspace() for char in name):
            raise ValueError("Please use only letters and spaces in your hero's name")

    print(f"Welcome {name}.. are you ready for the adventure of a lifetime?")
    side_by_side_hero(warart(), magart())
    hero = ""
    while hero not in ["mage", "warrior"]:
        hero = input(f"Please choose your hero: ").lower().strip()
    print(f"You chose {hero.title()}")
    special = input(f"What is your special skill {name}? ")
    # add this special to class?
    return {"name": name, "hero": hero, "special": special}


def build_hero(name, hero, special):
    match hero:
        case "warrior":
            my_hero = Warrior(name, special)
        case "mage":
            my_hero = Mage(name, special)
        case _:
            return f"Hero not Warrior or Mage"
    return my_hero


def game_title(title):
    print("\n")
    figlet = Figlet()
    figlet.setFont(font="chunky")
    return figlet.renderText(title)


if __name__ == "__main__":
    main()
