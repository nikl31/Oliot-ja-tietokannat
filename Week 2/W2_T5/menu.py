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
            print()
            self.bottles.append(SodaBottle(brand, volume))

        elif choice == "2":
            print("#### Soda bottles ####")
            for i, bottle in enumerate(self.bottles, start=1):
                print(f"Bottle {i}:")
                print(f"  brand - {bottle.brand}")
                print(f"  volume - {bottle.volume}")
            print("#### Soda bottles ####")

        elif choice == "3":
            print("Saving soda bottles...")
            print()

            rows = []
            for bottle in self.bottles:
                rows.append(bottle.serialize() + "\n")

            content = "".join(rows)

            file = open("inventory.txt", "w")
            file.write(content)
            file.close()

            print("Saving completed!")

        elif choice == "0":
            print("\nExiting program.")
            return False

        else:
            print("Unknown option, try again.")

        return True