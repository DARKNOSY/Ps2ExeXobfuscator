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

def load(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"{Fore.RED}File not found.{Style.RESET_ALL}")
        return None
    except json.JSONDecodeError as e:
        print(f"{Fore.RED}Invalid JSON format: {e}{Style.RESET_ALL}")
        return None

def save(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"{Fore.GREEN}Data saved successfully.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred while saving the file: {e}{Style.RESET_ALL}")

def main():
    print("\033]0;Ps2ExeXobfuscator by DARKNOSY\007")
    
    get_stats()
    print_header()

    key = "ps_script"
    powershell_path = input(f"Path of your powershell script: ")
    json_data[key] = powershell_path

    key = "exe_name"
    new_value = input(f"Name of the exe: ")
    json_data[key] = new_value

    save("src/config.json", json_data)

    os.system("py src/ps2exe.py")

if __name__ == "__main__":
    json_data = load("src/config.json")
    
    if json_data:
        main()
