from Character import Character
class Tank(Character):
    def take_damage(self, damage):
        damage1 = damage - self.defense
        self.health = max(self.health - damage, 0)
        return damage1