from soda_bottle import SodaBottle

def main():
    print("Program starting.")
    print("Constructing soda bottle.")

    brand = input("Insert brand: ")
    volume = float(input("Insert volume: "))

    bottle = SodaBottle(brand, volume)

    print("SodaBottle object created!")
    print("Serializing SodaBottle object.")

    print("Serialized sodabottle:")
    print(bottle.serialize())

    print("Program ending.")


if __name__ == "__main__":
    main()