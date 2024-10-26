
# Hero class with shared attributes
class Hero:
    def __init__(self,name, special):
        if not name:
            raise ValueError("Please enter a name")
        self.name = name
        self.special = special
        self.level = 1
        self._backpack = {}

    def __str__(self):
        return f"I am a hero, my name is {self.name}"

    def special_move(self):
        return f"{self.name} unleashes their special move! \n\t~~-->>{self.special}<<--~~"

    def backpack(self):
        ...

#Mage inherits from Hero, with added functionality
class Mage(Hero):
    def __init__(self, name, special):
        super().__init__(name, special)

    def taunt(self):
        return f"{self.name} stands tall, throwing magic missles in all directions."


#Warrior inherits from Hero, with added functioality
class Warrior(Hero):
    def __init__(self, name, special):
        super().__init__(name, special)
