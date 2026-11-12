from models.Building import Building
from contracts.Attacker import Attacker


class Fort(Building, Attacker):
    def attack(self, unit):
        unit.receiveDamage(25)