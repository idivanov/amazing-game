import unittest
import character
import weapon


class CharacterTest(unittest.TestCase):

    def setUp(self):
        self.test_character = character.Character('NIKIFOR', 100, 0, 0, 0, 0)
        self.test_paladin = character.Paladin('UNUFRI')
        self.test_mage = character.Mage('URSULA')
        self.test_warrior = character.Warrior('GENADI')
        self.test_default_weapon = weapon.Weapon(0, 0, 0, 0)
        self.test_weapon = weapon.Weapon(10, 10, 10, 10)

    def test_initialize_character(self):
        self.assertEqual('NIKIFOR', self.test_character.name)
        self.assertEqual(100, self.test_character.hit_points)
        self.assertEqual(100, self.test_character.health)
        self.assertEqual(0, self.test_character.attack_power)
        self.assertEqual(0, self.test_character.spell_power)
        self.assertEqual(0, self.test_character.armor)
        self.assertEqual(0, self.test_character.magic_resist)
        self.assertEqual(self.test_default_weapon, self.test_character.weapon)

    def test_initialize_paladin(self):
        self.assertEqual('UNUFRI', self.test_paladin.name)
        self.assertEqual(100, self.test_paladin.hit_points)
        self.assertEqual(100, self.test_paladin.health)
        self.assertEqual(10, self.test_paladin.attack_power)
        self.assertEqual(10, self.test_paladin.spell_power)
        self.assertEqual(20, self.test_paladin.armor)
        self.assertEqual(10, self.test_paladin.magic_resist)
        self.assertEqual(self.test_default_weapon, self.test_paladin.weapon)

    def test_initialize_mage(self):
        self.assertEqual('URSULA', self.test_mage.name)
        self.assertEqual(85, self.test_mage.hit_points)
        self.assertEqual(85, self.test_mage.health)
        self.assertEqual(0, self.test_mage.attack_power)
        self.assertEqual(20, self.test_mage.spell_power)
        self.assertEqual(10, self.test_mage.armor)
        self.assertEqual(20, self.test_mage.magic_resist)
        self.assertEqual(self.test_default_weapon, self.test_mage.weapon)

    def test_initialize_warrior(self):
        self.assertEqual('GENADI', self.test_warrior.name)
        self.assertEqual(120, self.test_warrior.hit_points)
        self.assertEqual(120, self.test_warrior.health)
        self.assertEqual(15, self.test_warrior.attack_power)
        self.assertEqual(0, self.test_warrior.spell_power)
        self.assertEqual(30, self.test_warrior.armor)
        self.assertEqual(5, self.test_warrior.magic_resist)
        self.assertEqual(self.test_default_weapon, self.test_warrior.weapon)

    def test_character_skills(self):
        self.assertEqual(100, self.test_character.health)
        self.test_character.damage_taken((10, "magic"))
        self.assertEqual(90, self.test_character.health)
        self.test_character.damage_taken((10, "melee"))
        self.assertEqual(80, self.test_character.health)
        self.test_character.damage_taken((10, "boss"))
        self.assertEqual(70, self.test_character.health)
        self.assertEqual('{} has {}/{} health'.format(
                        self.test_character.name,
                        self.test_character.health,
                        self.test_character.hit_points),
                        self.test_character.current_health())
        self.assertEqual(True, self.test_character.is_alive())

    def test_equip_weapon(self):
        self.test_character.equip_weapon(self.test_weapon)
        self.assertEqual(self.test_weapon, self.test_character.weapon)

    def test_paladin_skills(self):
        self.assertEqual(10, self.test_paladin.strike())
        self.assertEqual(0, self.test_paladin.heal())
        self.assertEqual(0, self.test_paladin.bonus())
        self.assertEqual('{} has {}/{} health'.format(
                        self.test_paladin.name,
                        self.test_paladin.health,
                        self.test_paladin.hit_points),
                        self.test_paladin.current_health())

    def test_mage_skills(self):
        self.assertEqual(20, self.test_mage.strike())
        self.assertEqual(0, self.test_mage.heal())
        self.assertEqual("silence", self.test_mage.bonus())
        self.assertEqual('{} has {}/{} health'.format(
                        self.test_mage.name,
                        self.test_mage.health,
                        self.test_mage.hit_points),
                        self.test_mage.current_health())

    def test_warrior_skills(self):
        self.assertEqual(15, self.test_warrior.strike())
        self.assertEqual(0, self.test_warrior.heal())
        self.assertEqual("stun", self.test_warrior.bonus())
        self.assertEqual('{} has {}/{} health'.format(
                        self.test_warrior.name,
                        self.test_warrior.health,
                        self.test_warrior.hit_points),
                        self.test_warrior.current_health())
        self.assertEqual(125, self.test_warrior.hit_points)
        self.assertEqual(40, self.test_warrior.armor)
        self.assertEqual(125, self.test_warrior.health)
        self.assertEqual(7, self.test_warrior.magic_resist)

if __name__ == '__main__':
    unittest.main()
