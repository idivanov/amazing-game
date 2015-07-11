class Bot():
    def __init__(self, hit_points, power):
        self.hit_points = hit_points
        self.power = power
        self.type = "Bot"
        self.no_attack = 0

    def damage_taken(self, hit):
        pass

    def attack(self):
        pass

    def is_alive(self):
        return self.hit_points > 0

    def current_health(self):
        return "{} has {} health".format(self.type, self.hit_points)


class Warlock(Bot):
    '''Spell using enemy'''
    def __init__(self):
        super().__init__(50, 20)
        self.type = "Warlock"

    def attack(self):
        if self.no_attack > 0:
            self.no_attack -= 1
            return (0, "magic")
        return (self.power, "magic")

    def damage_taken(self, hit):
        if hit is "stun":
            self.no_attack = 2
            self.hit_points -= 10
            return (0, "magic")

        if hit is "silence":
            self.no_attack = 4
            return (0, "magic")

        self.hit_points -= hit


class Berserker(Bot):
    '''Melee using enemy'''
    def __init__(self):
        super().__init__(100, 20)
        self.type = "Berserker"

    def attack(self):
        if self.no_attack > 0:
            self.no_attack -= 1
            return (0, "melee")
        return(self.power, "melee")

    def damage_taken(self, hit):
        if hit is "stun":
            self.no_attack = 4
            self.hit_points -= 10
            return (0, "melee")

        if hit is "silence":
            self.no_attack = 2
            return (0, "melee")

        self.hit_points -= hit


class Boss(Bot):
    '''Final enemy'''
    def __init__(self):
        super().__init__(1000, 1)
        self.type = "Boss"

    def attack(self):
        if self.no_attack > 0:
            self.no_attack -= 1
            return (0, "boss")
        return (self.power, "boss")

    def damage_taken(self, hit):
        if hit is "stun":
            self.no_attack = 2
            return

        if hit is "silence":
            self.no_attack = 2
            return

        self.hit_points -= hit
