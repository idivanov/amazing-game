import unittest
import bot


class BotTest(unittest.TestCase):

    def setUp(self):
        self.test_bot = bot.Bot(10, 20)
        self.test_warlock = bot.Warlock()
        self.test_berserker = bot.Berserker()
        self.test_boss = bot.Boss()

    def test_initialize_bot(self):
        self.assertEqual(10, self.test_bot.hit_points)
        self.assertEqual(20, self.test_bot.power)
        self.assertEqual("Bot", self.test_bot.type)
        self.assertEqual(0, self.test_bot.no_attack)

    def test_initialize_warlock(self):
        self.assertEqual(50, self.test_warlock.hit_points)
        self.assertEqual(20, self.test_warlock.power)
        self.assertEqual("Warlock", self.test_warlock.type)
        self.assertEqual(0, self.test_warlock.no_attack)

    def test_initialize_berserker(self):
        self.assertEqual(100, self.test_berserker.hit_points)
        self.assertEqual(20, self.test_berserker.power)
        self.assertEqual("Berserker", self.test_berserker.type)
        self.assertEqual(0, self.test_berserker.no_attack)

    def test_initialize_boss(self):
        self.assertEqual(1000, self.test_boss.hit_points)
        self.assertEqual(1, self.test_boss.power)
        self.assertEqual("Boss", self.test_boss.type)
        self.assertEqual(0, self.test_boss.no_attack)

    def test_bot_skills(self):
        self.assertEqual("Bot", self.test_bot.type)
        self.assertEqual(10, self.test_bot.hit_points)
        self.assertEqual("{} has {} health".format(
                            self.test_bot.type, self.test_bot.hit_points
                            ),
                        self.test_bot.current_health())
        self.assertEqual(True, self.test_bot.is_alive())

    def test_warlock_skills(self):
        self.assertEqual(50, self.test_warlock.hit_points)
        self.assertEqual("Warlock", self.test_warlock.type)
        self.assertEqual((20, "magic"), self.test_warlock.attack())
        self.test_warlock.damage_taken(10)
        self.assertEqual(40, self.test_warlock.hit_points)
        self.test_warlock.damage_taken("stun")
        self.assertEqual(2, self.test_warlock.no_attack)
        self.assertEqual(30, self.test_warlock.hit_points)
        self.test_warlock.damage_taken("silence")
        self.assertEqual(4, self.test_warlock.no_attack)
        self.assertEqual((0, "magic"), self.test_warlock.attack())

    def test_berserker_skills(self):
        self.assertEqual(100, self.test_berserker.hit_points)
        self.assertEqual("Berserker", self.test_berserker.type)
        self.assertEqual((20, "melee"), self.test_berserker.attack())
        self.test_berserker.damage_taken(10)
        self.assertEqual(90, self.test_berserker.hit_points)
        self.test_berserker.damage_taken("stun")
        self.assertEqual(4, self.test_berserker.no_attack)
        self.assertEqual(80, self.test_berserker.hit_points)
        self.test_berserker.damage_taken("silence")
        self.assertEqual(2, self.test_berserker.no_attack)
        self.assertEqual((0, "melee"), self.test_berserker.attack())

    def test_boss_skills(self):
        self.assertEqual(1000, self.test_boss.hit_points)
        self.assertEqual("Boss", self.test_boss.type)
        self.assertEqual((1, "boss"), self.test_boss.attack())
        self.test_boss.damage_taken(10)
        self.assertEqual(990, self.test_boss.hit_points)
        self.test_boss.damage_taken("stun")
        self.assertEqual(2, self.test_boss.no_attack)
        self.assertEqual(990, self.test_boss.hit_points)
        self.test_boss.damage_taken("silence")
        self.assertEqual(2, self.test_boss.no_attack)
        self.assertEqual((0, "boss"), self.test_boss.attack())

if __name__ == '__main__':
    unittest.main()
