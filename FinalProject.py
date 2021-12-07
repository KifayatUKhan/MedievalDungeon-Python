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

# Dict for Weapons
#   Stick 
#       Level 1
#       strenght -> 2
#   Sword 
#       Level 2
#       strenght -> 6
#   Crossbow 
#       Level 3
#       strenght -> 8
weaponDict = {
    1 : {"Weapon" : "Stick", "Level" : 1, "Strenght" : 2},
    2 : {"Weapon" : "Sword", "Level" : 2, "Strenght" : 6},
    3 : {"Weapon" : "Crossbow", "Level" : 3, "Strenght" : 8}
}

# Dict for Enemies
#   Snake 
#       Killed by Stick, Sword
#       Points -> 10
#   Hyena 
#       Killed by Crossbow, Sword
#       Points -> 10
#   Bear 
#       Killed by Crossbow
#       Points -> 10
enemyDict = {
    1 : {"Enemy" : "Snake", "DestroyedBy" : "Stick"},
    2 : {"Enemy" : "Hyena", "DestroyedBy" : "Sword"},
    3 : {"Enemy" : "Bear", "DestroyedBy" : "Crossbow"},
}

# Display Weapons Available
#   If Points
#       Points 0-10 -> Stick
#       Points 10-20 -> Sword
#       Points 20-30 -> Crossbow
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

# Input for Weapon Selection
while True:
    weaponSelect = int(input("Enter Weapon#: "))

    if weaponSelect == 1:
        userWeapon = stick
        break
    elif weaponSelect == 2:
        userWeapon = sword
        break
    elif weaponSelect == 3:
        userWeapon = crossbow
        break
    else:
        print("Wrong Input - Enter again")
        continue


# Display Enemies
#   Snake
#   Hyena
#   Bear
# Select an Enemy
for enemies in Enemies:


# Conditional Statments
#   If weapon matches -> kill -> get points
#   else -> fail -> no points
# Store the points in an external file
