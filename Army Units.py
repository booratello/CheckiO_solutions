"""
You are the developer of the new strategy game and you need to add the soldier creation process to it.
Let's start with the 2 types - AsianArmy and EuropeanArmy (each of them will be a subclass of the Army - class with the
methods for the creation of soldiers).
Also there will be 3 types of soldiers in the game - Swordsman, Lancer, and Archer (also the classes).
Each army has unique names for those 3 types.
For the EuropeanArmy there are: Knight (for Swordsman), Raubritter (for Lancer), and Ranger (for Archer).
For the AsianArmy: Samurai (for Swordsman), Ronin (for Lancer), and Shinobi (for Archer).
Each army can create all 3 types of the soldiers using the next methods:

train_swordsman (name) - create an instance of the Swordsman.
train_lancer (name) - create an instance of the Lancer.
train_archer (name) - create an instance of the Archer.

All 3 classes (Swordsman, Lancer, and Archer) should have the introduce() method, which returns the string that
describes the soldiers in the following format:
"'type' 'name', 'army type' 'specialization(basic class)'", for example:
"Raubritter Harold, European lancer"
"Shinobi Kirigae, Asian archer"

In this mission you should use the Abstract Factory design pattern.
"""

from abc import ABC, abstractmethod


class Army(ABC):
    @classmethod
    @abstractmethod
    def army_name(cls):
        pass

    @abstractmethod
    def train_swordsman(self, name):
        pass

    @abstractmethod
    def train_lancer(self, name):
        pass

    @abstractmethod
    def train_archer(self, name):
        pass


class EuropeanArmy(Army):

    @classmethod
    def army_name(cls):
        return 'European'

    def train_swordsman(self, name):
        return Knight(name, self.army_name())

    def train_lancer(self, name):
        return Raubritter(name, self.army_name())

    def train_archer(self, name):
        return Ranger(name, self.army_name())


class AsianArmy(Army):

    @classmethod
    def army_name(cls):
        return 'Asian'

    def train_swordsman(self, name):
        return Samurai(name, self.army_name())

    def train_lancer(self, name):
        return Ronin(name, self.army_name())

    def train_archer(self, name):
        return Shinobi(name, self.army_name())


class Soldier:
    def __init__(self, name, army, specialization):
        self.name = name
        self._army = army
        self._specialization = specialization

    def introduce(self):
        return f'{self.__class__.__name__} {self.name}, {self._army} {self._specialization}'


class Swordsman(Soldier):
    def __init__(self, name, army):
        super().__init__(name, army, specialization='swordsman')


class Lancer(Soldier):
    def __init__(self, name, army):
        super().__init__(name, army, specialization='lancer')


class Archer(Soldier):
    def __init__(self, name, army):
        super().__init__(name, army, specialization='archer')


class Knight(Swordsman):
    pass


class Raubritter(Lancer):
    pass


class Ranger(Archer):
    pass


class Samurai(Swordsman):
    pass


class Ronin(Lancer):
    pass


class Shinobi(Archer):
    pass


my_army = EuropeanArmy()
enemy_army = AsianArmy()

soldier_1 = my_army.train_swordsman("Jaks")
soldier_2 = my_army.train_lancer("Harold")
soldier_3 = my_army.train_archer("Robin")

soldier_4 = enemy_army.train_swordsman("Kishimoto")
soldier_5 = enemy_army.train_lancer("Ayabusa")
soldier_6 = enemy_army.train_archer("Kirigae")

print(soldier_1.introduce())
print(soldier_2.introduce())
print(soldier_3.introduce())
print(soldier_4.introduce())
print(soldier_5.introduce())
print(soldier_6.introduce())

assert soldier_1.introduce() == "Knight Jaks, European swordsman"
assert soldier_2.introduce() == "Raubritter Harold, European lancer"
assert soldier_3.introduce() == "Ranger Robin, European archer"

assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"
