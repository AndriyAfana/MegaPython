from Character import  Character
class Vampyre(Character):
    lifesteal_percent = 0.1
    def attack(self, target):
        damage_dealt = target.take_damage(self.damage)
        lifesteal = int(damage_dealt * self.lifesteal_percent)
        self.health = min(self.health + lifesteal, 100)
        return damage_dealt