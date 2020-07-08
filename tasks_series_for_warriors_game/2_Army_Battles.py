"""
In the previous mission - Warriors - you've learned how to make a duel between
2 warriors happen. Great job! But let's move to something that feels a little
more epic - the armies! In this mission your task is to add new classes and
functions to the existing ones. The new class should be the Army and have the
method add_units() - for adding the chosen amount of units to the army.
The first unit added will be the first to go to fight, the second will be
the second, ...
Also you need to create a Battle() class with a fight() function, which will
determine the strongest army.
The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and
the first warrior of the second army. As soon as one of them dies - the next
warrior from the army that lost the fighter enters the duel, and the surviving
warrior continues to fight with his current health. This continues until all
the soldiers of one of the armies die. In this case, the battle() function
should return True, if the first army won, or False, if the second one was
stronger.

Note that army 1 have the advantage to start every fight!

Input: The warriors and armies.

Output: The result of the battle (True or False).
"""


class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


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
        while army_1.units != [] and army_2.units != []:
            attacking, defending = army_1.units[0], army_2.units[0]
            while True:
                defending.health -= attacking.attack
                if defending.health <= 0:
                    break
                else:
                    attacking, defending = defending, attacking
            if army_1.units[0].is_alive:
                army_2.units.pop(0)
            else:
                army_1.units.pop(0)
        return army_1.units != []


def fight(unit_1, unit_2):
    attacking, defending = unit_1, unit_2
    while True:
        defending.health -= attacking.attack
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

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
