from math import floor


class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50
        self.defense = 0

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 3
        self.health = 60
        self.defense = 2


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 4
        self.health = 40
        self.vampirism = 50

    def vamp_heal(self, damage):
        hurt = self.__class__().health - self.health
        if hurt > 0:
            vamp_hp = floor(damage * self.vampirism / 100)
            self.health += vamp_hp if hurt > vamp_hp else hurt


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.health = 50
        self.puncture = 50

    def puncturing_attack(self, damage, second_defending):
        second_defending.health -= \
            damage * self.puncture / 100 - second_defending.defense


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 0
        self.health = 60
        self.heal_power = 2

    def heal(self, unit):
        hurt = unit.__class__().health - unit.health
        if hurt > 0:
            unit.health += self.heal_power if hurt > self.heal_power else hurt


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, what_unit, how_many):
        while how_many != 0:
            self.units.append(what_unit())
            how_many -= 1


class Battle:
    @staticmethod
    def fight(army_1, army_2):
        while army_1.units != [] and army_2.units != []:
            attacking_army, defending_army = army_1, army_2

            while True:
                attacking_unit, defending_unit = \
                    attacking_army.units[0], defending_army.units[0]
                damage = attacking_unit.attack - defending_unit.defense if \
                    attacking_unit.attack > defending_unit.defense else 0
                defending_unit.health -= damage

                if attacking_unit.__class__.__name__ == "Vampire":
                    attacking_unit.vamp_heal(damage)

                if attacking_unit.__class__.__name__ == "Lancer" and \
                        len(defending_army.units) > 1 and damage > 0:
                    attacking_unit.puncturing_attack(damage,
                                                     defending_army.units[1])
                    if not defending_army.units[1].is_alive:
                        defending_army.units.pop(1)

                if len(attacking_army.units) > 1 and \
                        attacking_army.units[1].__class__.__name__ == "Healer":
                    attacking_army.units[1].heal(attacking_unit)

                if not defending_unit.is_alive:
                    defending_army.units.pop(0)
                    break
                else:
                    attacking_army, defending_army = \
                        defending_army, attacking_army

        return army_1.units != []


def fight(unit_1, unit_2):
    attacking, defending = unit_1, unit_2
    while True:
        damage = attacking.attack - defending.defense if \
            attacking.attack > defending.defense else 0
        defending.health -= damage
        if attacking.__class__.__name__ == "Vampire":
            attacking.vamp_heal(damage)
        if defending.health <= 0:
            break
        else:
            attacking, defending = defending, attacking
    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14
    priest.heal(freelancer)
    assert freelancer.health == 16

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
