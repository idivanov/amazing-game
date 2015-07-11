from battle import *
from weapon import *
import maps
import random


class Game():
    def __init__(self, map):
        self.map = map
        self.player_location = 0
        self.character = None

    def print_map(self):
        '''printing the map'''
        self.update_location()
        for row in range(maps.ROWS):
            line = ""
            for _ in range(maps.COLUMNS):
                line += self.map[row*10 + _]
            print(line)
        print()

    def update_location(self):
        '''Updating the location of the player in the map'''
        new_map = ""
        for _ in range(50):
            if _ == self.player_location:
                new_map += 'P'
            elif self.map[_] == 'P' and _ is not self.player_location:
                new_map += '.'
            else: 
                new_map += self.map[_]
        self.map = new_map

    def move_right(self):
        '''Move to the right square if it is available and not blocked'''
        if ((maps.COLUMNS - 1) - self.player_location) % maps.COLUMNS == 0\
        and self.player_location is not 0:
            return False

        if self.map[self.player_location + 1] == '#':
            return False

        self.player_location += 1
        self.update_location()
        return True

    def move_left(self):
        '''Move to the left square if it is available and not blocked'''
        if self.player_location % maps.COLUMNS == 0:
            return False

        if self.map[self.player_location - 1] == '#':
            return False

        self.player_location -= 1
        self.update_location()
        return True

    def move_up(self):
        '''Move to the up square if it is available and not blocked'''
        if self.player_location < maps.COLUMNS:
            return False

        if self.map[self.player_location - maps.COLUMNS] == '#':
            return False

        self.player_location -= maps.COLUMNS
        self.update_location()
        return True

    def move_down(self):
        '''Move to the down square if it is available and not blocked'''
        if self.player_location >= (maps.ROWS-1) * maps.COLUMNS:
            return False

        if self.map[self.player_location + maps.COLUMNS] == '#':
            return False

        self.player_location += maps.COLUMNS
        self.update_location()
        return True

    def user_input(self, message):
        return input(message + "\nEnter here: ")

    def select_weapon(self, weapon=None):
        '''Choosing your weapon'''
        if weapon is not None:
            self.character.equip_weapon(weapon)
            return

        weapon_description =\
            "Now select your weapon. You can choose from:\n" +\
            "m - Mace (15 hp, 15 attack_power, 5spell_power, 5 armor)\n" +\
            "a - Axe (20 hp, 15 attack_power, 0 spell_power, 10 armor)\n" +\
            "d - Dagger (10 hp, 5 attack_power, 25 spell_power, 5 armor)\n" +\
            "s - Shield (25 hp, 5 attack_power, 5 spell_power, 40 armor)\n"
        user_input = self.user_input(weapon_description)
        if user_input == 'm':
            self.character.equip_weapon(Weapon(15, 15, 5, 5))
        elif user_input == 'a':
            self.character.equip_weapon(Weapon(20, 15, 0, 10))
        elif user_input == 'd':
            self.character.equip_weapon(Weapon(10, 5, 25, 5))
        elif user_input == 's':
            self.character.equip_weapon(Weapon(25, 5, 5, 40))
        else:
            self.character.equip_weapon(Weapon(10, 10, 10, 10))

    def select_character(self, character=None, weapon=None):
        '''Selecting your character'''
        if character is not None:
            self.character = character
            self.select_weapon(weapon)
            return
        class_description = "You must select your character now." + \
            " Choose between Mage, Warrior and Paladin\n" + \
            "Press m,w or p for each class"
        name_description = "Please enter your name"
        character_class = self.user_input(class_description)
        character_name = self.user_input(name_description)
        if character_class is 'p':
            self.character = Paladin(character_name)
        elif character_class is 'm':
            self.character = Mage(character_name)
        else:
            self.character = Warrior(character_name)
        self.select_weapon()

    def play(self, is_test=False):
        '''Playing the game untill you die or reach the treasure'''
        turn_description = "MOVE! Press: " + \
            "\nw - up\na - left\ns - down\nd - right\n"

        if is_test is False:
            self.select_character()
        user_input = ""

        while self.player_location != 49 and is_test is False:
            self.print_map()
            user_input = self.user_input(turn_description)
            if user_input == 'w':
                self.move_up()
            elif user_input == 's':
                self.move_down()
            elif user_input == 'a':
                self.move_left()
            elif user_input == 'd':
                self.move_right()
            else:
                continue
            self.print_map()
            luck = int(random.uniform(1, 4))
            if luck == 1:
                print ("You are very lucky and here are no enemies!\n" +
                    " You may continue your jorney!")
                continue
            elif luck == 2:
                print ("You will fight a warlock. Good luck!")
                fight = Battle(self.character, Warlock())
                fight.start()
                print (fight.result())
            elif luck == 3:
                print ("You will fight a berserker. Good luck!")
                fight = Battle(self.character, Berserker())
                fight.start()
                print (fight.result())

            if self.character.is_alive() == False:
                print ("You are dead.")
                return "You lost!"

        if self.player_location == 49 and is_test is False:
            print("You reached the goal. Now you will fight with boss")
            fight = Battle(self.character, Boss())
            fight.start()
            return (fight.result())
        else:
            print("You must have found a bug in the game. Congrats anyway!")

        return "You won!" if self.character.is_alive() else "You lost!"

