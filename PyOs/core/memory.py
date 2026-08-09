# MEMORY MANAGER
from logger import log

class Memory:

    def __init__ (self , memory_limit = 1024):

        # fix memory size to stop memory overflow
        self.memory_limit = memory_limit
        self.total_memory = memory_limit
        self.memory = {}

    # allocate memory to process
    def allocate_memory (self):

        process = input("\nEnter process name: ").strip()

        if process in self.memory:
            print("Process already exists.")
            
            log(f"Memory allocation failed: {process} already exists")

            return

        # allocate memory in MB formate = amb
        while True:
            try:
                amb = int(input("Enter amount to allocate (MB): "))

                if amb <= 0:
                    print("Memory must be greater than 0.\n")
                    log(f"Memory allocation failed for {process}: invalid amount {amb}")
                    continue

                if amb > self.memory_limit:
                    print("Insufficient memory.\n")
                    log(f"Memory allocation failed for {process}: insufficient memory request {amb}MB")
                    continue

            except ValueError:
                print("Invalid (MB) type!\n")
                log("Memory allocation failed: invalid MB input")
                continue
            break
        
        # retrun available memory after procees took
        self.memory_limit -= amb

        #  give waring to user
        if self.memory_limit < 200:
            print("Warning: Low memory!\n")

            log("Low memory warning triggered")
        
        self.memory[process] = amb
        print(f"{amb} MB allocated to {process}.\n")

        log(f"{amb}MB allocated to process {process}")

        return amb

    # free memory from porcess
    def free_memory(self):

        process = input("\nEnter process name to free memory: ").strip()

        if process == "":
            print("Invalid process name.\n")
            return

        if not self.memory:
            print("No memory to free.\n")
            log("Memory free attempted but no processes exist")
            return
        
        # free space from memory = fmb
        if process in self.memory:
            freed = self.memory.pop(process)

            # return memory form process after end
            self.memory_limit += freed

            print(f"{freed} MB freed from {process} successfully.\n")

            log(f"{freed}MB memory freed from process {process}")
        
        else:
            print("Process not found.\n")

            log(f"Memory free failed: process {process} not found")

    # show memory usage from task
    def show_current_memory (self):

        total_memory = self.total_memory
        used_memory = sum(self.memory.values())
        free_memory = total_memory - used_memory
        usage_percentage = (used_memory / total_memory) * 100

        print(f"\nTotal Memory: {total_memory} MB")
        print(f"Used Memory: {used_memory} MB")
        print(f"Free Memory: {free_memory} MB")
        print(f"Memory Usage: {usage_percentage:.2f}%")

        log("Memory status viewed")

        if not self.memory:
            print("\nNo processes using memory.")
            return

        print("\nCurrent Memory Usage:")

        for process, mb in self.memory.items():
            print(f"{process} -> {mb} MB")
    
    # main memory menu
    def memory_menu (self):


        while True:

            print ("\n--- Memory Manager ---")
            print("1. Allocate Memory")
            print("2. Free Memory")
            print("3. Show current Memory")
            print("4. Back")

            try:            # To avoid user wrong input
                choice = int(input("\nChoose an option (1-4): "))
            except ValueError:      # To void crashes
                print("Invalid choice type!\n")
                log("Invalid memory menu input type")
                continue

            if choice == 1:
                self.allocate_memory()

            elif choice == 2:
                self.free_memory()

            elif choice == 3:
                self.show_current_memory()

            elif choice == 4:
                print("\nBack...\n")
                break

            else:
                print("Invalid choice type.\n")
                log("Invalid memory menu choice entered")

m = Memory()