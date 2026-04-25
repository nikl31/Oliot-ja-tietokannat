from menu import Menu

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        
        menu = Menu()
        running = True
        
        while running:
            menu.show()
            choice = input("Your choice: ")
            
            running = menu.handle_choice(choice)
            
        print("Program ending.")

        return None


if __name__ == "__main__":
    app = Main()