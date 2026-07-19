import pos
import time
from logger import log

# PROJECT START FROM HERE
class Start:

    def start_os(self):

        l = pos.l

        print("Booting Python OS...")
        time.sleep(1)
        print("Loading file system...")
        time.sleep(1)
        print("Loading memory manager...")
        time.sleep(1)
        print("System ready.\n")

        print("==============================")
        print("           PYTHON OS          ")
        print("==============================")

        log("Python OS started")

        while True:

            #  Main programs start form here
            print("1. Login")
            print("2. Register")
            print("3. Exit")

            try:            # To avoid user wrong input
                choice = int(input("Choose an option (1-3): "))
            except ValueError: # To void crashes
                print("Invalid choice type!\n")
                continue

            if(choice == 1):

                log("Login option selected")
                l.login()

            elif(choice == 2):

                log("Register option selected")
                username , password = l.register()
                l.login()
            
            elif(choice == 3):
                print("\nBye!")
                log("Python OS closed")
                break

            else:
                print("Invalid choice.\n")

s = Start()
s.start_os()