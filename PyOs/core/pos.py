import file_system
import process
import memory
import folder
import cmd
from logger import log

class Login:

    def __init__(self): 
        self.current_user = None

    # LOGIN
    def login(self):
        
        while True: 
            username = input("\nEnter username: ").strip()

            if username == "":
                print("Invalid username.")
                continue

            password = input("Enter 4-digit password: ")

            if len(password) != 4 or not password.isdigit():
                print("Wrong password! Try again.")
                continue     

            try:
                with open("PyOs/data/users.txt" , "r") as f:
                    for line in f:
                        parts = line.strip().split(":") 
                        if len(parts) != 2: 

                            continue 

                        u , p = parts 

                        if u == username and p == password:
                            print("Login successful!")
                            print(f"Welcome, {username}\n")
                            
                            self.current_user = username

                            log(f"User {username} logged in")
                            
                            # to call main menu from here automatically
                            self.main_menu()
                            return
                        
            except FileNotFoundError:
                print("No users registered yet.")
                return

            print("Invalid username or password.")
            log(f"Failed login attempt for {username}")

    # REGISTER USER
    def register(self):

        while True:

            print("\n--- Register User ---") 
            
            username = input("Enter username: ").strip()

            if username == "":
                print("Invalid username.")
                continue

            try:
                with open("PyOs/data/users.txt") as f:
                    for line in f:
                        parts = line.strip().split(":")  
                        if len(parts) != 2: 
                            continue 

                        u, _ = parts 

                        if u == username:
                            print("Username already exists.")
                            return
            except FileNotFoundError:
                pass

            password = input("Enter 4-digit password: ")
            confirm_password = input("Confirm password: ")

            if len(password) != 4 or password != confirm_password or not password.isdigit():
                print("Wrong password! Try again.")
                continue 

            with open("PyOs/data/users.txt" , "a") as f:
                f.write(f"{username}:{password}\n")

            print("User created successfully!\n")
            print("Redirecting to login...\n")

            log(f"New user registered: {username}")
                
            break

        return username , password

    # MAIN MENU RUN AFTER COMPLETE LOGIN
    def main_menu(self):

        fs = file_system.fs
        p = process.p
        m = memory.m
        fo = folder.fo
        tml = cmd.tml

        print("==============================")
        print("           Main Menu          ")
        print("==============================")

        while True:
            
            print ("\n--- Main Task Manager ---")
            print("1. File System")
            print("2. Creat Folder")
            print("3. Process Manager")
            print("4. Memory Manager")
            print("5. View Logs")
            print("6. Terminal Mode")
            print("7. Logout")

            try:
                choice = int(input("Choose an option (1-7): "))
            except ValueError:
                print("Invalid choice type!")
                continue

            if choice == 1:
                fs.file_system_menu()

            elif choice == 2:
                fo.folder_menu()

            elif choice == 3:
                p.process_manager()

            elif choice == 4:
                m.memory_menu()

            elif choice == 5:

                print("\n--- System Logs ---")

                try:
                    with open("PyOs/data/logs.txt") as f:
                        print(f.read())
                except FileNotFoundError:
                    print("No logs found.")
     
            elif choice == 6:
                tml.run_terminal()

            elif choice == 7:
                print("Logged out.")
                log(f"User {self.current_user} logged out")
                break

            else:
                print("Invalid choice.")

l = Login()