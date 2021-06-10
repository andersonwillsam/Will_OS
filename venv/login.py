# Will Anderson
# Will OS V. 1

# Login
def login():
    with open("data.txt", "r") as f:
        content = f.readlines()
        name = content[0].rstrip()
        password = content[1]

        def get_password():
            print("Type your password to login if you forgot type reset: ")
            typed_password = input()
            if typed_password == password:
                name.rstrip()
                print("Logged in... ")

            elif typed_password == "reset":
                def reset_password(): 
                    print("\nType your name to reset password.")
                    typed_name = input()
                    if typed_name == name:
                        def get_new_password():
                            print("\nNow type your new password twice.")
                            new_password = input("Password: ")
                            new_password_confirmation = input("Confirm Password: ")
                            
                            if new_password_confirmation == new_password:
                                with open("data.txt", "w") as f:
                                    f.write(name)
                                    f.write("\n" + new_password)

                            else:
                                print("\nNot same password type again.")
                                get_new_password()
                        get_new_password()
               
                    else:
                        print("\nNot your name...")
                        reset_password()
                reset_password()
    
            else:
                print("Wrong Password...")
                get_password()
        get_password()