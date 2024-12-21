import random
from Character import Character

class Ninja(Character):
    dodge_chance = 0.2

    def take_damage(self, damage):
        if random.random() < self.dodge_chance:
            return 0
        return super().take_damage(damage)