import hashlib
import getpass

user_accounts = {}

def register_user():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_accounts[username] = hashed_password
    print("Account successfully created!")

def authenticate_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    if username in user_accounts and user_accounts[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def run_program():
    while True:
        action = input("Press 1 to register, 2 to log in, or 0 to exit: ")
        
        if action == "1":
            register_user()
        elif action == "2":
            authenticate_user()
        elif action == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_program()
