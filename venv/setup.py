# Will Anderson
# Will OS V. 1

import sys



# This is our main function and it's purpose is to get data to store in the users info.txt document.
def setup():
    # We need to make the users age and birthday know globally throughout this file.
    try:

        # Info for SignUp
        print("\n--------------------------------------------------")
        print("Glad you are here, let's get you set up.")
        print("First you will need to enter some personal info.\nYou can trust us to never use this info.")
        print("--------------------------------------------------")

        # Filling out the data
        print("\n--------------------------------------------------")
        name = input("What is your name?: ")
        password = input("What do you want to make your password?: ")
        password_confirmation = input("Type your password again: ")
        print("--------------------------------------------------")

        # Confirming the data
        if password_confirmation == password:
            print("\n--------------------------------------------------")
            confirm = input("\nSo... "
                            + "\nYour username is: " + name
                            + "\nYou want your password to be: " + password
                            + "\nCorrect (yes/no): ").lower()
            print("--------------------------------------------------")

            # If you confirm the data we need to put the data in the data.txt file.
            if confirm == "yes":
                with open("data.txt", "w") as f:
                    f.write(name)
                    f.write("\n" + password)

                    # This will close Will OS.
                    print("You are done just close this window or press any key and open Will OS again.")
                    input()
                    sys.exit()

            # If they do not confirm restart the process.
            else:
                setup()
        else:
            print("You did not type the same password twice please fill out again.")
            setup()

    # If something goes wrong with the setup.
    except Exception as e:
        print("Something went wrong with setting up Will OS... Error: {}.".format(e))
        print("Restarting...")
        setup()
