class Bot():
    def __init__(self, hit_points, power):
        self.hit_points = hit_points
        self.power = power

    def damage_taken(self, hit):
        print ("Bot takes {} dmg".format(hit))
        self.hit_points -= hit

    def attack(self):
        print ("Bot hits for {}".format(self.power))
        return self.power

    def is_alive(self):
        return self.hit_points > 0
