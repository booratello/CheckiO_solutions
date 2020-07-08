from math import floor

"""
In this mission you should add a new class Warlord(), which should be the 
subclass of the Warrior class and have the next characteristics:
health = 100
attack = 4
defense = 2

Also, when the Warlord is included in any of the armies, that particular army 
gets the new move_units() method which allows to rearrange the units of that 
army for the better battle result. The rearrangement is done not only before 
the battle, but during the battle too, each time the allied units die. 
The rules for the rearrangement are as follow:
1. If there are Lancers in the army, they should be placed in front of everyone 
else.
2. If there is a Healer in the army, he should be placed right after the first 
soldier to heal him during the fight. If the number of Healers is > 1, all of 
them should be placed right behind the first Healer.
3. If there are no more Lancers in the army, but there are other soldiers who 
can deal damage, they also should be placed in first position, and the Healer 
should stay in the 2nd row (if army still has Healers).
4. Warlord should always stay way in the back to look over the battle and 
rearrange the soldiers when it's needed.
5. Every army can have no more than 1 Warlord.
6. If the army doesn’t have a Warlord, it can’t use the move_units() method.

Input: The warriors, armies and weapons.

Output: The result of the battle (True or False).

How it is used: For computer games development.

Precondition: 6 types of units, 2 types of battles
"""


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
        damage_to_second_defending = \
            damage * self.puncture / 100 - second_defending.defense
        second_defending.health -= damage_to_second_defending if \
            damage_to_second_defending > 0 else 0


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


class Warlord(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 4
        self.health = 100
        self.defense = 2


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, what_unit, how_many):
        while how_many != 0:
            self.units.append(what_unit())
            how_many -= 1

    @classmethod
    def find_unit(cls, units_list, name):
        units_count = 0
        if any(type(i) == name for i in units_list):
            for el in units_list:
                if type(el) == name:
                    units_count += 1
        return units_count

    @classmethod
    def sort_units(cls, all_fighters, types_of_required_fighters,
                   count_of_required_fighters):
        required_fighters = []
        if count_of_required_fighters > 0:
            for i in range(len(all_fighters)):
                if len(required_fighters) == count_of_required_fighters:
                    break
                i -= len(required_fighters)
                if type(all_fighters[i]) in types_of_required_fighters:
                    required_fighters.append(all_fighters.pop(i))
            if types_of_required_fighters == [Healer]:
                for i in range(count_of_required_fighters):
                    all_fighters.insert(i + 1, required_fighters[i])
            elif types_of_required_fighters != [Warlord]:
                for i in range(count_of_required_fighters):
                    all_fighters.insert(i, required_fighters[i])
            else:
                all_fighters.append(required_fighters[0])
        return all_fighters

    def move_units(self):
        counter = Army.find_unit(self.units, Warlord)
        if counter > 0:
            self.units = Army.sort_units(self.units, [Warlord], counter)
            counter = Army.find_unit(self.units, Lancer)
            if counter > 0:
                self.units = Army.sort_units(self.units, [Lancer], counter)
            else:
                who_can_fight = []
                for el in self.units:
                    if el.attack > 0 and type(el) != Warlord:
                        who_can_fight.append(type(el))
                counter = len(who_can_fight)
                self.units = Army.sort_units(self.units,
                                             list(set(who_can_fight)), counter)
            counter = Army.find_unit(self.units, Healer)
            if counter > 0 and counter + 1 != len(self.units):
                self.units = Army.sort_units(self.units, [Healer], counter)


class Battle:
    @staticmethod
    def fight(army_1, army_2):
        army_1.move_units()
        army_2.move_units()
        while army_1.units != [] and army_2.units != []:
            attacking_army, defending_army = army_1, army_2
            while True:
                attacking_unit, defending_unit = \
                    attacking_army.units[0], defending_army.units[0]

                if not attacking_unit.is_alive:
                    attacking_army.units.pop(0)
                    attacking_army.move_units()
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
                    defending_army.move_units()
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

    ronald = Warlord()
    heimdall = Knight()

    assert fight(heimdall, ronald) is False

    my_army = Army()
    my_army.add_units(Warlord, 1)
    my_army.add_units(Warrior, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 2)

    enemy_army = Army()
    enemy_army.add_units(Warlord, 3)
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 2)
    enemy_army.add_units(Knight, 2)

    my_army.move_units()
    enemy_army.move_units()

    assert type(my_army.units[0]) == Lancer
    assert type(my_army.units[1]) == Healer
    assert type(my_army.units[-1]) == Warlord

    assert type(enemy_army.units[0]) == Vampire
    assert type(enemy_army.units[-1]) == Warlord
    assert type(enemy_army.units[-2]) == Knight

    # 6, not 8, because only 1 Warlord per army could be
    assert len(enemy_army.units) == 6

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is True

print("Coding complete? Let's try tests!")
