import unittest
import battle
import bot
import character


class BattleTest(unittest.TestCase):

    def setUp(self):
        self.test_dead_bot = bot.Bot(0, 0)
        self.test_alive_bot = bot.Bot(10, 10)
        self.test_dead_character = character.Character("Dead", 0, 0, 0, 0, 0)
        self.test_alive_character = \
            character.Character("Alive", 10, 10, 10, 10, 10)
        self.test_bot_battle = \
            battle.Battle(self.test_dead_character, self.test_alive_bot)
        self.test_character_battle = \
            battle.Battle(self.test_alive_character, self.test_dead_bot)

    def test_initialize_battle(self):
        self.assertEqual(self.test_dead_bot, self.test_character_battle.bot)
        self.assertEqual(self.test_dead_character,
                        self.test_bot_battle.character)
        self.assertEqual(self.test_alive_bot, self.test_bot_battle.bot)
        self.assertEqual(self.test_alive_character, 
                        self.test_character_battle.character)

    def test_bot_battle(self):
        self.test_bot_battle.start()
        self.assertEqual("{} wins\n Game over".format(
                self.test_alive_bot.type),
            self.test_bot_battle.result())

    def test_character_battle(self):
        self.test_character_battle.start()
        self.assertEqual("{} wins\n".format(
                                self.test_alive_character.name
                                            ) + 
                            self.test_alive_character.current_health(),
                        self.test_character_battle.result())

if __name__ == '__main__':
    unittest.main()