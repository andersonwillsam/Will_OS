# Will Anderson
# Will OS V. 1

import os
import sys

# Commander
def gamerun():
    print("\n--------------------------------------------------")
    print("Type list for list of games.")
    game = input("\nGame: ")
    
    if game == "baseball":
        print("Opening Baseball...\n--------------------------------------------------\n")
        os.system('python WillGames/Baseball/Main.py')
        gamerun()
    elif game == "chaty":
        print("Opening Chaty...\n--------------------------------------------------\n")
        os.system('python WillGames/Chaty/Chaty.py')
        gamerun()
    elif game == "colorgame":
        print("Opening Color Game...\n")
        os.system('python WillGames/ColorGame/ColorGame.py')
        gamerun()
    elif game == "screenpet":
        print("Opening Screen Pet...\n")
        os.system('python WillGames/ScreenPet/ScreenPet.py')
        gamerun()    

    elif game == "snake":
        print("Opening Snake...\n")
        os.system('python WillGames/Snake/Snake.py')
        gamerun()
    
    elif game == "spaceinvaders":
        print("Opening SpaceInvaders...\n")
        os.system('python WillGames/SpaceInvaders/SpaceInvaders.py')
        gamerun()

    elif game == "list":
        print("\nList of Will Games:")
        print("Baseball -A simulatin baseballgame")
        print("Chaty -A really chaty robot to talk to")
        print("ColorGame -A brain twister of colors")
        print("Racer -On your marks get set havefun")
        print("ScreenPet -A good homework buddy")
        print("Snake -Eat the food not your self")
        print("SpaceInvaders -Protect the galexy from glatic invaders")
        gamerun()

    elif game == "exit":
        os.system('python commander.oy')
        
    else:
        print("Not an game")
        gamerun()
    print("--------------------------------------------------")
            