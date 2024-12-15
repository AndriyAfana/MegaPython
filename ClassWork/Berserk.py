from Character import Character
class Berserk(Character):
    rage_limit = 50
    damage_multiplier = 1.5

    def __init__(self, name, health=100, damage=5, defense=0, damage_multiplier=1.5, rage_limit = 50):
        Character.__init__(self, name, health, damage, defense)
        self.damage_multiplier = damage_multiplier
        self.rage_limit = rage_limit

    def attack(self, target):
        final_damage = self.damage * self.damage_multiplier if self.health < self.rage_limit else self.damage
        return target.take_damage(final_damage)