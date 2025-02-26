from colorama import Fore, Back, Style
import random


def maths_room():
    levels = {
        "1": [1, 10],
        "2": [2, 100],
        "3": [3, 1000],
        "4": [4, 10000],
        "5": [55, 424242],
    }

    score = 0
    print(goblin("mwuahahahahahaah.. fresh meat.."))
    print(goblin("Are you ready to challenge the Git Goblin?"))
    print(goblin("I'll give you a chance.. you can choose how difficult you want my little game to be, how doe's that sound?"))
    print(goblin("Just give me a number between 1 and 5, 5 being the hardest.. and well.. i'll do the reset.. hurry now!"))

    level = get_level(levels)
    total_questions = 5

    for i in range(total_questions):
        question = generate_problem(levels, level)
        user_answer = get_user_answer(f"Question {i + 1}: {question}")
        actual_answer = calculate_answer(question)
        if int(user_answer == actual_answer):
            score += 1
    if score >= 3:
        print(goblin("Hmmm.. not bad i guess.. lets see what the Jester as to say about all this.."))
        print(goblin("Well.. what are you waiting for.. get out of here before i change my mind!"))    
    else:
        print(goblin("Oh boy, you're in trouble.. The Jester want's a little word with you.."))
        print(score)

    print("**The Goblin kicks you out..**")
    print("TOTAL SCORE: ", score)
    return score


def get_level(levels):
    level = ""
    while level not in levels.keys():
        level = input(
            Fore.GREEN + "Git Goblin: " + Style.RESET_ALL + "So what is it to be? "
        )

    return level


def generate_problem(levels, level):
    operators = ["%", "*", "+", "//"]
    num1 = str(random.randint(levels[level][0], levels[level][1]))
    num2 = str(random.randint(levels[level][0], levels[level][1]))
    operand = str(random.choice(operators))
    return f"{num1} {operand} {num2}"


def get_user_answer(question):
    while True:
        try:
            user_answer = int(input(f"{question}:  "))
            return user_answer
        except ValueError:
            print("Please enter a valid input")


def calculate_answer(question):
    ans_x, ans_op, ans_y = question.split(" ")
    ans_x = int(ans_x)
    ans_y = int(ans_y)
    match ans_op:
        case "%":
            return ans_x % ans_y
        case "*":
            return ans_x * ans_y
        case "+":
            return ans_x + ans_y
        case "//":
            return ans_x // ans_y

        case _:
            return "No valid operator found"


def goblin(phrase):
    return Fore.GREEN + "Git Goblin: " + Style.RESET_ALL + f"{phrase}"


