# imports
from random import randint, choice

# global variables


# classes
class Weapon:
    def __init__(self, name, damage) -> None:
        self.name = name
        self.damage = damage

    def get_damage(self):
        return self.damage

# BRYTER MOT STANDARD
GOBLIN_WEPONS = [Weapon("Rusty Clever", 2),
                 Weapon("Rusty spear", 3),
                 Weapon("Stone axe", 1)]


class Character:
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
        self.generare_weapon
        self.attack = self.weapon.get_damage()


    def __str__(self) -> str:
        return f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor} "

    def generare_weapon(self):
        random_weapon = randint(0, 100)
        if random_weapon < 20: self.weapon = Weapon("shortsword")
        elif random_weapon >= 20 and random_weapon < 40: self.weapon = Weapon("Broadsword", 5)
        elif random_weapon >= 40 and random_weapon < 60: self.weapon = Weapon("Small knife", 1)
        elif random_weapon >= 60 and random_weapon < 80: self.weapon = Weapon("Spear", 2)
        elif random_weapon >= 80 and random_weapon < 90: self.weapon = Weapon("Halbeard", 4)
        elif random_weapon >= 90 and random_weapon < 95: self.weapon = Weapon("Morningstar", 6)
        elif random_weapon == 96: self.weapon = Weapon("Ateiseh", 50) 
        elif random_weapon == 97: self.weapon = Weapon("Excalibur", 15)
        elif random_weapon == 98: self.weapon = Weapon("Axe of Drago", 10)
        elif random_weapon == 99: self.weapon = Weapon("Sword of khaine", 20)
        elif random_weapon == 100: self.weapon = Weapon("Frostmourne", 20)
        else: self.weapon = Weapon("Fist", 1)


    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0

        
    def get_attack(self): #tidigare damage
        return self.attack

    def get_health(self):
        return self.health

    def get_name(self):
        return self.name

    def get_attribute(self):
        return self.name, self.health, self.armor


class Goblin:

    def __init__(self, health, armor, id):
        self.health = health
        self.armor = armor
        self.id = id
        self.weapon = choice(GOBLIN_WEPONS)
        self.attack = self.weapon.get_damage()


    def __str__(self):
        return f"Goblin: #{self.id}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor} "


    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_name(self):
        return f"Goblin #{self.id}"


def save_character(chars : list()):
    save_list = []
    for character in chars:
        name, health, armor = character.get_attribute()
        save_string = f"{name}/{health}/{armor}\n"
        save_list.append(save_string)

    with open("saved_characters.txt", "w", encoding="utf8") as f:
        for line in save_list:
            f.write(line)
        print("characters has been saved")

def load_characters():
    characters = []
    with open("saved_characters.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            attributes = line.split("/")
            char = Character(attributes[0],
                             int(attributes[1]),
                             int(attributes[2]))

            characters.append(char)
    return characters

def create_character():
    print("Welcome to the chaacter creater!")
    name = input("What is your characters called?: ")
    health = randint(10, 30)
    attack = randint(3, 5)
    armor = randint(0, 5)

    return_char = Character(name, health, armor)

    print()
    print(return_char)
    print("Character has been created")
    return return_char