class Player:
    def __init__(self, name, desc, type, hp, armor, damage):
        self.name = name
        self.desc = desc
        self.type = type
        self.hp = hp
        self.armor = armor
        self.damage = damage

    def attack(self, monster):
        monster.hp -= self.damage

    def talk(self):
        return self.desc

    def is_dead(self):
        return self.hp <= 0
