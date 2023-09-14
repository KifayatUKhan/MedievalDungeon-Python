# Game Name: Medieval Dungeon
# Author: Kifayat Ullah Khan
# Created: Dec 07, 2021
# Description: The user is provided with weapons Stick, Crossbow and Sword and has to kill an enemy, Snake, Hyena, and Bear. 
#              Weapons can kills specific enemies, upon selecting the right weapon, the user kills the enemy,
#              and by killing the enemy the user receives points.

import os

# Directory of file where user points will be stored after exiting game
# Or get points from when user opens the game
fileDir = r"D:\College\Programming\Final Project\UserPoints.txt"

# Directoty for txt file where the already rewarded enemies list will be stored
listFile = r"D:\College\Programming\Final Project\RewardedEnemies.txt"

# Where user's selected attributes will be saved
userAttributes = {"Weapon" : "", "Enemy" : "", "Level" : "", "ELevel" : "", "Points" : ""}

# -----------------------------------------------------------------------------------------------
# Function: onlyInt()
# Description: Identifies and catches Exception errors and reiterates the question
#              in order to get a valid input.
# Parameters:
#           ask: any string, or variable, to be shown in the input prompt
#           range (range): sets a range, where it only accept value within the range, otherwise an error
# Return value: 
#            inputVar: stores and returns the user entered value upon calling.
# -----------------------------------------------------------------------------------------------
def onlyInt(ask, range):
    inputVar = 0
    while True:
        try: 
            inputVar = int(input(ask))
            if not inputVar in range:
                raise Exception
            break
        except ValueError:
            print("Invalid value Value - Enter an Integer")
            continue
        except Exception:
            print("Invalid- Enter # again!")
            continue
    return inputVar

# -----------------------------------------------------------------------------------------------
# Function: greetMenu()
# Description: Greets the user to the Game and Informs of basic flow of the game. 
#              Shows the user's points and current weapon based on the level and prints out the Menu for user.
# Parameters:
#           weapon (Dict): refers to the dictionary where weapon's information are stored.
#           user (Dict): refers to the dictionary where details of the user are stored. i.e. Level, Points, Weapon etc.
# -----------------------------------------------------------------------------------------------
def greetMenu(weapon, user):
    print("\n")
    print("---------------------- WELCOME TO MEDIEVEL DUNGEON ------------------------")
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
    inlineOutput += "[1] Start Game, [2] My Inventory, [3] Cheat Sheet, [4] About"
    inlineOutput += "\n"
    inlineOutput += "-"*40
    print(inlineOutput)

# -----------------------------------------------------------------------------------------------
# Function: startGameFunc()
# Description: Runs when the user selects "Start Game" from the Menu. Performs the main gaming function of the program.
#              Shows the user the enemies list, and if the user gets it correct, 10 pts are added to user's point file.
#              If user gets the answer wrong, 2 more tries are given, if still get wrong answer, the program shut down.
# Parameters:
#           user (Dict) : refers to the dictionary where details of the user are stored. i.e., Level, Points, Weapon etc.
#           enemy (Dict) : refers to the dictionary where enemy's information are stored. i.e., Name, level etc.
#           eList (List) : a list where the already rewarded enemies are stored, so that user is not rewarded twice for the same enemy
# -----------------------------------------------------------------------------------------------
def startGameFunc(user, enemy, eList):
    while True:
        print("-"*40)
        print("WPN: {:<11} LVL: {:<10} PTS: {:>2}".format(user["Weapon"], user["Level"], user["Points"] ))
        print("-"*40)

        for e in enemyDict:
            print("{} : {}".format(e, enemy[e]["Enemy"]))
        print("-"*40)
        
        # Variable for the current chance number, to try again if wrong answer.
        uChance = 1

        # If there are chances left keep looping
        while uChance <= 3:
            userInput = onlyInt("Choose Enemy [1-3]: ", range(1,7))

            if userInput in enemy:
                # If User level is greater than zero, then open the file where the already rewarded enemy list is
                # This is so that the user cannot be rewarded for a single enemy twice
                if user["Level"] > 0:
                    with open(listFile, "r") as enemyRewarded:
                        eList = enemyRewarded.read().split(",")

                user["ELevel"] = enemy[userInput]["Level"]

                if not enemy[userInput]["Enemy"] in eList:
                    # If the new enemy is not in already rewarded list, add it to the list
                    with open(listFile, "w") as enemyRewarded:
                        enemyRewarded.write("{},".format(enemy[userInput]["Enemy"]))

                    eList = enemy[userInput]["Enemy"]
                    # If User level matches or is greater than the enemy level, the user wins, otherwise lose.
                    if user["WLevel"] >= user["ELevel"]:
                        user["Points"] += 10
                        print("-"*40)
                        print("WELL DONE! YOU DEFENDED AGAINST THE ENEMY")
                        print("POINTS: {}".format(user["Points"]))
                        print("-"*40)
                        break
                    # If user gets it wrong
                    else:
                        print("-"*40)
                        print("You DIED!")
                        if uChance < 3:
                            print("Don't Worry! You still have {} Chance(s)".format(3-uChance))
                        uChance = uChance + 1
                        print("-"*40)
                        continue
                # Show this message if points for an enemy is already collected.
                elif enemy[userInput]["Enemy"] in eList:
                    print("\n")
                    print("Sorry! You have already been rewarded on this Enemy. Select New")
                    print("You can keep your chances though")
                    print("\n")
                    continue
            else: 
                continue
        break

