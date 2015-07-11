import unittest
import weapon


class WeaponTest(unittest.TestCase):

    def setUp(self):
        self.test_weapon = weapon.Weapon(10, 10, 10, 10)

    def test_initialize_weapon(self):
        self.assertEqual(10, self.test_weapon.hp_bonus)
        self.assertEqual(10, self.test_weapon.attack_power)
        self.assertEqual(10, self.test_weapon.spell_power)
        self.assertEqual(10, self.test_weapon.armor)

if __name__ == '__main__':
    unittest.main()
