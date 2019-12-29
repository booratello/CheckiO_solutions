"""
So we have 3 types of units: the Warrior, Knight and Defender. Let's make the
battles even more epic and add another type - the Vampire!
Vampire should be the subclass of the Warrior class and have the additional
vampirism parameter, which helps him to heal himself. When the Vampire hits
the other unit, he restores his health by +50% of the dealt damage (enemy
defense makes the dealt damage value lower).

The basic parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%

Input: The warriors and armies.

Output: The result of the battle (True or False).
"""


class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50
        self.defense = 0
        self.vampirism = 0

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
                damage = attacking.attack - defending.defense if \
                    attacking.attack > defending.defense else 0
                defending.health -= damage
                attacking.health += damage * attacking.vampirism / 100
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

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
