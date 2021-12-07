# Game Name: Medievel Dungeon
# Author: Kifayat Ullah Khan
# Created: Dec 07 2021
# Description: The user is provided with weapons Stick, Crossbow and Sword and has to kill an enemy, Snake, Hyena, and Bear. 
#              Weapons can kills specific enemies, upon selecting the right weapon , the user kills the enemy,
#              and by killing the enemy the user receives points.

# Levels
#   Level 1 -> 0-10 points
#   Level 2 -> 10-20
#   level 3 -> 20-30
userPoints = 0
levelOne = range(0,10)
levelTwo = range(10,20)
levelThree = range(20,30)

print("You have {} Points".format(userPoints))

# Class for Weapons
#   Stick 
#       Level 1
#       strenght -> 2
#   Sword 
#       Level 2
#       strenght -> 6
#   Crossbow 
#       Level 3
#       strenght -> 8
class Weapons:

    def __init__(self, name, level, strenght):
        self.name = name
        self.level = level
        self.strenght = strenght

stick = Weapons("Stick", 1, 2)
sword = Weapons("Sword", 2, 6)
crossbow = Weapons("Crossbow", 3, 8)

# Class for Enemies
#   Snake 
#       Killed by Stick, Sword
#       Points -> 10
#   Hyena 
#       Killed by Crossbow, Sword
#       Points -> 10
#   Bear 
#       Killed by Crossbow
#       Points -> 10
class Enemies:
    points = 10

    def __init__(self, name, weapon1, weapon2):
        self.name = name
        self.weapon1 = weapon1
        self.weapon2 = weapon2

snake = Enemies("Snake", "Stick", False)
hyena = Enemies("Hyena", "Sword", "Crossbow")
hyena = Enemies("Bear", "Crossbow", False)

# Display Weapons Available
#   If Points
#       Points 0-10 -> Stick
#       Points 10-20 -> Sword
#       Points 20-30 -> Crossbow
# Input for Selection
if userPoints in levelOne:
    print("Weapon: {}\nLevel: {}\nStrenght: {} ".format(stick.name, stick.level, stick.strenght))
elif userPoints in levelTwo:
    print("Weapon: {}\nLevel: {}\nStrenght: {} ".format(stick.name, stick.level, stick.strenght))
    print("Weapon: {}\nLevel: {}\nStrenght: {} ".format(sword.name, sword.level, sword.strenght))
elif userPoints in levelThree:
    print("Weapon: {}\nLevel: {}\nStrenght: {} ".format(stick.name, stick.level, stick.strenght))
    print("Weapon: {}\nLevel: {}\nStrenght: {} ".format(sword.name, sword.level, sword.strenght))
    print("Weapon: {}\nLevel: {}\nStrenght: {} ".format(crossbow.name, crossbow.level, crossbow.strenght))
else:
    print(" You have WON the Game. No More Playing")


# Display Enemies
#   Snake
#   Hyena
#   Bear
# Select an Enemy

# Conditional Statments
#   If weapon matches -> kill -> get points
#   else -> fail -> no points
# Store the points in an external file