# -----------------------------------------------------------------------------------------------
# Function: myInventoryFunc()
# Description: Runs when the user selects "My Inventory" from the Menu. Lists the weapons the user has, by means of level.
# Parameters:
#           weapon (Dict): refers to the dictionary where weapon's information are stored. i.e., Name of Weapon, Level.
#           user (Dict): refers to the dictionary where details of the user are stored. i.e., Level, Points, Weapon etc.
# -----------------------------------------------------------------------------------------------
def myInventoryFunc(weapon, user):
    print("Your Weaponry\n")
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
#           user (Dict): refers to the dictionary where details of the user are stored. i.e. Level, Points, Weapon etc.
#           enemy (Dict): refers to the dictionary where enemy's information are stored. i.e Name, level etc.
# -----------------------------------------------------------------------------------------------
def gameCheatFunc(user, enemy):
    print("-"*40)
    print("YOUR LEVEL: {} ".format(user["Level"]))
    print("\n")
    print("{:<10s} {:<10s} {:<10s}".format("ENEMY", "LEVEL", "WEAPON(s) TO DEFEND BY"))

    for e in enemy:
        print("{:<10} {:<10} {:<10}".format( enemy[e]["Enemy"], enemy[e]["Level"], enemy[e]["Weapon"]))
    print("\n")
    print("An Upper level weapon can defend against lower level enemies")
    inlineMenu()

# -----------------------------------------------------------------------------------------------
# Function: aboutGameFunc()
# Description: Runs when the user selects "About" from the Menu. Shows someinformation to teach the user.
#              Details about the game, and how it is played.
# -----------------------------------------------------------------------------------------------
def aboutGameFunc():
    print("-"*40)
    print("\n")
    print("Hi,")
    print("In this game you have to kill enemy according to your level")
    print("There are 3 levels, each level has its weapons, and set of enemies")
    print("You are assingned a weapon based on your level.")
    print("What you have to do is guess the enemy which can be defended by your Weapon")
    print("If you have Stick, it can depend against Snake, so If you select Snake, you will get 10 points.")
    print("When you get points, you upgrade to new level, with an upgraded weapon.")
    print("If you get it Wrong, you have 2 more Chances to get it Correct")
    print("If you still fail to get the correct enemy, you will DIE without any points")
    print("NOTE: You will not be rewarded twice for an already guessed enemy")
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
    1 : {"Weapon" : "Stick", "Level" : 0},
    2 : {"Weapon" : "Spearhead", "Level" : 1},
    3 : {"Weapon" : "Sword", "Level" : 2}
}

# Dict for Enemies
enemyDict = {
    1 : {"Enemy" : "Snake", "Weapon" : "Stick, Spearhead, Sword", "Level" : 0},
    2 : {"Enemy" : "Hyena", "Weapon" : "Spearhead, Sword", "Level" : 1},
    3 : {"Enemy" : "Bear", "Weapon" : "Spearhead", "Level" : 2},
    4 : {"Enemy" : "Alligator", "Weapon" : "Spearhead, Sword", "Level" : 1},
    5 : {"Enemy" : "Lion", "Weapon" : "Spearhead", "Level" : 2},
    6 : {"Enemy" : "Scorpion", "Weapon" : "Stick, Spearhead, Sword", "Level" : 0},
}

# List where already rewarded enemy list will be stored, 
eList = []

greetMenu(weaponDict, userAttributes)
# Menu options
startGame = 1
myInventory = 2
gameCheat = 3
aboutGame = 4

# Selection Menu Option and the further actions
while True:
    userOption = onlyInt(":> ", range(1,5))

    # Starts the game
    if userOption == startGame:
        startGameFunc(userAttributes, enemyDict, eList)
        break
    # Shows theuser's Weaponary
    elif userOption == myInventory:
        myInventoryFunc(weaponDict, userAttributes)
        continue
    # Shows a list of enemy's, and weapon's level to win the game
    elif userOption == gameCheat:
        gameCheatFunc(userAttributes, enemyDict)
        continue
    # Provides more information about the Game
    elif userOption == aboutGame:
        aboutGameFunc()
        continue
    else:
        print("Invalid Input - Try again! ")
        inlineMenu()
            
    break

# Write points to the user points file
with open(fileDir, "w") as pointFile:
    pointFile.write(str(userAttributes["Points"]))

# Reset the points, and rewarded list if reach the max. 30 points.
if userAttributes["Points"] == 30:
    print("You Reached 30 Points. The Points will reset now")
    print("-"*40)
    os.remove(listFile)
    os.remove(fileDir)