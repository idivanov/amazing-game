from character import *
from bot import *
from weapon import *


class Battle():
    def __init__(self, character, bot):
        self.character = character
        self.bot = bot

    def user_input(self):
        spell_description = "1 - attack\n2 - heal \n3 - bonus\n"
        return input(spell_description +
            "Enter your choice for this turn(1/2/3): ")

    def start(self):
        character_dmg = 0
        bot_dmg = 0

        while self.character.is_alive() and self.bot.is_alive():
            print ("------------")
            print ("Begin of the round")
            print ("------------")
            print (self.character.current_health())
            print (self.bot.current_health())
            print ("------------")

            user_input = self.user_input()
            if user_input == '2':
                character_dmg = self.character.heal()
            elif user_input == '3':
                character_dmg = self.character.bonus()
            else:
                character_dmg = self.character.strike()

            print("{} deals {} dmg".format(self.character.name,
                character_dmg))
            self.bot.damage_taken(character_dmg)

            if not self.bot.is_alive():
                return

            bot_dmg = self.bot.attack()
            self.character.damage_taken(bot_dmg)
            print("{} deals {} dmg".format(self.bot.type, bot_dmg))

            print ("------------")
            print ("End of the round")
            print ("------------")
            print (self.character.current_health())
            print (self.bot.current_health())
            print ("------------\n\n")

    def result(self):
        if self.character.is_alive():
            return "{} wins\n".format(self.character.name)\
             + self.character.current_health()
        return "{} wins\n Game over".format(self.bot.type)
