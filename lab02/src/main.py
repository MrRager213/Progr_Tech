from models.Fort import Fort
from models.Archer import Archer
from models.MobileHome import MobileHome


archer1 = Archer(1, "Лучник", 5, 10, 100)
archer2 = Archer(2, "Лучник", 5, 10, 100)
fort = Fort(3, "Форт", 3, 4, True)
house = MobileHome(4, "Мобильное строение", 7, 8, True)

print("Здоровье первого лучника:", archer1.getHp())

archer2.attack(archer1)
print("Здоровье первого лучника после пропущенной атаки:", archer1.getHp())

house.move(10, 15)
print("Координаты дома:", house.getX(), house.getY())
