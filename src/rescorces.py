class Character:
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def __str__(self) -> str:
        return f"name: {self.name}\nhealth: {self.health}\nattack: {self.attack}\narmor: {self.armor} "