from coin_acceptor import CoinAcceptor

class Main:
    def __init__(self) -> None:
        print("Program starting.")

        ca = CoinAcceptor()

        while True:
            print("1 - Insert coin\n")
            print("2 - Show coins")
            print("3 - Return coins")
            print("0 - Exit program")

            choice = input("Your choice: ")

            if choice == "1":
                ca.insertCoin()

            elif choice == "2":
                print(f"Currently '{ca.getAmount()}' coins in coin acceptor\n")

            elif choice == "3":
                returned = ca.returnCoins()
                print(f"Coin acceptor returned '{returned}' coins.\n")

            elif choice == "0":
                print("\nProgram ending.")
                break

            else:
                print("Invalid option.")

                return None



if __name__ == "__main__":
    app = Main()