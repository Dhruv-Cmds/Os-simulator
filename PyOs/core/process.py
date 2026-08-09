# PROCESS MANAGER
from logger import log

class ProcessManager:

    def __init__ (self):
        self.processes = []
        self.next_pid = 1000

    # process start from here
    def start_process(self , sp):
        
        process = {
            "pid" : self.next_pid,
            "sp" : sp               # start process name = sp
        }

        self.processes.append(process)
        print(f"Process started with PID {self.next_pid}\n")

        log(f"Process {sp} started with PID {self.next_pid}")

        self.next_pid += 1

    # process kill from here
    def kill_process(self , pid):
        
        if not self.processes:
            print("No processes to kill.\n")
            return
        
        for p in self.processes:
            if p['pid'] == pid:
                self.processes.remove(p)
                print(f"Process {p['sp']} terminated.\n")

                log(f"Process {p['sp']} with PID {pid} terminated")

                return
            
        print("Process not found.\n")
        log(f"Kill process failed: PID {pid} not found")

    # view process from here
    def view_running_task(self):
        
        if not self.processes:
            print("No running processes.\n")
            return
        
        print(f"\nRunning Processes ({len(self.processes)}):")
        for p in self.processes:
            print(f"PID {p['pid']} - {p['sp']}")

    # manage all task form here
    def process_manager(self):
        

        while True:
            
            print("\n--- Process Manager ---")
            print("1. Start Process")
            print("2. Kill Process")
            print("3. View Running Processes")
            print("4. Back")

            try:            # To avoid user wrong input
                choice = int(input("Choose an option (1-4): "))
            except ValueError:     # To void crashes
                print("Invalid choice type!\n")
                continue

            if choice == 1:

                # start process name = sp
                sp = input("\nEnter process name: ").strip()
                self.start_process(sp)
            
            elif choice == 2:

                # to prevent unknown user input
                while True:
                    try:
                        pid = int(input("\nEnter PID to kill: "))
                    except ValueError:
                        print("Invalid PID.")
                        continue
                    break

                self.kill_process(pid)

            elif choice == 3:
                self.view_running_task()

            elif choice == 4:
                print("\nBack...")
                break
            
            else:
                print("Invalid choice type.\n")

p = ProcessManager()