#  FILE SYSTEM
import os
from logger import log

BASE_DIR = "PyOs/data/files"
 
class FileSystem:

    # CREAT FILES
    def create_file(self , folder_path = BASE_DIR):     # BASE_DIR is defult path {data/files}, when we sent argument 
                                                        # folder_path = path. py replace BASE_DIR to path

        if not os.path.exists(folder_path):
            print("Folder path does not exist.")
            return

        # creat file = cf
        cf = input("\nEnter file name: ").strip()

        if "." not in cf:
            cf += ".txt"
        
        else:
            name , ext = cf.rsplit("." , 1)
            cf = name + "." + ext.lower()
        
        # blocked types:

        blocked = [".mp3" , ".mp4" , ".png" ,
                   ".jpg" , ".jpeg" , ".exe" , 
                   ".dll" , ".zip" , ".rar" , 
                   ".iso"]
        
        if any(cf.endswith(ext) for ext in blocked):
            print("Unsupported file type for this system.")
            return
        
        path = os.path.join(folder_path, cf)

        if os.path.exists(path):
            print("File already exists.\n")
            return

        lines = []

        while True:

            # file content = fc
            fc = input("Enter file content (type 'Q' to finish):  ").strip()
            
            if fc.upper() == "Q":
                break
            lines.append(fc)
        
        content = "\n".join(lines)

        with open(path , "w") as f:
            f.write(content)
        print("File created successfully.\n")

        log(f"File {cf} created in {folder_path}")

        return cf

    # READ FILES
    def read_file(self, cf):

        path = os.path.join(BASE_DIR, cf)

        if os.path.exists(path):
            with open(path, "r") as f:
                print(f.read())

            log(f"File {cf} read")

        else:
            print("File not found.\n")

    #  EDIT AVAILABLE FILES
    def edit_file(self , cf):

        path = os.path.join(BASE_DIR, cf)

        if os.path.exists(path):
            
            print("\nCurrent Content:\n")

            with open (path , "r") as f:
                print(f.read())
            
            # To add new lines
            lines = []

            while True:

                # file content = fc
                fc = input("Enter file content (type 'Q' to finish):  ").strip()

                if fc.upper() == "Q":
                    break
                lines.append(fc)

                if not lines:
                    print("No changes made.")

                    log (f"File edit cancelled ")

                    return          

            with open (path , "w") as f:
                f.write("\n".join(lines))
            
            print("File updated.\n")

            log(f"File {cf} updated.")

        else:
            print("File not found.\n")

    # DELETE FILES
    def delete_file(self, cf):

        path = os.path.join(BASE_DIR, cf)

        if os.path.exists(path):
            os.remove(path)
            print("File deleted.\n")

            log(f"File {cf} deleted")

        else:
            print("File not found.\n")

    # SHOW LIST OF FILES
    def list_file(self):

        if not os.listdir(BASE_DIR):
            print("No files to show")

            log ("No file found.")
            return
        
        print("\nFiles:")
        files = os.listdir(BASE_DIR)
        for i , file in enumerate(files , 1):
            print(f"{i}: {file}\n")

        log("File list viewed")

    # MAIN FILE SYSTEM MENU START FORM HERE
    def file_system_menu(self):

        cf = None

        
        while True:

            print("\n--- File System ---")
            print("1. Create File")
            print("2. Read File")
            print("3. Edit File")
            print("4. Delete File")
            print("5. List Files")
            print("6. Back")

            try:            # To avoid user wrong input
                choice = int(input("Choose an option (1-6): "))
            except ValueError:     # To void crashes
                print("Invalid choice type!\n")
                continue
            
            if choice == 1:
                self.create_file()

            elif choice == 2:
                file_name = input("\nEnter file name to read: ").strip()
                self.read_file(file_name)

            elif choice == 3:
                file_name = input("\n Enter file name to edit: ").strip()
                self.edit_file(file_name)

            elif choice == 4:
                
                file_name = input("\nEnter file name to delete: ").strip()
                confirm = input("Are you sure? (y/n): ").strip()
                if confirm.lower() != "y":
                    return
                self.delete_file(file_name)

            elif choice == 5:
                self.list_file()

            elif choice == 6:
                print("\nBack...")
                break

            else:
                print("Invalid choice type.\n")

fs = FileSystem()