from coin_acceptor import CoinAcceptor


def oo_main_structure():
    print("Program starting.")

    ca = CoinAcceptor()

    while True:
        print("1 - Insert coin")
        print("2 - Show coins")
        print("3 - Return coins")
        print("0 - Exit program")

        choice = input("Your choice: ")

        if choice == "1":
            ca.insertCoin()

        elif choice == "2":
            print(f"Currently '{ca.getAmount()}' coins in coin acceptor")

        elif choice == "3":
            returned = ca.returnCoins()
            print(f"Coin acceptor returned '{returned}' coins.")

        elif choice == "0":
            print("Program ending.")
            break


if __name__ == "__main__":
    oo_main_structure()