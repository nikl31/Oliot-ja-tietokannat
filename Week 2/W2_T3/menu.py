class Menu:
    def show(self):
        print("Menu:")
        print("1 - Add bottle")
        print("2 - Show bottle")
        print("3 - Save bottle")
        print("0 - Exit")

    def handle_choice(self, choice: str):
        if choice == "1":
            print("'Add bottle' not implemented yet.")
            print()
        elif choice == "2":
            print("'Show bottle' not implemented yet.")
            print()
        elif choice == "3":
            print("'Save bottle' not implemented yet.")
            print()
        elif choice == "0":
            print("\nExiting program.")
            return False
        else:
            print("Unknown option, try again.")
            print()
        return True