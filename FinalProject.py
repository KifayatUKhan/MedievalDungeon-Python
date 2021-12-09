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
            if not inputVar in range(1,5):
                raise Exception
            break
        except ValueError:
            print("Inavlid value Value- Enter an Integer")
            continue
        except Exception:
            print("Invalid- Enter # again!")
            continue
    return inputVar

# -----------------------------------------------------------------------------------------------
# Function: greetMenu()
# Description: Greets the user to the Game, and Informs of basic flow of the game. 
#              Shows the user's points and current weapon based on the level, and prints out the Menu for user.
# Parameters:
#           weapon (Dict) : refers to the dictionary where weapon's informations are stored.
#           user (Dict) : refers to the dictionary where details of the user are stored. i.e. Level, Points, Weapon etc.
# -----------------------------------------------------------------------------------------------
def greetMenu(weapon, user):
    print("\n")
    print("---------------------- WELCOME TO MEDIEVEL MAZE ------------------------")
    print("TO WIN YOU HAVE TO GUESS THE CORRECT ENEMY BASED ON YOUR CURRENT WEAPON.")
    print("--------------------- SELECT 'ABOUT' FOR MORE INFO ---------------------")
    print("------------------- OR 'CHEAT SHEET' FOR ENEMY LEVELS ------------------")
    print("------------------------------------------------------------------------")

    # Display current Weapon, Level and Points of the User.
    for level in weapon:
        if user["Level"] == weapon[level]["Level"]:
            user["Weapon"] = weapon[level]["Weapon"]
            user["WLevel"] = weapon[level]["Level"]
            print("WEAPON: {:<23} LEVEL: {:<22} POINTS: {:>2}".format(user["Weapon"], user["Level"], user["Points"] ))

    # Display Menu
    print("\n")
    print("1: START GAME")
    print("2: MY INVENTORY")
    print("3: CHEAT SHEET")
    print("4: ABOUT")
    print("-"*40)

# -----------------------------------------------------------------------------------------------
# Function: inlinemenu()
# Description: shows menu options when in an individual page.
# -----------------------------------------------------------------------------------------------
def inlineMenu():
    inlineOutput = "-"*40
    inlineOutput += "\n"
    inlineOutput += "[1] Start Game,  [2] My Inventory, [3] Cheat Sheet, [4] About"
    inlineOutput += "\n"
    inlineOutput += "-"*40
    print(inlineOutput)

# -----------------------------------------------------------------------------------------------
# Function: startGameFunc()
# Description: Runs when the user selects "Start Game" from the Menu. Performs the main gaming function of the program.
#              Shows th user the enemies list, and if the user gets it correct, 10 pts are added to user's point file.
#              If user gets the answer wrong, 2 more tries are given, if still get wrong answer, the programs shuts
# Parameters:
#           user (Dict) : refers to the dictionary where details of the user are stored. i.e. Level, Points, Weapon etc.
#           enemy (Dict) : refers to the dictionary where enemy's informations are stored. i.e Name, level etc.
# -----------------------------------------------------------------------------------------------
def startGameFunc(user, enemy):
    while True:
        print("-"*40)
        print("WPN: {:<11} LVL: {:<10} PTS: {:>2}".format(user["Weapon"], user["Level"], user["Points"] ))
        print("-"*40)

        for e in enemyDict:
            print("{} : {}".format(e, enemy[e]["Enemy"]))
        
        # Variable for the current chance number, to try again if wrong answer.
        uChance = 1
        while uChance <= 3:
            userInput = int(input("Choose Enemy [1-3]: "))

            if userInput in enemy:
                user["Enemy"] = enemy[userInput]["Enemy"]
                user["ELevel"] = enemy[userInput]["Level"]

                # If User level matches or is greater than the enemy level, the user wins, otherwise lose.
                if user["WLevel"] >= user["ELevel"]:
                    user["Points"] += 10
                    print("-"*40)
                    print("WELL DONE! YOU ESCAPED THE ROOM")
                    print("POINTS: {}".format(user["Points"]))
                    print("-"*40)
                    break
                else:
                    print("-"*40)
                    print("You DIED!")
                    if uChance < 3:
                        print("Don't Worry! You still have {} Chance(s)".format(3-uChance))
                    uChance = uChance + 1
                    print("-"*40)
                    continue
            else: 
                continue
        break

# -----------------------------------------------------------------------------------------------
# Function: myInventoryFunc()
# Description: Runs when the user selects "My Inventoy" from the Menu. Lists the weapons the user has, by means of level.
# Parameters:
#           weapon (Dict) : refers to the dictionary where weapon's informations are stored. i.e Name of Weapon, Level.
#           user (Dict) : refers to the dictionary where details of the user are stored. i.e. Level, Points, Weapon etc.
# -----------------------------------------------------------------------------------------------
def myInventoryFunc(weapon, user):
    print("Your Weaponary\n")
    for level in weapon:
        if user["Level"] >= weapon[level]["Level"]:
            print("'{}' acquired from Level {}".format(weapon[level]["Weapon"], weapon[level]["Level"]))
            print("\n")
    inlineMenu()

