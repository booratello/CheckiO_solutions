"""
You need to create the class Warrior, the instances of which will have 2 parameters - health (equal to 50 points) and
attack (equal to 5 points), and 1 property - is_alive, which can be True (if warrior's health is > 0) or False (in the
other case). In addition you have to create the second unit type - Knight, which should be the subclass of the Warrior
but have the increased attack - 7. Also you have to create a function fight(), which will initiate the duel between 2
warriors and define the strongest of them. The duel occurs according to the following principle:
- Every turn, the first warrior will hit the second and this second will lose his health in the same value as the attack
of the first warrior.
- After that, if he is still alive, the second warrior will do the same to the first one.
The fight ends with the death of one of them. If the first warrior is still alive (and thus the other one is not
anymore), the function should return True, False otherwise.

Input: The warriors.

Output: The result of the duel (True or False).
"""

class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50

    @property
    def is_alive(self):
        return True if self.health > 0 else False


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    attacking, defending = unit_1, unit_2
    while True:
        defending.health -= attacking.attack
        if defending.health <= 0:
            break
        else:
            attacking, defending = defending, attacking
    return True if unit_1.is_alive else False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

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

    print("Coding complete? Let's try tests!")
