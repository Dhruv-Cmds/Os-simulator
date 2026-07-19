# Python OS Simulator

A terminal-based operating system simulator built with **pure Python**.
This project demonstrates core programming concepts such as **Object-Oriented Programming, file handling, system simulation, and modular architecture** without relying on external frameworks.

The simulator mimics basic operating system components including **user authentication, file management, process handling, and memory simulation**.

---

## Overview

The goal of this project is to simulate how a simple operating system manages different subsystems.
Instead of focusing on UI or frameworks, the emphasis is on **core logic, system design, and clean code structure**.

This project was built as a learning exercise to strengthen understanding of:

* Python fundamentals
* OOP design
* Modular programming
* State management
* File-based persistence

---


## Screenshots

### System Start
![System Start](screenshots/01_system_start_menu.png)

### Main Menu
![Main Menu](screenshots/03_login_success_main_menu.png)

### File System
![File System](screenshots/04_file_system_menu_and_creat_file.png)

### Folder Manager
![Folder Manager](screenshots/23_folder_manager_menu.png)

### Process Manager
![Process Manager](screenshots/9_process_manager_menu.png)

### Memory Manager
![Memory Manager](screenshots/14_memory_manager_menu.png)

### Terminal 
![Terminal Mode](screenshots/terminal.png)

### System Logs
![Logs](screenshots/20_view_system_logs.png)


## Features

* **User Authentication**

  * Register and login system
  * Persistent user storage

* **File System Simulation**

  * Create virtual files
  * Read stored file content
  * Delete files
  * List available files

* **Process Manager**

  * Simulate running processes
  * Assign process IDs (PID)
  * View active processes
  * Terminate processes

* **Memory Manager**

  * Simulate memory allocation
  * Track used and free memory
  * Deallocate memory

* **Create Folder**

  * Create folder
  * Open fodler
  * Delete fodler
  * List folder

* **System Logging**

  * Track important system events
  * User login activity
  * File operations
  * Process actions

## Shell Commands

```bash
ls                     # list files
mkdir <folder_name>    # create folder
touch <file>           # create file
touch <folder/file>    # create file inside folder
rm <file>              # delete file
rm <folder/file>       # delete file inside folder
```

## System Commands

```bash
help
about
system_info
uptime
clear
exit
```

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Dhruv-Cmds/Python-os-simulator.git
   ```
   
2. Navigate into the project directory:
  ```bash
  cd Python-os-simulator
  ```
3. Run the program:
  python main.py

---

## Project Structure

```
python-os-simulator/
│
├── core/
│   ├── cmd.py
│   ├── file_system.py
│   ├── folder.py
│   ├── logger.py
│   ├── Main.py
│   ├── memory.py
│   ├── pos.py
│   ├── process.py
│
├── data/
│   │ └── files/
│   └── player/
│         └─ main.py
│   ├── files.json
│   ├── logs.txt
│   ├── test.txt
│   └── users.txt
│
│
├── screenshots
│
├── .gitattributes
├── .gitignore
├──  LICENSE
└── README.md
```

Each module is responsible for a specific subsystem of the simulated OS.

---

## How It Works

When the program starts, users are presented with a login/register interface.
After authentication, the main system menu allows interaction with various simulated OS components.

The simulator uses **file-based storage** to persist data between sessions.

---

## Example Usage

```
====================================
        PYTHON OS
====================================

1. Login
2. Register
3. Exit

Enter choice: 1

Login successful!

Main Menu
1. File System
2. Creat Folder
3. Process Manager
4. Memory Manager
5. View Logs
6. Terminal
7. Logout
```

---

## Technologies Used

* Python 3
* Object-Oriented Programming
* File Handling
* JSON / Text Storage

No external libraries or frameworks were used.

---

---

## Changelog

### v1.2.0

New Features
- Added terminal commands (about, uptime, system_info)
- Improved command terminal usability

Improvements
- Better system interaction through command interface

### v1.1.0
- Introduced Folder Manager (create, open, delete folders)
- Enabled file creation inside folders
- Improved modular interaction between folder and file system
- Stability improvements and bug fixes

### v1.0.1
- Fixed login validation
- Fixed process manager edge case
- Improved memory manager safety

### v1.0.0
- Initial release
- File system
- Process manager
- Memory manager
- Logging

---

## Author

Dhruv

