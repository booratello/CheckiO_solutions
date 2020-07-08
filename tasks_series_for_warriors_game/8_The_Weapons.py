from math import floor

"""
In this mission you should create a new class Weapon(health, attack, defense, 
vampirism, heal_power) which will equip your soldiers with weapons. Every 
weapon's object will have the parameters that will show how the soldier's 
characteristics change while he uses this weapon. Assume that if the soldier 
doesn't have some of the characteristics (for example, defense or vampirism), 
but the weapon have those, these parameters don't need to be added to the 
soldier.

The parameters list:
health - add to the current health and the maximum health of the soldier this 
modificator;
attack - add to the soldier's attack this modificator;
defense - add to the soldier's defense this modificator;
vampirism - increase the soldier’s vampirism to this number (in %. So 
vampirism = 20 means +20%);
heal_power - increase the amount of health which the healer restore for the 
allied unit.

All parameters could be positive or negative, so when a negative modificator is
being added to the soldier’s stats, they are decreasing, but none of them can 
be less than 0.

Let’s look at this example: vampire (basic parameters: health = 40, attack = 4,
vampirism = 50%) equip the Weapon(20, 5, 2, -60, -1). The vampire has the 
health and the attack, so they will change - health will grow up to 60 
(40 + 20), attack will be 9 (4 + 5). The vampire doesn’t have defense or the 
heal_power, so these weapon modificators will be ignored. The weapon's 
vampirism modificator -60% will work as well. The standard vampirism value is 
only 50%, so we’ll get -10%. But, as we said before, the parameters can’t be 
less than 0, so the vampirism after all manipulations will be just 0%.

Also you should create a few standard weapons classes, which should be the 
subclasses of the Weapon. Here’s their list:
Sword - health +5, attack +2
Shield - health +20, attack -1, defense +2
GreatAxe - health -15, attack +5, defense -2, vampirism +10%
Katana - health -20, attack +6, defense -5, vampirism +50%
MagicWand - health +30, attack +3, heal_power +3

And finally, you should add an equip_weapon(weapon_name) method to all of the 
soldiers classes. It should equip the chosen soldier with the chosen weapon.
This method also should work for the units in the army. You should hold them in
the list and use it like this:
my_army.units[0].equip_weapon(Sword())- equip the first soldier with the sword.

Notes:
While healing (both vampirism and health restored by the healer), the health 
can’t be greater than the maximum amount of health for this unit (with 
consideration of all of the weapon's modificators).
If the heal from vampirism is float (for example 3.6, 1.1, 2.945), round it 
down in any case. So 3.6 = 3, 1.1 = 1, 2.945 = 2.
Every soldier can be equipped with any number of weapons and get all their 
bonuses, but if he wears too much weapons with the negative health modificator 
and his health is lower or equal 0 - he is as good as dead, which is actually 
pretty dead in this case.

Input: The warriors, armies and weapons.

Output: The result of the battle (True or False).

How it is used: For computer games development.

Precondition: 5 types of units, 2 types of battles
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
