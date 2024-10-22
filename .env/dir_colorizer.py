# Task 3

import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory(path: Path, indent=0):

    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{"    " * indent}{Fore.GREEN}{item.name}/")
                print_directory(item, indent + 1)

            else:
                print(f"{"    " * indent}{Fore.WHITE}{item.name}/")
    except PermissionError:
        print(f"{"    " * indent}{Fore.RED}Access denied: {item}/")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED} Error: Path '{directory_path}' is not a directory.")
        sys.exit(1)

    print(f"{Fore.BLUE} Directory structure for: {directory_path}")
    print_directory(directory_path)

if __name__ == "__main__":
    main()