# Game Name: Medievel Dungeon
# Author: Kifayat Ullah Khan
# Created: Dec 07 2021
# Description: The user is provided with weapons Stick, Crossbow and Sword and has to kill an enemy, Snake, Hyena, and Bear. 
#              Weapons can kills specific enemies, upon selecting the right weapon , the user kills the enemy,
#              and by killing the enemy the user receives points.
fileDir = r"D:\College\Programming\Final Project\UserPoints.txt"
try:
    with open(fileDir, "r") as pointFile:
        userPoints = int(pointFile.read())
except FileNotFoundError:
    print("Points file not found - Points will be reset")
    userPoints = 0


userAssets = {"Weapon" : "", "Enemy" : "", "Level" : "", "ELevel" : "",}
# Levels
#   Level 1 -> 0-10 points
#   Level 2 -> 10-20
#   level 3 -> 20-30

levelDict = {
    1 : {"Level" : 1, "Range" : range(0,10)},
    2 : {"Level" : 2, "Range" : range(10,20)},
    3 : {"Level" : 3, "Range" : range(20,30)},
}
for x in levelDict:
    if userPoints in levelDict[x]["Range"]:
        userAssets["Level"] = levelDict[x]["Level"]
print(userAssets["Level"])
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
    1 : {"Enemy" : "Snake", "DestroyedBy" : "Stick", "Level" : 1},
    2 : {"Enemy" : "Hyena", "DestroyedBy" : "Sword", "Level" : 2},
    3 : {"Enemy" : "Bear", "DestroyedBy" : "Crossbow", "Level" : 3},
}

# Display Weapons Available
#   If Points
#       Points 0-10 -> Stick
#       Points 10-20 -> Sword
#       Points 20-30 -> Crossbow
for level in weaponDict:
    if userPoints in levelDict[level]["Range"]:
        print("Weapon available: {}".format(weaponDict[level]["Weapon"]))
        userAssets["Weapon"] = weaponDict[level]["Weapon"]
        userAssets["Level"] = levelDict[level]["Level"]


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
        userAssets["Enemy"] = enemyDict[userInput]["Enemy"]
        userAssets["ELevel"] = enemyDict[userInput]["Level"]
        break
    else: 
        continue

# Conditional Statments
#   If weapon matches -> kill -> get points
#   else -> fail -> no points
# Store the points in an external file

if userAssets["Level"] == userAssets["ELevel"]:
    userPoints += 10
    print("Congrats! Your level of weapon matched the enemy level")
else:
    print("Sorry you LOST")

with open(fileDir, "w") as pointFile:
    pointFile.write(str(userPoints))

if userPoints == 30:
    print("You have reached the point. Delet the points file to reset")