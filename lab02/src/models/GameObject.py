class GameObject:
    def __init__(self, id=int, name=str, x=int, y=int):
        self.id = id
        self.name = name
        self.x = x
        self.y = y

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getX(self):
        return self.x

    def getY(self):
        return self.y