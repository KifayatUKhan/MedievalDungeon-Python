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
'''
levelDict = {
    1 : {"Level" : 1, "Range" : range(0,10)},
    2 : {"Level" : 2, "Range" : range(10,20)},
    3 : {"Level" : 3, "Range" : range(20,30)},
}
'''

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
#   Snake
#   Hyena
#   Bear
# Select an Enemy
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

# Conditional Statments
#   If weapon matches -> kill -> get points
#   else -> fail -> no points
# Store the points in an external file

if userAttributes["WLevel"] >= userAttributes["ELevel"]:
    userAttributes["Points"] += 10
    print("Congrats! Your level of weapon matched the enemy level")
else:
    print("Sorry you LOST")

with open(fileDir, "w") as pointFile:
    pointFile.write(str(userAttributes["Points"]))

if userAttributes["Points"] == 30:
    print("You have reached the point. Delete the points file to reset")
    os.remove(fileDir)