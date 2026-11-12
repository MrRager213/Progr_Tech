from models.Building import Building
from contracts.Moveable import Moveable


class MobileHome(Building, Moveable):
    def move(self, x=int, y=int):
        self.x = x
        self.y = y