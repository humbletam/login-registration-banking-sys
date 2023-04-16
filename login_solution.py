# New credentials as Admin in Login sys
username_admin = "sunflower"
password_admin = "1000101"
name_admin = "Rustam"

def LoginProcces():
    print("Login process: ")

# Count var for login attempts

    count = 0
    while count < 3:
        loginSolution_login = input("Login: ")
        loginSolution_passwd = input("Password: ")

# Login verification procces
# Sys checks if premade user inputs his credentials right - in that case: Premade user got access to the sys        
        if loginSolution_login == username_admin and loginSolution_passwd == password_admin:
            print("Access granted! Welcome "+ name_admin)
            break
        elif loginSolution_login != username_admin and loginSolution_passwd != password_admin:
            print("Access denied! Incorrect username, try again...")
            count += 1
LoginProcces()