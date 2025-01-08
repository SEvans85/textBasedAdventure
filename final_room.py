# NOT IN USE
from colorama import Fore, Back, Style

def final_room():
    print("Welcome to the Final Boss!")
    print(mrdevops_says("Wow.. you finally made it"))
    print(mrdevops_says("Good Luck!"))
    #Dictionary Questions, with keys being Subjects, Values being a dictionary with Questions, Answers and Outputs.
    questions = {
        "Python": [
            {
                "easy_q": "Declare a variable 'x' with the string 'Hello, World!'",
                "easy_a": "x = 'Hello, World!'",
                "easy_output": "I hope you got this correct, the answer is 'x = \'Hello, World!\'"
            },
            {
                "med_q": "True or False: You can handle exceptions in Python using try and catch blocks.",
                "med_ans": "False",
                "med_output": "The answer is False, In Python we use try and except blocks"
            },
            {
                "hard"
            }
        ],
        "DevOps": [
            {
                "easy_q": ""

            },
            {
                "medium_q": ""
            },
            {
                "hard_q": "",
                "hard_a": "",
                "hard_output": ""
            }
        ],
        "Final": [
            {
                "hard_q": "What is DevOps?",
                "hard_a": "42",
                "hard_output": "The Answer to the Ultimate Question of Life, The Universe, and Everything.. is 42"
            }
        ]
    }
    

def mrdevops_says(phrase):
    return Fore.BLUE + "Mr DevOps: " + Style.RESET_ALL + f"{phrase}"