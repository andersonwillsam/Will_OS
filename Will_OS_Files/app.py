# Will Anderson
# Will OS V. 1

import os

from game import gamerun

def apprun():
    while True:
        print("\n--------------------------------------------------")
        print("If you want a list of apps type list.")           
        app = input("\nApp: ")
        
        if app == "text":
            print("Opening Will Text...")
            os.system('python WillApps/WillText.py')
            apprun()

        elif app == "tunes":
            print("Opening Will Tunes...")
            os.system('python WillApps/WillTunes.py')
            apprun()

        elif app == "calculator":
            print("Opening Will calculator...")
            os.system('python WillApps/WillCalculator.py')
            apprun()

        elif app == "browser":
            print("Opening Will Browser...")
            os.system('python WillApps/WillBrowser.py')
            apprun()

        elif app == "file":
            print("Opening Will File...")
            os.system('python WillApps/WillFile.py')
            apprun()

        elif app == "alarm":
            print("Opening Will Alarm...")
            os.system('python WillApps/WillAlarm.py')
            apprun()

        elif app == "game":
            print("Opening Will Game...")
            gamerun()
            break


        elif app == "list":
            print("\nHere is a list of Will Apps:")
            print("Text -A trusty text editor")
            print("Tunes -A pretty good way to feel the beat")
            print("Calculator -A simple trusty number machine")
            print("Browser -Want to surf, surf here")
            print("File -Lets explore your hard drive")
            print("Alarm -Time to wake up")
            print("Game -Want to play a game")
            apprun()

        elif app == "exit":
            print("--------------------------------------------------")
            break
            
        else:
            print("Not an app")
            apprun()
        print("--------------------------------------------------")
        