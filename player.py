class Player:
    def __init__(self, name, level=1, exp=0, hp=None, max_hp=None, attack=None, defense=None):
        self.name = name
        self.level = level
        self.exp = exp
        self.max_hp = max_hp if max_hp is not None else 20 + (5 * level)
        self.hp = hp if hp is not None else self.max_hp
        self.attack = attack if attack is not None else 5 * level
        self.defense = defense if defense is not None else 1 + (level / 3)

    def is_alive(self):
        return self.hp > 0

    def heal_full(self):
        self.hp = self.max_hp

    def take_damage(self, amount):
        damage_taken = amount / self.defense
        self.hp -= damage_taken
        return damage_taken