# -----------------------------------------------------------------------------------------------
# Function: gameCheatFunc()
# Description: Runs when the user selects "Game Cheat" from the Menu. Lists the details about Weapons, and Enemies.
#              Which weapon(s) can defend against which enemy is listed here, so this is basically a cheat sheet.
# Parameters:
#           user (Dict) : refers to the dictionary where details of the user are stored. i.e. Level, Points, Weapon etc.
#           enemy (Dict) : refers to the dictionary where enemy's informations are stored. i.e Name, level etc.
# -----------------------------------------------------------------------------------------------
def gameCheatFunc(user, enemy):
    print("-"*40)
    print("\n")
    print("YOUR LEVEL: {} ".format(user["Level"]))
    print("{:<10s} {:<10s} {:<10s}".format("ENEMY", "LEVEL", "WEAPON TO DEFEND BY"))

    for e in enemy:
        print("{:<10} {:<10} {:<10}".format( enemy[e]["Enemy"], enemy[e]["Level"], enemy[e]["Weapon"]))
    print("An upper level weapon can kill lower level enemies")
    inlineMenu()

# -----------------------------------------------------------------------------------------------
# Function: aboutGameFunc()
# Description: Runs when the user selects "Game Cheat" from the Menu. Lists the details about Weapons, and Enemies.
#              Which weapon(s) can defend against which enemy is listed here, so this is basically a cheat sheet.
# Parameters:
#           user (Dict) : refers to the dictionary where details of the user are stored. i.e. Level, Points, Weapon etc.
#           enemy (Dict) : refers to the dictionary where enemy's informations are stored. i.e Name, level etc.
# -----------------------------------------------------------------------------------------------
def aboutGameFunc():
    print("-"*40)
    print("\n")
    print("HI,")
    print("In this game you have to kill enemy according to your level")
    print("If you guess your enemy level according to your level, you kill it")
    print("When you kill it, you get 10 points, and reach new level")
    print("or you get killed, if you don't select the right level enemy")
    inlineMenu()

# Opening points file and assigning points to a varibale
try:
    with open(fileDir, "r") as pointFile:
        userAttributes["Points"] = int(pointFile.read())
except FileNotFoundError:
#    print("MESSAGE: User Points file not found - Points will be reset to 0")
    userAttributes["Points"] = 0

# Assigning level to user based on points 1 level = 30
if userAttributes["Points"] == 0:
    userAttributes["Level"] = 0
elif userAttributes["Points"] > 0:
    userAttributes["Level"] = int(userAttributes["Points"] / 10)

# Dict for Weapons
weaponDict = {
    1 : {"Weapon" : "Stick", "Level" : 0, "Strenght" : 2},
    2 : {"Weapon" : "Spearhead", "Level" : 1, "Strenght" : 6},
    3 : {"Weapon" : "Sword", "Level" : 2, "Strenght" : 8}
}

# Dict for Enemies
enemyDict = {
    1 : {"Enemy" : "Snake", "Weapon" : "Stick, Spearhead, Sword", "Level" : 0},
    2 : {"Enemy" : "Hyena", "Weapon" : "Spearhead, Sword", "Level" : 1},
    3 : {"Enemy" : "Bear", "Weapon" : "Spearhead", "Level" : 2},
    4 : {"Enemy" : "Alligator", "Weapon" : "Spearhead, Sword", "Level" : 1},
    5 : {"Enemy" : "Lion", "Weapon" : "Spearhead", "Level" : 2},
    5 : {"Enemy" : "Scorpion", "Weapon" : "Stick, Spearhead, Sword", "Level" : 0},
}

greetMenu(weaponDict, userAttributes)
# Menu options
startGame = 1
myInventory = 2
gameCheat = 3
aboutGame = 4

# Selction Menu Option and the further actions
while True:
    userOption = onlyInt(":> ")

    if userOption == startGame:
        startGameFunc(userAttributes, enemyDict)
        break
    elif userOption == myInventory:
        myInventoryFunc(weaponDict, userAttributes)
        continue
    elif userOption == gameCheat:
        gameCheatFunc(userAttributes, enemyDict)
        continue
    elif userOption == aboutGame:
        aboutGameFunc()
        continue
    else:
        print("WRONG INPUT")
        inlineMenu()
            
    break

# Write points to the user points file
with open(fileDir, "w") as pointFile:
    pointFile.write(str(userAttributes["Points"]))

# Reset the points, if reach the max. points.
if userAttributes["Points"] == 30:
    print("You Reached 30 Points. The Points will reset now")
    print("-"*40)
    os.remove(fileDir)