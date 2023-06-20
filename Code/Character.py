class Character:

    def __init__(self, hp, mp, stamina, damage):
        self.hp = hp
        self.mp = mp
        self.stamina = stamina
        self.damage = damage
        self.immunity_time = 0

    def get_hurt(self, damage):
        if self.immunity_time == 0:
            self.hp -= damage
            self.immunity_time = 60