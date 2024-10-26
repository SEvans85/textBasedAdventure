import pytest
from project import build_hero, Hero, Mage, Warrior
from maths_room import get_level, generate_problem, get_user_answer, calculate_answer, maths_room
from not_wordle_room import calculate_score

#check when you run something with certain parameters you get the expected result back
def test_build_warrior():
    name = "scott"
    hero = "warrior"
    special = "Throwing spaghetti at enemies"
    hero = build_hero(name, hero, special)
    assert isinstance(hero, Warrior)
    assert hero.name == name
    assert hero.special == special

def test_build_mage():
    name = "magic man"
    hero = "mage"
    special = "Fires magic missiles in all directions!"
    hero = build_hero(name, hero, special)
    assert isinstance(hero, Mage)
    assert hero.name == name
    assert hero.special == special


def test_calculate_answer():
    assert calculate_answer("8 + 4") == 12
    assert calculate_answer("12 * 4") == 48
    assert calculate_answer("64 // 14") == 4
    assert calculate_answer("120 % 34") == 18

def test_calculate_score():
    assert calculate_score(5) == 0
    assert calculate_score(4) == 1
    assert calculate_score(3) == 2
    assert calculate_score(2) == 3
    assert calculate_score(1) == 4

