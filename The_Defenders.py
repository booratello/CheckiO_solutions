"""
In the previous mission - Army battles, you've learned how to make a battle
between 2 armies. But we have only 2 types of units - the Warriors and Knights.
Let's add another one - the Defender. It should be the subclass of the Warrior
class and have an additional defense parameter, which helps him to survive
longer. When another unit hits the defender, he loses a certain amount of his
health according to the next formula: enemy attack - self defense (if enemy
attack > self defense). Otherwise, the defender doesn't lose his health.

The basic parameters of the Defender:
health = 60
attack = 3
defense = 2

The warriors and armies.

The result of the battle (True or False)
"""


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


class Army:
    def __init__(self):
        self.units_list = []

    def add_units(self, what_unit, how_many):
        while how_many != 0:
            self.units_list.append(what_unit())
            how_many -= 1


class Battle:
    @staticmethod
    def fight(army_1, army_2):
        while army_1.units_list != [] and army_2.units_list != []:
            attacking, defending = army_1.units_list[0], army_2.units_list[0]
            while True:
                defending.health -= attacking.attack - defending.defense if \
                    attacking.attack > defending.defense else 0
                if defending.health <= 0:
                    break
                else:
                    attacking, defending = defending, attacking
            if army_1.units_list[0].is_alive:
                army_2.units_list.pop(0)
            else:
                army_1.units_list.pop(0)
        return army_1.units_list != []


def fight(unit_1, unit_2):
    attacking, defending = unit_1, unit_2
    while True:
        defending.health -= attacking.attack - defending.defense if \
            attacking.attack > defending.defense else 0
        if defending.health <= 0:
            break
        else:
            attacking, defending = defending, attacking
    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary
    # for auto-testing

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

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
