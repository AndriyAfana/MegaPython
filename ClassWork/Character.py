class Character:
    name = ""
    health = 100
    damage = 5
    defense = 0

    def __init__(self, name, health=100, damage=5, defense=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense

    def print_stats(self):
        print(f" -< {self.name} >- ")
        print(f" Здоров`я {self.health} ")
        print(f" Шкода {self.damage} ")
        print(f" Захист {self.defense} ")

    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)
        return damage
    def attack(self, target):
        return target.take_damage(self.damage)