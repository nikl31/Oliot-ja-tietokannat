from soda_bottle import SodaBottle

class Menu:
    def __init__(self):
        self.bottles = []

    def show(self):
        print("Menu:")
        print("1 - Add bottle")
        print("2 - Show bottles")
        print("3 - Save bottle")
        print("0 - Exit")

    def handle_choice(self, choice: str):
        if choice == "1":
            print("Creating soda bottle.")
            brand = input("Insert brand: ")
            volume = float(input("Insert volume: "))
            bottle = SodaBottle(brand, volume)
            self.bottles.append(bottle)

        elif choice == "2":
            print("#### Soda bottles ####")
            for i, bottle in enumerate(self.bottles, start=1):
                print(f"Bottle {i}:")
                print(f"  brand - {bottle.brand}")
                print(f"  volume - {bottle.volume}")
            print("#### Soda bottles ####")

        elif choice == "3":
            print("'save' not implemented yet.")

        elif choice == "0":
            print("\nExiting program.")
            return False

        else:
            print("Unknown option, try again.")

        return True