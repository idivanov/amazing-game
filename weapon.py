class Weapon():
    '''Class, representing weapons in game'''
    def __init__(self, hp_bonus, attack_power, spell_power, armor):
        self.hp_bonus = hp_bonus
        self.attack_power = attack_power
        self.spell_power = spell_power
        self.armor = armor

    def __eq__(self, other):
        return self.hp_bonus == other.hp_bonus and \
                self.attack_power == other.attack_power and \
                self.spell_power == other.spell_power and \
                self.armor == other.armor
