from math import floor


class Weapon:
    def __init__(self, health=0, attack=0, defense=0, vampirism=0,
                 heal_power=0):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power


class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.health = 5
        self.attack = 2


class Shield(Weapon):
    def __init__(self):
        super().__init__()
        self.health = 20
        self.attack = -1
        self.defense = 2


class GreatAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.health = -15
        self.attack = 5
        self.defense = -2
        self.vampirism = 10


class Katana(Weapon):
    def __init__(self):
        super().__init__()
        self.health = -20
        self.attack = 6
        self.defense = -5
        self.vampirism = 50


class MagicWand(Weapon):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.attack = 3
        self.heal_power = 3


class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50
        self.defense = 0

    @property
    def is_alive(self):
        return self.health > 0

    def equip_weapon(self, weapon_name):
        setattr(self, "max_health",
                self.__class__().health if not hasattr(self, "max_health")
                else self.max_health)
        health_before_get_weapon = self.health
        copy_unit_attrs = self.__class__().__dict__.copy()
        for unit_attr, unit_attr_value in copy_unit_attrs.items():
            for weapon_attr, weapon_attr_value in weapon_name.__dict__.items():
                if weapon_attr == unit_attr and unit_attr_value != 0:
                    self.__dict__[unit_attr] += weapon_attr_value
        copy_unit_attrs = self.__dict__.copy()
        for unit_attr, unit_attr_value in copy_unit_attrs.items():
            if unit_attr_value < 0:
                self.__dict__[unit_attr] = 0
        self.max_health += self.health - health_before_get_weapon


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
        if not hasattr(self, "max_health"):
            self.max_health = self.__class__().health
        hurt = self.max_health - self.health
        if hurt > 0:
            vamp_hp = floor(damage * self.vampirism / 100)
            self.health += vamp_hp if hurt > vamp_hp else hurt


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
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
        if not hasattr(unit, "max_health"):
            unit.max_health = unit.__class__().health
        hurt = unit.max_health - unit.health
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

                if not attacking_unit.is_alive:
                    attacking_army.units.pop(0)
                    break

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

                attacking_army, defending_army = defending_army, attacking_army

        return army_1.units != []

    @staticmethod
    def straight_fight(army_1, army_2):
        while army_1.units != [] and army_2.units != []:
            for i in range(min(len(army_1.units), len(army_2.units))):
                if fight(army_1.units[i], army_2.units[i]):
                    army_2.units[i] = "dead_body"
                else:
                    army_1.units[i] = "dead_body"
            for some_army in [army_1, army_2]:
                while some_army.units.count("dead_body") > 0:
                    some_army.units.remove("dead_body")
        return army_1.units != []


def fight(unit_1, unit_2):
    attacking, defending = unit_1, unit_2
    while True:
        if not attacking.is_alive:
            break
        damage = attacking.attack - defending.defense if \
            attacking.attack > defending.defense else 0
        defending.health -= damage
        if attacking.__class__.__name__ == "Vampire":
            attacking.vamp_heal(damage)
        if defending.health <= 0:
            break
        attacking, defending = defending, attacking
    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary
    # for auto-testing

    ogre = Warrior()
    lancelot = Knight()
    richard = Defender()
    eric = Vampire()
    freelancer = Lancer()
    priest = Healer()

    sword = Sword()
    shield = Shield()
    axe = GreatAxe()
    katana = Katana()
    wand = MagicWand()
    super_weapon = Weapon(50, 10, 5, 150, 8)

    ogre.equip_weapon(sword)
    ogre.equip_weapon(shield)
    ogre.equip_weapon(super_weapon)
    lancelot.equip_weapon(super_weapon)
    richard.equip_weapon(shield)
    eric.equip_weapon(super_weapon)
    freelancer.equip_weapon(axe)
    freelancer.equip_weapon(katana)
    priest.equip_weapon(wand)
    priest.equip_weapon(shield)

    assert ogre.health == 125
    assert lancelot.attack == 17
    assert richard.defense == 4
    assert eric.vampirism == 200
    assert freelancer.health == 15
    assert priest.heal_power == 5

    assert fight(ogre, eric) is False
    assert fight(priest, richard) is False
    assert fight(lancelot, freelancer) is True

    my_army = Army()
    my_army.add_units(Knight, 1)
    my_army.add_units(Lancer, 1)

    enemy_army = Army()
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 1)

    my_army.units[0].equip_weapon(axe)
    my_army.units[1].equip_weapon(super_weapon)

    enemy_army.units[0].equip_weapon(katana)
    enemy_army.units[1].equip_weapon(wand)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is True

    print("Coding complete? Let's try tests!")
