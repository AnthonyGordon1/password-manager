import string
import getpass
import hashlib

password_manager = []

#TODO Refactor for a better function
def create_account(): 
    username = input("Enter your new username: ")
    password = getpass.getpass("Enter in your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully.")