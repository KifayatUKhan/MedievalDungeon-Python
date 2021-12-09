# Game Name: Medievel Dungeon
# Author: Kifayat Ullah Khan
# Created: Dec 07 2021
# Description: The user is provided with weapons Stick, Crossbow and Sword and has to kill an enemy, Snake, Hyena, and Bear. 
#              Weapons can kills specific enemies, upon selecting the right weapon , the user kills the enemy,
#              and by killing the enemy the user receives points.

import os

# Directory of file where user points will be stored after exiting game
# Or get points from when user opens the game
fileDir = r"D:\College\Programming\Final Project\UserPoints.txt"

# Where user's selected attributes will be saved
userAttributes = {"Weapon" : "", "Enemy" : "", "Level" : "", "ELevel" : "", "Points" : ""}

# -----------------------------------------------------------------------------------------------
# Function: onlyInt()
# Description: Identifies and catches Exception errors and reiterates the question
#              in order to get a valid input.
# Parameters:
#           ask: any string, or variable, to be shown in the input prompt
# Return value: 
#            inputVar: stores and returns the user entered value upon calling.
# -----------------------------------------------------------------------------------------------
def onlyInt(ask):
    inputVar = 0
    while True:
        try: 
            inputVar = int(input(ask))
            if not inputVar in range(1,4):
                raise Exception
            break
        except ValueError:
            print("Inavlid value Value- Enter an Integer")
            continue
        except Exception:
            print("Invalid- Enter # again!")
            continue
    return inputVar


# Opening points file and assigning points to a varibale
try:
    with open(fileDir, "r") as pointFile:
        userAttributes["Points"] = int(pointFile.read())
except FileNotFoundError:
    print("Points file not found - Points will be reset")
    userAttributes["Points"] = 0

# Assigning level to user based on points 1 level = 30
if userAttributes["Points"] == 0:
    userAttributes["Level"] = 0
elif userAttributes["Points"] > 0:
    userAttributes["Level"] = int(userAttributes["Points"] / 10)

print("Your level is {} ".format(userAttributes["Level"]))
print("You have {} Points".format(userAttributes["Points"]))

# Dict for Weapons
weaponDict = {
    1 : {"Weapon" : "Stick", "Level" : 0, "Strenght" : 2},
    2 : {"Weapon" : "Sword", "Level" : 1, "Strenght" : 6},
    3 : {"Weapon" : "Crossbow", "Level" : 2, "Strenght" : 8}
}

# Dict for Enemies
enemyDict = {
    1 : {"Enemy" : "Snake", "DestroyedBy" : "Stick", "Level" : 0},
    2 : {"Enemy" : "Hyena", "DestroyedBy" : "Sword", "Level" : 1},
    3 : {"Enemy" : "Bear", "DestroyedBy" : "Crossbow", "Level" : 2},
}

# Display Weapons Available
for level in weaponDict:
    if userAttributes["Level"] == weaponDict[level]["Level"]:
        userAttributes["Weapon"] = weaponDict[level]["Weapon"]
        userAttributes["WLevel"] = weaponDict[level]["Level"]
        print("Weapon available: {}".format(userAttributes["Weapon"]))

# Display Enemies
print("-"*15)
print("\n")
print("1: START GAME")
print("2: INVENTORY")
print("3: ABOUT")
print("\n")
print("-"*15)

# Menu options
startGame = 1
gameInventory = 2
aboutGame = 3

# Selction Menu Option and the further actions
while True:
    userOption = onlyInt(":> ")
    
    if userOption == startGame:
        for enemy in enemyDict:
            print("{} : {}".format(enemy, enemyDict[enemy]["Enemy"]))

        while True:
            userInput = int(input("Choose Enemy [1-3]: "))
            if userInput in enemyDict:
                userAttributes["Enemy"] = enemyDict[userInput]["Enemy"]
                userAttributes["ELevel"] = enemyDict[userInput]["Level"]
                break
            else: 
                continue
    elif userOption == gameInventory:
        print("-"*15)
        print("\n")
        print("YOUR LEVEL: {} ".format(userAttributes["Level"]))
        print("{:<10s} {:<10s} {:<10s}".format("LEVEL", "WEAPON", "ENEMY"))
        for enemy in enemyDict:
            print("{:<10} {:<10} {:<10}".format(enemyDict[enemy]["Level"], weaponDict[enemy]["Weapon"], enemyDict[enemy]["Enemy"]))
        print("An upper level weapon can kill lower level enemies")
        print("\n")
        print("-"*15)
        print("[1] Start Game,  [2] Inventory, [3] About")
        print("-"*15)
        continue
    elif userOption == aboutGame:
        print("-"*15)
        print("\n")
        print("HI,")
        print("In this game you have to kill enemy according to your level")
        print("If you guess your enemy level according to your level, you kill it")
        print("When you kill it, you get 10 points, and reach new level")
        print("or you get killed, if you don't select the right level enemy")
        print("\n")
        print("-"*15)
        print("[1] Start Game,  [2] Inventory, [3] About")
        print("-"*15)
        
        continue
    else:
        print("WRONG INPUT")
            
    break

# If User level matches or is greater than the enemy level, the user wins, otherwise lose.
if userAttributes["WLevel"] >= userAttributes["ELevel"]:
    userAttributes["Points"] += 10
    print("Congrats! Your level of weapon matched the enemy level")
else:
    print("Sorry you LOST")

# Write points to the user points file
with open(fileDir, "w") as pointFile:
    pointFile.write(str(userAttributes["Points"]))

# Reset the points, if reach the max. points.
if userAttributes["Points"] == 30:
    print("You have reached the point. Delete the points file to reset")
    os.remove(fileDir)