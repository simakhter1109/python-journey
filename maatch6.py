username = input("Enter username: ")
password = input("Enter password: ")

correct_username = "simakhter11"
correct_password = "diya@1109"

match (username == correct_username, password == correct_password):
    
    case (True, True):
        print("Login Successful!")
    case (False, True):
        print("Incorrect Username.")
    case(True, False):
        print("Incorrect password.")
    case(False, False):
        print("Invalid Username and Password.")
        