# Will Anderson
# Will OS V. 1

import os

from commander import commander

def apprun():
    print("\n--------------------------------------------------")
    print("If you want a list of apps type list.")           
    app = input("\nApp: ")
    
    if app == "text":
        print("Opening Will Text...")
        os.system('python WillApps/WillText.py')

    elif app == "tunes":
        print("Opening Will Tunes...")
        os.system('python WillApps/WillTunes.py')

    elif app == "calculator":
        print("Opening Will calculator...")
        os.system('python WillApps/WillCalculator.py')

    elif app == "browser":
        print("Opening Will Browser...")
        os.system('python WillApps/WillBrowser.py')

    elif app == "file":
        print("Opening Will File...")
        os.system('python WillApps/WillFile.py')

    elif app == "alarm":
        print("Opening Will Alarm...")
        os.system('python WillApps/WillAlarm.py')

    elif app == "game":
        print("Opening Will Game...")
        os.system('python game.py')

    elif app == "list":
        print("\nHere is a list of Will Apps:")
        print("Text -A trusty text editor")
        print("Tunes -A pretty good way to feel the beat")
        print("Calculator -A simple trusty number machine")
        print("Browser -Want to surf, surf here")
        print("File -Lets explore your hard drive")
        print("Alarm -Time to wake up")
        print("Game -Want to play a game")

    elif app == "exit":
        commander()
        
    else:
        print("Not an app")
        apprun()
    print("--------------------------------------------------")
    apprun()
apprun()