from coin_acceptor import CoinAcceptor

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        print("Welcome to coin acceptor program.")
        print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)\n")
        
        ca = CoinAcceptor()
        
        while True:
            coin = float(input("Insert coin(0 return, -1 exit): "))
            
            if coin == -1:
                print("Exiting program.\n")
                break
            
            elif coin == 0:
                print("Returning coins...")
                coins, value = ca.returnCoins()
                print(f"{coins} coins with {value}€ value returned.")
                print(f"Inserted coins - {ca.getAmount()}, value - {ca.getValue()}€\n")
                
            else:
                print("Inserting...")
                ca.insertCoin(coin)
                print(f"Inserted coins - {ca.getAmount()}, value - {ca.getValue()}€\n")
                
        print("Program ending.")

        return None

if __name__ == "__main__":
    app = Main()