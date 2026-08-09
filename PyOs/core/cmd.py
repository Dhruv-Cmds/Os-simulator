import os
import time
from logger import log
import file_system
import process
import memory
import folder

class Terminal:
        # ---------------- TERMINAL HELP ---------------- #

    def show_help(self):

        print("\nAvailable Commands:\n")

        print("Shell Commands:")
        print(" ls")
        print(" mkdir <folder_name>")
        print(" touch <folder/file_name>")
        print(" rn <file_name>\n")

        print("File System:")
        print(" create_file")
        print(" read_file")
        print(" edit_file")
        print(" delete_file")
        print(" list_files")

        print("\nFolder System:")
        print(" create_folder")
        print(" open_folder")
        print(" delete_folder")
        print(" list_folder")

        print("\nMemory Manager:")
        print(" allocate_memory")
        print(" free_memory")
        print(" show_memory")

        print("\nProcess Manager:")
        print(" start_process")
        print(" kill_process")
        print(" view_process")

        print("\nSystem:")
        print(" view_logs")
        print(" help")
        print(" exit\n")


    # ---------------- TERMINAL MODE ---------------- #

    def run_terminal(self):

        start_time = time.time()

        fs = file_system.fs
        p = process.p
        m = memory.m
        fo = folder.fo

        print("\nMini OS Simulator Terminal")
        print("Type 'help' to see commands\n")
        print("Type 'clear' to clear Terminal\n")
        print("Type 'system_info' to check system information\n")
        print("Type 'about' to check about program information\n")
        print("Type 'uptime' to check OS run time\n")

        while True:

            command = input("OS> ").strip()

            parts = command.split()
            cmd = parts[0] if parts else ""
            args = parts[1:]

            if command == "help":
                self.show_help()

            # ---------------- FILE SYSTEM ---------------- #

            elif command == "create_file":
                fs.create_file()

            elif command == "read_file":
                file = input("Enter file name: ").strip()
                fs.read_file(file)

            elif command == "edit_file":
                file = input("Enter file name: ").strip()
                fs.edit_file(file)

            elif command == "delete_file":
                file = input("Enter file name: ").strip()
                fs.delete_file(file)

            elif command == "list_files":
                fs.list_file()

            # ---------------- FOLDER SYSTEM ---------------- #

            elif command == "create_folder":
                fo.create_folder()

            elif command == "open_folder":
                fo.open_folder()

            elif command == "delete_folder":
                fo.delete_folder()

            elif command == "list_folder":
                fo.list_folder()

            # ---------------- MEMORY SYSTEM ---------------- #

            elif command == "allocate_memory":
                m.allocate_memory()

            elif command == "free_memory":
                m.free_memory()

            elif command == "show_memory":
                m.show_current_memory()

            # ---------------- PROCESS SYSTEM ---------------- #

            elif command == "start_process":
                
                name = input("Enter process name: ").strip()
                p.start_process(name)

            elif command == "kill_process":

                try:
                    pid = int(input("Enter PID: "))

                    p.kill_process(pid)
                    
                except ValueError:
                    print("Invalid PID")

            elif command == "view_process":
                p.view_running_task()


            # ---------------- LINUX STYLE COMMANDS ---------------- #

            #  ls = check list of files
            elif cmd == "ls":

                fs.list_file()

                log (f" File list viewd via shell command")
            
            #  mkdir = to creat folder
            elif cmd == "mkdir":
                
                if args:

                    folder_name = args[0]

                    path  = os.path.join("data" , folder_name)

                    if not os.path.exists(path):
                        os.mkdir(path)

                        print(f"Folder '{folder_name}' created.")

                        log (f"Folder '{folder_name}' created via shell command")
                    
                    else:
                        print("Folder already exists.")
            
            # touch = craet files
            elif cmd == "touch":

                if args:

                    file_path = args[0]

                    #  make path data/foldername/file.txt
                    path = os.path.join("data" , file_path)

                    folder_name = os.path.dirname(path)

                    #  folder exist check

                    if folder_name and not os.path.exists(folder_name):
                        print("Folder does not exist.")
                        return

                    with open (path , "w") as f:
                        pass

                    print(f"File '{file_path}' created.")

                    log (f"File '{file_path}' created via shell command")

                else:
                    fs.create_file()

            #  rm = delete files
            elif cmd == "rm":

                if args:

                    file_path = args[0]

                    # direct path support (data/file.txt)
                    path = os.path.join("data", file_path)

                    if os.path.exists(path):

                        os.remove(path)

                        print(f"File '{file_path}' removed.")

                        log(f"File {file_path} deleted via shell command")

                    else:

                        # recursive search
                        found = False

                        for root, dirs, files in os.walk("data"):

                            if file_path in files:

                                full = os.path.join(root, file_path)

                                os.remove(full)

                                print(f"File '{file_path}' removed from {root}")

                                log(f"File {file_path} deleted from {root} via shell command")

                                found = True
                                break

                        if not found:
                            print("File not found.")

                else:
                    name = input("Enter file name: ").strip()
                    fs.delete_file(name)

            # ---------------- LOG SYSTEM ---------------- #

            elif command == "view_logs":

                try:

                    with open("data/logs.txt") as f:

                        print(f.read())

                except FileNotFoundError:

                    print("No logs found.")

            elif command == "exit":

                print("Shutting down OS...")

                break

            # ---------------- OS SHORT-CUTS ---------------- #

            elif command == "clear":

                os.system("cls" if os.name == "nt" else "clear")
            
            elif command == "system_info":

                print("\n=== System Information ===")
                print("OS Name: Python OS Simulator")
                print("Version: 1.1.0")
                print("Language: Python")
                print("Modules Loaded:")
                print("- File System")
                print("- Folder Manager")
                print("- Memory Manager")
                print("- Process Manager")
                print("- Logger")
                print("- Command Terminal")
                print("===========================\n")
            
            elif command == "about":

                print("\n=== About Python OS ===")
                print("Python OS Simulator")
                print("Version: 1.3.0")
                print("Built using Python")
                print("Architecture: Modular CLI System")
                print("Modules:")
                print("- File System")
                print("- Folder Manager")
                print("- Memory Manager")
                print("- Process Manager")
                print("- Logger")
                print("- Command Terminal")
                print("=======================\n")
            
            elif command == "uptime":

                print(f"Uptime: {round(time.time() - start_time,2)} seconds")

            else:
                print("Unknown command. Type 'help'")

tml = Terminal()