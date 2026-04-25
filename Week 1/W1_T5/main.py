from coin_acceptor import CoinAcceptor


class Main:
    def __init__(self) -> None:
        print("Program starting.")
        print("Welcome to coin acceptor program.")
        print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")

        ca = CoinAcceptor()

        while True:
            choice = input("\nInsert coin(0 return, -1 exit): ")

            if choice == "-1":
                print("Exiting program.")
                break

            value = float(choice)

            if value == 0:
                print("Returning coins...")
                coins, total = ca.returnCoins()
                print(f"{coins} coins with {total}€ value returned.")
                print(f"Inserted coins - {ca.getAmount()}, value - {ca.getValue()}€")

            else:
                print("Inserting...")
                ca.insertCoin(value)
                print(f"Inserted coins - {ca.getAmount()}, value - {ca.getValue()}€")

        print("\nProgram ending.")


if __name__ == "__main__":
    app = Main()
