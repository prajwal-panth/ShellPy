import os
from utils.styles import Color


class ShellOperations:
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def create_file(self, file_name: str):
        try:
            with open(file_name, 'x'):
                print(f"{Color.Green}File '{file_name}' created successfully.{Color.Reset}")
        except FileExistsError:
            print(f"{Color.Red}File '{file_name}' already exists.{Color.Reset}")
        except Exception as err:
            print(f"{Color.Red}Error creating file: {err}{Color.Reset}")
   
    def create_directory(self, dir_name: str):
        try:
            os.mkdir(dir_name)
            print(f"{Color.Green}Directory '{dir_name}' created successfully.{Color.Reset}")
        except FileExistsError:
            print(f"{Color.Red}Directory '{dir_name}' already exists.{Color.Reset}")
        except Exception as err:
            print(f"{Color.Red}Error creating directory: {err}{Color.Reset}")

    def remove_file(self, file_name: str):
        try:
            os.remove(file_name)
            print(f"{Color.Green}File '{file_name}' removed successfully.{Color.Reset}")
        except FileNotFoundError:
            print(f"{Color.Red}File '{file_name}' does not exist.{Color.Reset}")
        except Exception as err:
            print(f"{Color.Red}Error removing file: {err}{Color.Reset}")

    def remove_directory(self, dir_name: str):
        try:
            os.rmdir(dir_name)
            print(f"{Color.Green}Directory '{dir_name}' removed successfully.{Color.Reset}")
        except FileNotFoundError:
            print(f"{Color.Red}Directory '{dir_name}' does not exist.{Color.Reset}")
        except OSError:
            print(f"{Color.Red}Directory '{dir_name}' is not empty.{Color.Reset}")
        except Exception as err:
            print(f"{Color.Red}Error removing directory: {err}{Color.Reset}")
    
    def remove_directory_recursive(self, dir_name: str):
        try:
            if not os.path.isdir(dir_name):
                print(f"{Color.Red}Directory '{dir_name}' does not exist.{Color.Reset}")
                return
            for item in os.listdir(dir_name):
                item_path = os.path.join(dir_name, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    self.remove_directory_recursive(item_path) 

            os.rmdir(dir_name)
            print(f"{Color.Green}Directory '{dir_name}' and all its contents have been removed.{Color.Reset}")
        except Exception as err:
            print(f"{Color.Red}Error removing directory: {err}{Color.Reset}")


    def read_file(self, file_name: str):
        try:
            with open(file_name, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print(f"{Color.Red}File '{file_name}' does not exist.{Color.Reset}")
        except Exception as err:
            print(f"{Color.Red}Error reading file: {err}{Color.Reset}")

    def write_to_file(self, file_name: str, content: str):
        try:
            with open(file_name, 'w') as f:
                f.write(content)
            print(f"{Color.Green}Content written to '{file_name}' successfully.{Color.Reset}")
        except Exception as err:
            print(f"{Color.Red}Error writing to file: {err}{Color.Reset}")
    
        
