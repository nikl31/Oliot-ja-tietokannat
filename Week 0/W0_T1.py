from colorama import init, Fore, Style

init()

name = input(Fore.GREEN + "Insert name: " + Style.RESET_ALL)
print("Hello " + Fore.GREEN + name + Style.RESET_ALL)