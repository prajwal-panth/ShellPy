import os
from .styles import Color, Icons

class ShellNavigation:
    def __init__(self, path: str = os.getcwd()):
        self.current_path = os.path.abspath(path)

    def list_items(self):
        items = os.listdir(self.current_path)
        if not items:
            print(f"{Color.Yellow}No items found in the current directory.{Color.Reset}")
            return

        print(f"{Color.Green}Contents of {self.current_path}:{Color.Reset}")
        for item in items:
            item_path = os.path.join(self.current_path, item)
            icon = Icons.folder if os.path.isdir(item_path) else Icons.file
            print(f"{icon} {item}")


    def change_directory(self, dir_name: str):
        new_path = os.path.abspath(os.path.join(self.current_path, dir_name))
        if os.path.isdir(new_path):
            self.current_path = new_path
            os.chdir(self.current_path)
            print(f"{Color.Green}Changed directory to: {self.current_path}{Color.Reset}")
        elif os.path.isfile(new_path):
            print(f"{Color.Red}'{dir_name}' is a file, not a directory.{Color.Reset}")
        else:
            print(f"{Color.Red}Directory '{dir_name}' does not exist.{Color.Reset}")