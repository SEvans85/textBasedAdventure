# DevOps Dungeon
#### Video Demo:  <URL HERE>
#### Description:
My project is named Devops Dungeon. I myself am a DevOps Apprentice almost one year on the job. I was struggling to think of an idea for my final project for CS50P.
I decided to create a text based adventure game, as i thought it would be easy to implement different skills i'd learnt into one project. It also convenient to add more features and 'rooms' as i see fit, meaning its infinitely extensible.
I tried to make the game atleast a little DevOps themed in some parts, just to make it more personal to me.

## Files
+ project.py -> contains the main part of my code and everything else is imported into this file
+ test_project.py -> contains all the tests for my project
  - including calculate_answer from maths_room, which make sures the answer the user is giving to the maths question is correct.
  - including calculate_score, from the not_wordle_room, which ensures that the score is correct based on the amount of guesses the user has left.
+ asciiart.py -> this contains all the ascii art i used for my project to give it some basic graphics. I did NOT design these graphics. Credit goes to https://ascii.co.uk/art
+ hangmanart.py -> this contains my different hangman positions in ASCII that get displayed after each guess in the hangman_room. Credit goes to https://ascii.co.uk/art
+ heros.py contains classes for my Hero and subclasses which inherit from Hero
+ hangman_room.py contains the hangman room where the user has to guess the hidden word in a certain amount of tries before the man is hung.
+ maths_room.py contains my maths room puzzle and all relevent functions
+ not_wordle_room.py contains a puzzle nothing like the famous wordle
+ requirements.txt contains the modules that needed to be installed via 'pip install requirements.txt' to run the program
+ notes.py is a notes file i've used on all the crazy ideas i wanted to implement over time. It also contains just some bugs and things i needed to fix.
+ NOT IN USE
  - final_room.py
  - regex_room.py

## What i learnt
I learn a hell of a lot from doing this project and CS50P in general. Making a project from scratch is a skill in itself. Having full control over the project and its structure gave me freedom, but also led me into some structure problems.
I originally had each 'room' has one function, but i quickly found this made it impossible to create effective tests for. So i ended up splitting each 'room' into its own module and importing them into my main file aka 'final_project.py'
Another problem i had was that new ideas kept coming to me as i was coding, or even when i was out for a walk. This meant the scope of the project just kept growing out of control. I would also bounce between one part of the project and another:
This had its pros and cons, because on one hand i could keep coding in another area when i had struggles with one part of the code. But the downside was i had alot of unfinished bits of code at one point and it made running / testing it troublesome.

## puzzles
### maths_room
User enters a desired level 1 - 5. The program will return maths questions using operators // % * and +, using ints in the range of the level entered by the player. I.E Level 1: 9 + 9, Level 2: 99 % 33 , Level 3: 960 // 20
The user will be asked 5 questions total and at the end of it will receive a score between 1 and 5, based on amount correct answers they entered.

### not_wordle_room
User will be given a random 5 letter word that they are to try and guess, from a list i provided. User enters 5 letter work to try to guess the hidden word.
If any letter in the word they guessed is in the actual hidden word AND it is in the correct place, that letter will be revealed.
If any letter in the word they guessed is in the actual hidden word, but the wrong place, that letter will appear as a ?
If any letter in the word they guessed is not in the actual word, it will appear as an X
User has 5 guesses to find the hidden word


## Running the Project
1. use 'pip install requirements.txt' to install the required modules that i used to create this project.
2. use 'python final_project.py' to run the program.

