class Color:
    Green = "\033[92m"
    Red = "\033[91m"
    Yellow = "\033[93m"
    Blue = "\033[94m"
    Reset = "\033[0m"


class Icons:
    folder = "\U0001F4C1"  # 📁
    file = "\U0001F4C4"    # 📄
    info = "\U00002139"    # ℹ️


class Info:
    VERSION = "1.0"
    @staticmethod
    def show_version():
        print(f"{Icons.info} {Color.Green}Python Shell Version {Info.VERSION}{Color.Reset}")
    
    def show_help():
        help_text = f"""
        {Icons.info} {Color.Blue}Available Commands:{Color.Reset}
        - ls / list         : List items in the current directory
        - pwd               : Print current working directory
        - mkdir <dir_name>  : Create a new directory
        - rmdir <dir_name>  : Remove an empty directory
        - rm <file_name>    : Remove a file
        - rm -r <dir_name>  : Remove a non-empty directory recursively
        - touch <file_name> : Create a new empty file
        - cat <file_name>   : Display file contents
        - echo \"content\" > <file_name> : Write content to file
        - cd <dir_name>     : Change directory
        - cd ..             : Change directory
        - clear             : Clear the screen
        - exit              : Exit the Shell
        - --version         : Display the version
        """
        print(help_text)
        
