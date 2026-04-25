from counter import Counter

class Main:
    def __init__(self):
        print("Program starting.")
        print("Initializing counter...")
        self.my_count: Counter = Counter()
        print("Counter initialized.")
        while True:
            print("\nOptions:")
            print("1) Add count")
            print("2) Get count")
            print("3) Zero count")
            print("0) Exit program")
            try:
                choice = int(input("Choice: "))
            except ValueError:
                print("Invalid input! Expected an integer!")
                continue
            if choice == 0:
                print("\nProgram ending.")
                break
            elif choice == 1:
                self.my_count.addCount()
                print("Count increased")
            elif choice == 2:
                cur_value = self.my_count.getCount()
                print(f"Current count '{cur_value}'")
            elif choice == 3:
                self.my_count.zeroCount()
                print("Count zeroed")
            else:
                print("Expected numbers between 0 and 4!")

if __name__ == "__main__":
    Main()