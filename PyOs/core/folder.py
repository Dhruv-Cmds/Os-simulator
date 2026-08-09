# FOLDER SYSTEM
import os
import file_system
from logger import log

# Folder path where all folder goes
BASE_DIR = "PyOs/data"

class Folder:

    # CREAT NEW FOLDER
    def create_folder(self):
      
        # creat folder = cl
        cl = input("\nEnter folder name to create: ").strip()

        if cl == "":
            print("Invalid folder name.")
            return
        
        path = os.path.join(BASE_DIR , cl) 

        if os.path.exists(path):
            print("Folder already exists.\n")
            return
        
        os.mkdir(path)

        print(f"Folder '{cl}' created successfully.\n")

        log(f"Folder {cl} created")
    
    # OPEN EXSISTING FOLDER
    def open_folder(self):

        fs = file_system.fs
        
        # opne folder = of 

        of = input("\nEnter folder name to open: ").strip()

        # join join data/{foldername} so path will become one full path data/foldername
        path = os.path.join(BASE_DIR , of)

        if not os.path.exists(path):

            print("Folder not found.\n")

            log(f"Folder path not found")
            return
        
        if not os.path.isdir(path):
            print("This is not a folder\n")
            return 

        print(f"Entered folder: {of}")

        print(f"Path: {path}")

        log(f"Entered folder {of}")

        while True:

            print("1. Create File in this Folder")
            print("2. Back...")

            choice = input("Choose option: ").strip()

            if choice == "1":
                # we are sending path which contain one argument path and path contain Base_DIR/{foldername}
                # bc we creat folder here base_DIR/{foldername} this will pass to creat_file. We are sharing one argument only.
                fs.create_file(path)

            elif choice == "2":
                print("2. Back...")
                break

            else:
                print("Invalid choice.\n")
    
    #  TO DELETE EXISTING FOLDER
    def delete_folder(self):
        
        #  delete folder  = df
        df = input("\nEnter folder name to delete: ").strip()

        path = os.path.join(BASE_DIR, df)

        if not os.path.exists(path):
            print("Folder not found.\n")

            log(f"Folder not found")
            return
        
        if not os.path.isdir(path):
            print("This is not a folder.\n")
            
            log (f"Invalid folder name")
            return

        #  shutil used to delete folder + files
        import shutil
        shutil.rmtree(path)

        print(f"Folder '{df}' deleted.\n")

        log(f"Folder {df} deleted")

    # SHOW All FOLDER
    def list_folder(self):

        # list of all folders = laf
        laf = os.listdir(BASE_DIR)

        for folder in laf:
            if os.path.isdir(os.path.join(BASE_DIR , folder)):
                print(f"[DIR] {folder}")
            else:
                print(f"[FILE] {folder}")
        
        log("Folder list viewed")
    
    def folder_menu (self):

        while True:

            print("\n--- Folder Manager ---")
            print("1. Creat Folder")
            print("2. Open Folder")
            print("3. Delete Folder")
            print("4. List Folder")
            print("5. Back")

            try:            # To avoid user wrong input
                choice = int(input("Choose an option (1-5): "))
            except ValueError:     # To void crashes
                print("Invalid choice type!\n")
                continue

            if choice == 1:
                self.create_folder()

            elif choice == 2:
                self.open_folder()

            elif choice == 3:
                self.delete_folder()

            elif choice == 4:
                self.list_folder()

            elif choice == 5:
                print("Back...")
                break
                
            else:
                print("Invalid choice type.\n")

fo = Folder()