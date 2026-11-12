from models.Unit import Unit
from contracts.Moveable import Moveable
from contracts.Attacker import Attacker


class Archer(Unit, Attacker, Moveable):
    def attack(self, unit):
        unit.receiveDamage(10)

    def move(self, x=int, y=int):
        self.x = x
        self.y = y