# Will Anderson
# 4/12/2021
# Will OS Main

# We are going to need to import some things...
import datetime

# Importations from other files in Will OS
from setup import setup
from login import login
from commander import commander

import time
import sys


def loding():
    print("Loding...")

    toolbar_width = 40

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(0.1)  # do real work here
        # update the bar
        sys.stdout.write("#")
        sys.stdout.flush()

    sys.stdout.write("]\n")  # this ends the progress bar

loding()

# This is going to be a welcome to Will OS and it will have the date that the program was started.
print("\n--------------------------------------------------")
print("Welcome To Will OS")
print("The Unix Based Sub-Operating System")
now = datetime.datetime.now()
print("\nTime and Date: ")
print(now.strftime('%H:%M on %A, %B the %dth, %Y'))
print("--------------------------------------------------")


try:
    with open("data.txt", "r") as f:
        content = f.readlines()
        name = content[0]
        password = content[1]

except:
    print("You need to setup Will OS")
    setup()

login()


# Here we will sort out the users so that they get logged in to the info or make a new account.
# Entering email and password and verifying them using info.txt
print("\n--------------------------------------------------")
print("Welcome to Will OS")
print("You are logged in as " + name.rstrip())
print("--------------------------------------------------")

print("\n--------------------------------------------------")
print("Will OS Commander")
print("Type 'help' for help.")

while True:
    commander()

input("Type any key  to exit...")
