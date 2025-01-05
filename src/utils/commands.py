from utils.operations import ShellOperations
from utils.navigation import ShellNavigation
from utils.styles import Info, Color

class CommandHandler:
    def __init__(self):
        self.ops = ShellOperations()
        self.nav = ShellNavigation()

    def execute(self, command: str):
        if command == "exit":
            print(f"{Color.Green}Exiting Shell. Goodbye!{Color.Reset}")
            exit()
        elif command == "clear":
            self.ops.clear_screen()
        elif command == "--version":
            Info.show_version()
        elif command == "help":
            Info.show_help()

        elif command in ["ls", "list"]:
            self.nav.list_items()
        elif command == "pwd":
            print(f"Current Working Directory: {self.nav.current_path}")            
        elif command.startswith("mkdir "):
            dir_name = command.replace("mkdir ", "").strip()
            self.ops.create_directory(dir_name)
        elif command.startswith("rmdir "):
            dir_name = command.replace("rmdir ", "").strip()
            self.ops.remove_directory(dir_name)
        elif command.startswith("rm -r "):
            dir_name = command.replace("rm -r ", "").strip()
            self.ops.remove_directory_recursive(dir_name)
        elif command.startswith("rm "):
            file_name = command.replace("rm ", "").strip()
            self.ops.remove_file(file_name)
        elif command.startswith("touch "):
            file_name = command.replace("touch ", "").strip()
            self.ops.create_file(file_name)
        elif command.startswith("cat "):
            file_name = command.replace("cat ", "").strip()
            self.ops.read_file(file_name)
        elif command.startswith("echo "):
            parts = command.split(">", 1)
            if len(parts) == 2:
                content, file_name = parts
                file_name = file_name.strip()
                content = content.replace("echo ", "").strip().strip('"')
                self.ops.write_to_file(file_name, content)
            else:
                print(parts[0].replace("echo ", "").strip().strip('"'))
        elif command.startswith("cd "):
            dir_name = command.replace("cd ", "").strip()
            self.nav.change_directory(dir_name)
        else:
            print(f"{Color.Red}Invalid command. Type 'help' for a list of commands.{Color.Reset}")
