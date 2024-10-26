import random
from colorama import Fore, Back, Style
from asciiart import jesterart


def jenkins_response(value):
    # WORK NEEDED - ADD IN QUOTES FOR DIFFERENT SCORES, FIX SCORE NUMBER IN ASCII,
    print(jesterart(value))
    response = {
        5: [
            "A perfect 5! Well, I doubt you'll be so lucky next time!",
            "Flawless victory! But don’t get too comfortable.",
            "Hmm… beginner’s luck, perhaps?",
        ],
        4: [
            "Not bad, not bad. But can you keep it up?",
            "Solid effort! You might just be worthy of my time.",
            "4 points? You're getting warmer, I suppose.",
        ],
        3: [
            "Average… distinctly average!",
            "A mere 3? I expected something… more.",
            "Middle of the road, just like I thought!",
        ],
        2: [
            "A meager 2? I almost feel sorry for you… almost.",
            "Is that all? 2 points? Pity.",
            "I've seen better… much better.",
        ],
        1: [
            "A single point? This is laughable!",
            "One lonely point… how sad.",
            "That’s it? Just 1? Pathetic!",
        ],
        0: [
            "That’s just pathetic.",
            "Oh dear, oh dear… not good at all.",
            "Zero points! You must be joking!",
        ],
    }

    print(
        Fore.RED + "Jenkins Jester: " + Style.RESET_ALL + random.choice(response[value])
    )


def jenkins_says(phrase):
    return Fore.RED + "Jenkins Jester: " + Style.RESET_ALL + f"{phrase}"
