# Will Anderson
# Will OS V. 1

import sys
import os

from setup import setup
from login import login
from app import apprun

# Commander
def commander():
    while True: 
        print("\n--------------------------------------------------")
        print("Will OS Commander")
        print("Type 'help' for help.")

        command = input("\nWill OS>> ")

        # Command Checker

        # Help
        if command == "help":
            print("Opening Will OS Help...")
            print("\nHere are some commands for Will OS: ")
            print("Exit - Closes Will OS")
            print("Settings - Opens Settings for  Will OS")
            print("Reset -Wipe Will OS")
            print("Lock -Locks Will OS")
            print("About -Learn all about Will OS")
            print("App -Want to run a application")

        # Exit
        elif command == "exit":
            print("Closing Will OS...")
            break

        # Settings
        elif command == "settings":
            print("Opening Will OS Settings...")
            setup()

        # Reset
        elif command == "reset":
            print("Opening Reset...")
            print("Type password to verify reset.")
            login()
            with open("data.txt", "w") as f:
                f.close()

        # Lock
        elif command == "lock":
            print("Locking...")
            login()

        # About
        elif command == "about":
            print("Opening About Will OS...")
            print("Will OS V.1 is a unix based sub-operating system for python developers.")
            print("V. 1 was created by my a 11 year old python programer with dreams for my future.")
            print("Hope you like it :-).")

        # App
        elif command == "app":
            apprun()

        else:
            print("Not a command.")

