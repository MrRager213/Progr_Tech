from models.GameObject import GameObject


class Building(GameObject):
    def __init__(self, id=int, name=str, x=int, y=int, built=bool):
        super().__init__(id, name=str, x=int, y=int)
        self.built = built

    def isBuilt(self):
        return self.built