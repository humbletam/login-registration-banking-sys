# Login/ Registration system 

# Global variables 
global username, password, name, user_choise


# Login startUp func which calls Login method outside registration method
# Need to refactor code/ add check sys for login if data is not found  
def Login_StartupOutside():

    print("Login process: ")

    # Count var for login attempts
    count = 0
    while count < 4:
        # New var for couting with data used var 
        username_log = input("Username: ")
        password_log = input("Password: ")

        if username_log == username and password_log == password:
            print("Access granted!")
            break
        else:
            print("Access denied! Try again")
            count += 1
    
# Registration func which calls Registration method 
def Registration_StartUp():
    # Login startUp func which calls Login method inside registration method 
    def Login_StartUpInside():

        print("Login process: ")

        # Count var for login attempts
        count = 0
        while count < 3:
            # New var for couting with data used var 
            username_log = input("Username: ")
            password_log = input("Password: ")

            if username_log == username and password_log == password:
                print("Access granted!")
                break
            else:
                print("Access denied! Try again")
                count += 1
    
    print("Registration process: ")

    username = input("Username: ")  
    password = input("Password: ")
    name = input("Enter your name: ")

    # This func checks if registration process passed or if failed returned the loop  
    if username and password and name != None:
        Login_StartUpInside()
    else:
        print("Registration process failed, try again...")
        Registration_StartUp()

       
# Basic function which calls a "Free-choise" 
def StartUp():

    print("Welcome!")
    # Integer value for user_choise
    user_choise = int(input("Sing in [1] or Sing up [2]: "))

    #User-choise check 
    if user_choise == 1:
        Login_StartupOutside()
    elif user_choise == 2:
        Registration_StartUp()
    else:
        print("Stand by...")


StartUp()