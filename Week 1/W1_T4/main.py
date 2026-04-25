from coin_acceptor import CoinAcceptor

def print_menu():
    print("\n1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit program")

def main():
    print("Program starting.")

    coin_acceptor = CoinAcceptor()

    while True:
        print_menu()
        choice = input("Your choice: ")

        if choice == "1":
            coin_acceptor.insertCoin()

        elif choice == "2":
            print(f"Currently '{coin_acceptor.getAmount()}' coins in coin acceptor")

        elif choice == "3":
            returned = coin_acceptor.returnCoins()
            print(f"Coin acceptor returned '{returned}' coins.")

        elif choice == "0":
            print("Program ending.")
            break

if __name__ == "__main__":
    main()