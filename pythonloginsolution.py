# Login/ Registration system 

# Global variables 
global username, password, name, user_choise

# New credentials as Admin in Login sys
username_admin = "sunflower"
password_admin = "1000101"
name_admin = "Rustam"

# Standard credentials as User in Login sys
username_user = "user"
password_user = "123456"
name_user = "User"

# Login startUp func which calls Login method outside registration method
# Need to refactor code/ add check sys for login if data is not found  
def Login_StartupOutside():

    print("Login process: ")

    # Count var for login attempts
    count = 0
    while count < 3:
        # New var for couting with data used var 
        username_log = input("Username: ")
        password_log = input("Password: ")

        # Login verification procces
        # Sys checks if premade user inputs his credentials right - in that case: Premade user got access to the sys
        if username_log == username_user and password_log == password_user:
            print("Access granted! Welcome "+ name_user)
            break
        # Sys checks who is in a sys - in that case: Admin correctly inputs this credetntials 
        elif username_log == username_admin and password_log == password_admin:
            print("Access granted! Admin panel... Welcome "+ name_admin)
            break
        # If username is incorrect - Access denied - user have 2 more tries 
        elif username_log != username_admin and username_log != username_user:
            print("Access denied! Incorrect username, try again...")
            count += 1
        # If password incorrect - Access denied - user have 2 more tries     
        else:
            print("Access denied! Password incorrect, try again...")
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

            # Sys checks if user inputs his credentials right - in that case: User got access to the sys
            if username_log == username and password_log == password:
                print("Access granted! Welcome "+ name )
                break
            # Sys checks if premade user inputs his credentials right - in that case: Premade user got access to the sys
            elif username_log == username_user and password_log == password_user:
                print("Access granted! Welcome "+ name_user)
                break
            # Sys checks who is in a sys - in that case: Admin correctly inputs this credetntials 
            elif username_log == username_admin and password_log == password_admin:
                print("Access granted! Admin panel... Welcome "+ name_admin)
                break
            # If username is incorrect - Access denied - user have 2 more tries
            elif username_log != username_admin and username_log != username_user and username_log != username:
                print("Access denied! Incorrect username, try again...")
                count += 1
            # If password incorrect - Access denied - user have 2 more tries
            else:
                print("Access denied! Password incorrect, try again...")
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
    # String value for user_choise
    user_choise = input("Sing in [1] or Sing up [2]: ")

    #User-choise check 
    if user_choise == "1":
        Login_StartupOutside()
    elif user_choise == "2":
        Registration_StartUp()
    elif user_choise == None:
        print("Stand by...")
    else:
        print("Stand by...")


StartUp()