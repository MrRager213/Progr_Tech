from models.GameObject import GameObject


class Unit(GameObject):
    def __init__(self, id=int, name=str, x=int, y=int, hp=float):
        super().__init__(id, name, x, y)
        self.hp = hp

    def isAlive(self):
        return self.hp > 0

    def getHp(self):
        return self.hp

    def receiveDamage(self, damage=float):
        self.hp = max(0, self.hp - damage)