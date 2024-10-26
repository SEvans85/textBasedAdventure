import random
from colorama import Fore, Back, Style
from asciiart import jesterart


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


def jenkins_says(phrase):
    return Fore.RED + "Jenkins Jester: " + Style.RESET_ALL + f"{phrase}"
