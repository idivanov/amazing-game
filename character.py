from weapon import *


class Character():
    '''Class representing your character'''
    def __init__(self, name, hit_points, attack_power,
                 spell_power, armor, magic_resist):
        self.name = name
        self.hit_points = hit_points
        self.health = hit_points
        self.attack_power = attack_power
        self.spell_power = spell_power
        self.armor = armor
        self.magic_resist = magic_resist
        self.weapon = Weapon(0, 0, 0, 0)

    def damage_taken(self, hit):
        taken = self.health
        if hit[1] is "magic":
            if hit[0] >= self.magic_resist:
                self.health = self.health - (hit[0] - self.magic_resist)
        if hit[1] is "melee":
            if hit[0] >= self.armor:
                self.health = self.health - (hit[0] - self.armor)
        if hit[1] is not "magic" and hit[1] is not "melee":
            self.health = self.health - hit[0]

        print ("{} takes {} dmg!".format(self.name, taken-self.health))

    def strike(self):
        pass

    def heal(self):
        pass

    def bonus(self):
        pass

    def is_alive(self):
        return self.health > 0

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.hit_points += self.weapon.hp_bonus
        self.health = self.hit_points

    def current_health(self):
        return "{} has {}/{} health".format(self.name,
            self.health, self.hit_points)


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10, 10, 20, 10)
        self.bonus_turns = 0

    def strike(self):
        if self.bonus_turns > 0:
            self.bonus_turns -= 1
            return (self.attack_power + self.weapon.attack_power) * 2
        return self.attack_power + self.weapon.attack_power

    def heal(self):
        self.health += 10 + self.spell_power/2
        if self.health > self.hit_points:
            self.health = self.hit_points
        return 0

    def bonus(self):
        '''Activating your bonus - dealing double damage in your next 3 turns'''
        self.bonus_turns = 3
        return self.weapon.attack_power


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 120, 15, 0, 30, 5)

    def strike(self):
        return self.attack_power + self.weapon.attack_power

    def heal(self):
        self.armor += 10
        self.hit_points += 5
        self.health += 10
        self.magic_resist += 2
        if self.health > self.hit_points:
            self.health = self.hit_points
        return 0

    def bonus(self):
        '''Stunning your enemy'''
        return "stun"


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 85, 0, 20, 10, 20)

    def strike(self):
        return self.spell_power + self.weapon.spell_power

    def heal(self):
        self.health += self.spell_power/2
        if self.health > self.hit_points:
            self.health = self.hit_points
        return 0

    def bonus(self):
        '''silencing your enemy'''
        return "silence"
