# 🐚 ShellPy: A Simple Python-Based Shell

A lightweight Python-based command-line tool that mimics basic Linux commands for file and directory operations.

## ✨ Features  

- 📂 **Directory Operations**: Create (`mkdir`), remove (`rmdir`), navigate (`cd`), and list (`ls`) directories.  
- 📄 **File Operations**: Create (`touch`), remove (`rm`), read (`cat`), and write (`echo`) files.  
- 🌐 **Navigation Commands**: Easily switch directories and check the current working directory (`pwd`).  
- 🖥️ **Utilities**: Clear the screen (`clear`) and view shell version or help.  
- ✅ **Cross-Platform**: Works on Linux, macOS, and Windows.  

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/prajwal-panth/ShellPy.git

# Navigate to project directory
cd ShellPy
```

### Requirements

* Python 3.6+
* No additional dependencies

## 🛠️ Available Commands

| Command | Description |
|---------|-------------|
| `ls` / `list` | List items in current directory |
| `pwd` | Print working directory |
| `mkdir <dir>` | Create new directory |
| `rmdir <dir>` | Remove empty directory |
| `rm <file>` | Remove file |
| `rm -r <dir>` | Remove directory recursively |
| `touch <file>` | Create empty file |
| `cat <file>` | Display file contents |
| `echo "text" > <file>` | Write to file |
| `cd <dir>` | Change directory |
| `cd ..` | Move up one directory level | 
| `clear` | Clear screen |
| `exit` | Exit shell |
| `--version` | Show version |
| `help` | Show help |

## 📖 Usage Example

```bash
💻 >> mkdir my_folder
💻 >> cd my_folder
💻 >> touch example.txt
💻 >> echo "Hello, ShellPy!" > example.txt
💻 >> cat example.txt
Hello, ShellPy!
💻 >> cd ..
💻 >> rm -r my_folder
```

## 📦 Project Structure

```bash
ShellPy/
├── main.py         # Entry point for the shell program
├── commands.py     # Handles user commands and maps them to operations
├── navigation.py   # Manages directory navigation
├── operations.py   # Handles file and directory operations
├── utils.py        # Utility functions and constants
├── README.md       # Project documentation
└── LICENSE         # MIT License file
```

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 💡 Contributing

Contributions welcome! Fork the repository, make improvements, and submit a pull request.