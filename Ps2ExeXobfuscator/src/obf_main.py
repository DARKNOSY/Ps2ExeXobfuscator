import json, os, requests
from colorama import Fore, Style, init

init(autoreset=True)

def get_stats():
    global stars_count, forks_count, watchers_count

    url = f"https://api.github.com/repos/DARKNOSY/Ps2ExeXobfuscator"
    response = requests.get(url)
    
    if response.status_code == 200:
        repo_data = response.json()
        stars_count = repo_data["stargazers_count"]
        forks_count = repo_data["forks_count"]
        watchers_count = repo_data["watchers_count"]

    else:
        print(f"{Fore.RED}Failed to fetch repository details.{Style.RESET_ALL}")

def print_success(message):
    print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")

def print_error(message):
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")

def print_header():
    header_text = f"Ps2ExeXobfuscator by @DARKNOSY - Stars: {stars_count}, Forks: {forks_count}, Watchers: {watchers_count}"
    console_width = os.get_terminal_size().columns
    padding_width = (console_width - len(header_text)) // 2
    header_line = "=" * console_width
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{header_line}")
    print(f"{Fore.BLUE}{Style.BRIGHT}{' ' * padding_width}{header_text}{' ' * padding_width}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{header_line}{Style.RESET_ALL}")

def main():
    print("\033]0;Ps2ExeXobfuscator by DARKNOSY\007")
    
    #get_stats()
    #print_header()

    powershell_path = input(f"Path of your powershell script: ")
    num_obf = input(f"Layers of obfuscation: ")

    os.system(f"py src/obf.py {powershell_path} {num_obf}")

if __name__ == "__main__":
    main()