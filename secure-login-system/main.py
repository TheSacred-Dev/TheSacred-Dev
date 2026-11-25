#Sacred Dev

import time

print("\n===============Welcome to the Secure Login System===============")
print("You have 3 attempts to log in. Please enter your credentials\n")

# Variables
username = "Python"
password = "CompSci10"
attempts = 0
max_attempts = 3

# Loop Mechanism
while attempts < max_attempts:
    attempts += 1
    attempts_left = max_attempts - attempts

    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    if entered_username == username and entered_password == password:
        print("\nAccess granted.\nWelcome to the secure system!")
        exit()
    else:
        if attempts >= max_attempts:
            print("\nYou have exceeded the maximum number of login attempts.")
            print("\nRetry login in 24 hours or contact our support team.")
            print("Locking terminal in ...")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("Terminal locked.")
            exit()
        else:
            print(f"""\nIncorrect username or password. 
{attempts_left} Attempt(s) Left, Please try again.\n""")
