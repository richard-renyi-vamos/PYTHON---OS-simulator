import os
import shutil

def show_help():
    print("""
SimplePyOS Commands:
---------------------
help               Show this help menu
ls                 List files in current directory
cd <dir>           Change directory
mkdir <dir>        Create a new directory
rm <file/dir>      Delete a file or directory
create <file>      Create a new empty file
edit <file>        Edit file (append text)
read <file>        Display contents of a file
calc               Open calculator
exit               Exit the OS
""")

def calculator():
    print("Welcome to PyOS Calculator! Type 'exit' to quit.")
    while True:
        expr = input("calc> ")
        if expr.lower() == 'exit':
            break
        try:
            print("Result:", eval(expr))
        except Exception as e:
            print("Error:", e)

def main():
    print("🧠 Welcome to SimplePyOS - Python Shell Simulation 🐍")
    show_help()

    while True:
        cmd = input("PyOS> ").strip()
        if not cmd:
            continue

        parts = cmd.split()
        command = parts[0]
        args = parts[1:]

        if command == "help":
            show_help()

        elif command == "ls":
            for item in os.listdir():
                print("📁" if os.path.isdir(item) else "📄", item)

        elif command == "cd":
            if not args:
                print("❌ Please specify a directory.")
            else:
                try:
                    os.chdir(args[0])
                    print("✅ Changed directory to", os.getcwd())
                except Exception as e:
                    print("❌ Error:", e)

        elif command == "mkdir":
            if not args:
                print("❌ Please specify a folder name.")
            else:
                try:
                    os.mkdir(args[0])
                    print("📁 Directory created:", args[0])
                except Exception as e:
                    print("❌ Error:", e)

        elif command == "rm":
            if not args:
                print("❌ Please specify a file or directory to remove.")
            else:
                path = args[0]
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    print("🗑️ Directory removed:", path)
                elif os.path.isfile(path):
                    os.remove(path)
                    print("🗑️ File removed:", path)
                else:
                    print("❌ No such file or directory:", path)

        elif command == "create":
            if not args:
                print("❌ Please specify a file name.")
            else:
                with open(args[0], 'w') as f:
                    pass
                print("📄 File created:", args[0])

        elif command == "edit":
            if not args:
                print("❌ Please specify a file name.")
            else:
                with open(args[0], 'a') as f:
                    print("✏️ Type text (type 'SAVE' to save and exit):")
                    while True:
                        line = input()
                        if line.upper() == "SAVE":
                            break
                        f.write(line + "\n")
                print("✅ Changes saved.")

        elif command == "read":
            if not args:
                print("❌ Please specify a file name.")
            else:
                try:
                    with open(args[0], 'r') as f:
                        print("📄 Contents of", args[0])
                        print(f.read())
                except Exception as e:
                    print("❌ Error:", e)

        elif command == "calc":
            calculator()

        elif command == "exit":
            print("👋 Exiting PyOS. Goodbye!")
            break

        else:
            print("❌ Unknown command:", command)

if __name__ == "__main__":
    main()
