import shutil
import ctypes
from colorama import Style, Fore, init

init()

class Colors:
    magenta = Fore.LIGHTMAGENTA_EX
    cyan = Fore.LIGHTCYAN_EX
    white = Fore.WHITE

def print_logo():
    cols = shutil.get_terminal_size().columns
    print()
    print(f"{Colors.magenta}     ██████╗██╗      ██████╗ ██╗   ██╗██████╗ ".center(cols))
    print(f"{Colors.magenta}    ██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗".center(cols))
    print(f"{Colors.magenta}    ██║     ██║     ██║   ██║██║   ██║██║  ██║".center(cols))
    print(f"{Colors.magenta}    ██║     ██║     ██║   ██║██║   ██║██║  ██║".center(cols))
    print(f"{Colors.magenta}     ██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝".center(cols))
    print(f"{Colors.magenta}     ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ".center(cols))
    print(f"{Colors.cyan}    Multi Functional Shorts Maker ~ Serialized".center(cols))
    print()

def print_menu():
    print(f" {Colors.magenta}[{Colors.white}1{Colors.magenta}]{Colors.white} Compile Shorts")
    print(f" {Colors.magenta}[{Colors.white}2{Colors.magenta}]{Colors.white} Reddit Scraper")
    print(f" {Colors.magenta}[{Colors.white}3{Colors.magenta}]{Colors.white} Imgur Scraper")
    print(f" {Colors.magenta}[{Colors.white}4{Colors.magenta}]{Colors.white} Shorts Automatic")
    print(f" {Colors.magenta}[{Colors.white}>{Colors.magenta}]{Colors.white} ", end="")

def prefix_stats(message):
    print(f" {Colors.magenta}[{Colors.white}~{Colors.magenta}] {Colors.white}{message}")

def console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)