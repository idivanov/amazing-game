import weapon


class Character():
    def __init__(self, name, hit_points, attack_power,
                 spell_power, armor, magic_resist, weapon):
        self.name = name
        self.hit_points = hit_points
        self.health = hit_points
        self.attack_power = attack_power
        self.spell_power = spell_power
        self.armor = armor
        self.magic_resist = magic_resist
        self.weapon = None

    def damage_taken(self, hit, is_spell):
        taken = self.health
        if is_spell is True:
            self.health = self.health - (hit - self.magic_resist)
        else:
            self.health = self.health - (hit - self.armor)
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


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10, 10, 20, 10, None)
        self.bonus_turns = 0

    def strike(self):
        if self.bonus_turns > 0:
            self.bonus_turns -= 1
            return (self.attack_power + self.weapon.attack_power) * 1.5
        return self.attack_power + self.weapon.attack_power

    def heal(self):
        self.health += 10 + spell_power/2
        if self.health > self.hit_points:
            self.health = self.hit_points

    def bonus(self):
        self.bonus_turns = 2


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 120, 15, 0, 30, 5, None)

    def strike(self):
        return self.attack_power + self.weapon.attack_power

    def heal(self):
        self.armor += 10
        self.hit_points += 5
        self.health += 10
        self.magic_resist += 2
        if self.health > self.hit_points:
            self.health = self.hit_points

    def bonus(self):
        return "stun"


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 85, 0, 20, 10, 20, None)

    def strike(self):
        return self.spell_power + weapon.spell_power

    def heal(self):
        self.health += spell_power/2
        if self.health > self.hit_points:
            self.health = self.hit_points

    def bonus(self):
        return "silence"
