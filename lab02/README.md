
# Лабораторная работа №2

## Реализация иерархии классов на Python

**Дисциплина:** Технологии программирования

**Студент:** Тодд Роман Ричардович
**Группа:** БИВТ-25-4-6
**Университет:** НИТУ МИСИС, Москва
**Год:** 2026

## Цель работы

Изучить принципы объектно-ориентированного программирования на языке Python и освоить создание классов, наследование, множественное наследование и использование абстрактных классов.

## Задание

Реализовать иерархию классов для пошаговой компьютерной стратегии.

Необходимо создать базовый класс `GameObject`, классы `Unit` и `Building`, а также классы `Archer`, `Fort` и `MobileHome`.

Дополнительно необходимо реализовать интерфейсы `Attacker` и `Moveable`, определяющие возможности атаки и перемещения игровых объектов.

## Ход работы

### 1. Создание базового класса GameObject

Был создан базовый класс `GameObject`, от которого наследуются все игровые объекты.

Класс содержит следующие атрибуты:

- `id` — идентификатор объекта, тип `int`;
- `name` — название объекта, тип `str`;
- `x` — координата по оси X, тип `int`;
- `y` — координата по оси Y, тип `int`.

Для получения значений атрибутов реализованы методы `getId()`, `getName()`, `getX()` и `getY()`.

### 2. Создание интерфейсов Attacker и Moveable

Для определения возможностей игровых объектов были созданы два абстрактных класса.

`Attacker` определяет метод `attack(unit)`, который принимает объект класса `Unit` и позволяет атаковать другой игровой юнит.

`Moveable` определяет метод `move(x, y)`, который принимает две координаты типа `int` и позволяет изменять положение объекта.

Для реализации абстрактных классов использовался модуль `abc` и декоратор `@abstractmethod`.

### 3. Создание класса Unit

Класс `Unit` наследуется от `GameObject` и описывает игровые подразделения.

Дополнительно он содержит атрибут `hp` типа `float`, отвечающий за количество здоровья.

В классе реализованы следующие методы:

- `isAlive()` — проверяет, жив ли юнит, возвращает `bool`;
- `getHp()` — возвращает количество здоровья типа `float`;
- `receiveDamage(damage)` — принимает урон типа `float` и уменьшает здоровье юнита.

### 4. Создание класса Archer

Класс `Archer` наследуется от `Unit` и реализует интерфейсы `Attacker` и `Moveable`.

Реализованы методы:

- `attack(unit)` — принимает объект класса `Unit` и наносит ему 10 единиц урона;
- `move(x, y)` — принимает координаты типа `int` и изменяет положение лучника.

### 5. Создание класса Building

Класс `Building` наследуется от `GameObject` и описывает игровые постройки.

Дополнительно содержит атрибут `built` типа `bool`, который определяет, завершено ли строительство.

Метод `isBuilt()` возвращает значение типа `bool`.

### 6. Создание классов Fort и MobileHome

Класс `Fort` наследуется от `Building` и реализует интерфейс `Attacker`. Метод `attack(unit)` принимает объект класса `Unit` и наносит ему 25 единиц урона.

Класс `MobileHome` наследуется от `Building` и реализует интерфейс `Moveable`. Метод `move(x, y)` принимает координаты типа `int` и изменяет положение постройки.

### 7. Типы входных и выходных данных

В программе используются следующие типы данных:

| Переменная или параметр | Тип данных | Назначение |
|---|---|---|
| `id` | `int` | Идентификатор объекта |
| `name` | `str` | Название объекта |
| `x` | `int` | Координата по оси X |
| `y` | `int` | Координата по оси Y |
| `hp` | `float` | Здоровье юнита |
| `damage` | `float` | Получаемый урон |
| `built` | `bool` | Состояние постройки |
| `unit` | `Unit` | Объект юнита, передаваемый для атаки |

Основные выходные данные методов:

- `getId()` — `int`;
- `getName()` — `str`;
- `getX()` и `getY()` — `int`;
- `isAlive()` — `bool`;
- `getHp()` — `float`;
- `isBuilt()` — `bool`;
- `attack()` и `move()` — `None`.

Таким образом, программа использует целочисленные значения, строки, числа с плавающей точкой, логические значения и объекты созданных классов.

### 8. Проверка работы программы

Для проверки были созданы объекты классов `Archer`, `Fort` и `MobileHome`.

Была проверена работа методов атаки, получения урона и перемещения объектов.

## Листинг программы

```python
from abc import ABC, abstractmethod


class GameObject:
    def __init__(self, id, name, x, y):
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


class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass


class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass


class Unit(GameObject):
    def __init__(self, id, name, x, y, hp):
        super().__init__(id, name, x, y)
        self.hp = hp

    def isAlive(self):
        return self.hp > 0

    def getHp(self):
        return self.hp

    def receiveDamage(self, damage):
        self.hp = max(0, self.hp - damage)


class Archer(Unit, Attacker, Moveable):
    def attack(self, unit):
        unit.receiveDamage(10)

    def move(self, x, y):
        self.x = x
        self.y = y


class Building(GameObject):
    def __init__(self, id, name, x, y, built):
        super().__init__(id, name, x, y)
        self.built = built

    def isBuilt(self):
        return self.built


class Fort(Building, Attacker):
    def attack(self, unit):
        unit.receiveDamage(25)


class MobileHome(Building, Moveable):
    def move(self, x, y):
        self.x = x
        self.y = y


archer = Archer(1, "Archer", 5, 10, 100)
fort = Fort(2, "Fort", 3, 4, True)
house = MobileHome(3, "MobileHome", 7, 8, True)

fort.attack(archer)
print("Здоровье лучника:", archer.getHp())

archer.attack(archer)
print("Здоровье лучника после атаки:", archer.getHp())

house.move(10, 15)
print("Координаты дома:", house.getX(), house.getY())
```

## Результат работы

В ходе лабораторной работы:

1. Создан базовый класс `GameObject`.
2. Реализованы классы `Unit` и `Building`.
3. Созданы абстрактные классы `Attacker` и `Moveable`.
4. Реализованы классы `Archer`, `Fort` и `MobileHome`.
5. Использовано обычное и множественное наследование.
6. Реализованы методы атаки, получения урона и перемещения.
7. Рассмотрены типы входных и выходных данных методов.
8. Проверена работа созданных классов и их методов.

**В результате лабораторной работы освоены основные принципы объектно-ориентированного программирования на языке Python и реализована иерархия игровых объектов.**
