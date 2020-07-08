"""
It seems that the Warrior, Knight, Defender and Vampire are not enough
to win the battle. Let's add one more powerful unit type - the Lancer.
Lancer should be the subclass of the Warrior class and should attack in
a specific way - when he hits the other unit, he also deals a 50% of
the deal damage to the enemy unit, standing behind the firstly assaulted
one (enemy defense makes the deal damage value lower - consider this).
The basic parameters of the Lancer:
health = 50
attack = 6

Input: The warriors and armies.

Output: The result of the battle (True or False).

Precondition: 5 types of units.
"""


class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50
        self.defense = 0
        self.vampirism = 0
        self.punching_attack = 0

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


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.health = 50
        self.punching_attack = 50


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
            attacking_army, defending_army = army_1, army_2

            while True:
                attacking_unit, defending_unit = \
                    attacking_army.units_list[0], defending_army.units_list[0]
                damage = attacking_unit.attack - defending_unit.defense if \
                    attacking_unit.attack > defending_unit.defense else 0
                defending_unit.health -= damage
                attacking_unit.health += \
                    damage * attacking_unit.vampirism / 100

                if len(defending_army.units_list) > 1:
                    behind_defending_unit = defending_army.units_list[1]
                    damage = (damage * attacking_unit.punching_attack / 100
                              - behind_defending_unit.defense)
                    behind_defending_unit.health -= damage if damage > 0 else 0
                    if not behind_defending_unit.is_alive:
                        defending_army.units_list.pop(1)

                if not defending_unit.is_alive:
                    defending_army.units_list.pop(0)
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
        attacking.health += damage * attacking.vampirism / 100
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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False
    assert fight(bob, mike) is False
    assert fight(lancelot, rog) is True
    assert fight(eric, richard) is False
    assert fight(ogre, adam) is True
    assert fight(freelancer, vampire) is True
    assert freelancer.is_alive is True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is True
    assert battle.fight(army_3, army_4) is False
    print("Coding complete? Let's try tests!")
