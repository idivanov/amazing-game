import unittest
import game
import character
import maps
import weapon


class GameTest(unittest.TestCase):

    def setUp(self):
        self.test_map1 = ".........." + \
                         ".........." + \
                         ".........." + \
                         ".........." + \
                         ".........$"

        self.test_map2 = "P........." + \
                         ".........." + \
                         ".........." + \
                         ".........." + \
                         ".........$"

        self.test_map3 = ".P........" + \
                         ".........." + \
                         ".........." + \
                         ".........." + \
                         ".........$"

        self.test_map4 = ".........." + \
                         ".P........" + \
                         ".........." + \
                         ".........." + \
                         ".........$"

        self.test_map5 = ".........." + \
                         "P........." + \
                         ".........." + \
                         ".........." + \
                         ".........$"

        self.test_map6 = ".#........" + \
                         "#P#......." + \
                         ".#........" + \
                         ".........." + \
                         ".........$"

        self.test_map7 = ".........." + \
                         ".........." + \
                         ".........." + \
                         ".........." + \
                         "P........$"

        self.test_map8 = ".........P" + \
                         ".........." + \
                         ".........." + \
                         ".........." + \
                         ".........$"

        self.test_game = game.Game(self.test_map1)
        self.test_blocked_game = game.Game(self.test_map6)
        self.test_unavailable_game1 = game.Game(self.test_map7)
        self.test_unavailable_game2 = game.Game(self.test_map8)
        self.test_character = character.Paladin("Nikifor")
        self.test_weapon = weapon.Weapon(10, 10, 10, 10)

    def test_initialize_game(self):
        self.assertEqual(self.test_map1, self.test_game.map)
        self.assertEqual(0, self.test_game.player_location)
        self.assertEqual(None, self.test_game.character)

    def test_available_moves(self):
        self.assertEqual(self.test_map1, self.test_game.map)
        self.test_game.update_location()
        self.assertEqual(self.test_map2, self.test_game.map)
        self.test_game.move_right()
        self.assertEqual(self.test_map3, self.test_game.map)
        self.test_game.move_down()
        self.assertEqual(self.test_map4, self.test_game.map)
        self.test_game.move_left()
        self.assertEqual(self.test_map5, self.test_game.map)
        self.test_game.move_up()
        self.assertEqual(self.test_map2, self.test_game.map)

    def test_blocked_moves(self):
        self.test_blocked_game.player_location = 11
        self.test_blocked_game.update_location()

        self.assertEqual(self.test_map6, self.test_blocked_game.map)
        self.test_blocked_game.move_up()
        self.assertEqual(self.test_map6, self.test_blocked_game.map)
        self.test_blocked_game.move_down()
        self.assertEqual(self.test_map6, self.test_blocked_game.map)
        self.test_blocked_game.move_left()
        self.assertEqual(self.test_map6, self.test_blocked_game.map)
        self.test_blocked_game.move_right()
        self.assertEqual(self.test_map6, self.test_blocked_game.map)

    def test_unavailable_down_and_left(self):
        self.test_unavailable_game1.player_location = 40
        self.test_unavailable_game1.update_location()

        self.assertEqual(self.test_map7, self.test_unavailable_game1.map)
        self.test_unavailable_game1.move_down()
        self.assertEqual(self.test_map7, self.test_unavailable_game1.map)
        self.test_unavailable_game1.move_left()
        self.assertEqual(self.test_map7, self.test_unavailable_game1.map)

    def test_unavailable_up_and_right(self):
        self.test_unavailable_game2.player_location = 9
        self.test_unavailable_game2.update_location()

        self.assertEqual(self.test_map8, self.test_unavailable_game2.map)
        self.test_unavailable_game2.move_up()
        self.assertEqual(self.test_map8, self.test_unavailable_game2.map)
        self.test_unavailable_game2.move_right()
        self.assertEqual(self.test_map8, self.test_unavailable_game2.map)

    def test_select_character(self):
        self.test_game.select_character(self.test_character, self.test_weapon)
        self.assertEqual(self.test_game.character, self.test_character)
        self.assertEqual(self.test_game.character.weapon, self.test_weapon)

    def test_win_play(self):
        self.test_game.player_location = 49
        self.test_game.update_location()
        self.test_game.select_character(self.test_character, self.test_weapon)
        self.assertEqual("You won!", self.test_game.play(True))


if __name__ == '__main__':
    unittest.main()
