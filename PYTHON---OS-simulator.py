import os
import sys

# Simulated File System
class FileSystem:
    def __init__(self):
        self.files = {}

    def create_file(self, filename, content=""):
        if filename in self.files:
            print(f"Error: File '{filename}' already exists!")
        else:
            self.files[filename] = content
            print(f"File '{filename}' created.")

    def read_file(self, filename):
        if filename in self.files:
            print(f"Reading {filename}:")
            print(self.files[filename])
        else:
            print(f"Error: File '{filename}' not found!")

    def delete_file(self, filename):
        if filename in self.files:
            del self.files[filename]
            print(f"File '{filename}' deleted.")
        else:
            print(f"Error: File '{filename}' not found!")

# Simulated Task Manager
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def run_tasks(self):
        print("Running tasks...")
        for task in self.tasks:
            print(f"Executing task: {task}")
            eval(task)
        self.tasks.clear()

# OS Kernel Simulation
class SimpleOS:
    def __init__(self):
        self.file_system = FileSystem()
        self.task_manager = TaskManager()

    def display_help(self):
        print("Simple OS Commands:")
        print("1. create [filename] [content] - Create a file with optional content")
        print("2. read [filename] - Read a file")
        print("3. delete [filename] - Delete a file")
        print("4. task [operation] - Add a task (e.g., '2 + 2')")
        print("5. run - Run all tasks")
        print("6. exit - Exit the OS")

    def run(self):
        print("Welcome to Simple OS!")
        self.display_help()
        while True:
            command = input("\nOS> ").strip().split()

            if len(command) == 0:
                continue

            cmd = command[0].lower()

            if cmd == "create":
                if len(command) < 2:
                    print("Error: Filename required.")
                else:
                    filename = command[1]
                    content = " ".join(command[2:]) if len(command) > 2 else ""
                    self.file_system.create_file(filename, content)

            elif cmd == "read":
                if len(command) < 2:
                    print("Error: Filename required.")
                else:
                    filename = command[1]
                    self.file_system.read_file(filename)

            elif cmd == "delete":
                if len(command) < 2:
                    print("Error: Filename required.")
                else:
                    filename = command[1]
                    self.file_system.delete_file(filename)

            elif cmd == "task":
                if len(command) < 2:
                    print("Error: Task required.")
                else:
                    task = " ".join(command[1:])
                    self.task_manager.add_task(task)

            elif cmd == "run":
                self.task_manager.run_tasks()

            elif cmd == "exit":
                print("Shutting down Simple OS...")
                sys.exit()

            else:
                print(f"Unknown command: {cmd}")
                self.display_help()

# Run the OS simulation
if __name__ == "__main__":
    os_simulation = SimpleOS()
    os_simulation.run()
