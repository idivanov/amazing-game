from character import *
from bot import *
from weapon import *


class Battle():
    def __init__(self, character, bot):
        self.character = character
        self.bot = bot

    def start(self):
        character_dmg = 0
        bot_dmg = 0
        while self.character.is_alive():
            character_dmg = self.character.strike()
            self.bot.damage_taken(character_dmg)
            if self.bot.is_alive():
                bot_dmg = self.bot.attack()
                self.character.damage_taken(bot_dmg, True)
            else:
                print("{} wins".format(self.character.name))
                return None
        print ("bot wins")


sword = Weapon(10, 10, 0, 0)
az = Paladin("NIKIFOR")
az.equip_weapon(sword)
bot = Bot(50, 20)

b = Battle(az, bot)
b.start()
