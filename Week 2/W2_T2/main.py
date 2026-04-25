from soda_bottle import SodaBottle

def main():
    print("Program starting.")

    filename = input("Insert filename: ")

    file = open(filename, "r")
    line = file.readline().strip()
    file.close()

    print(f'Deserializing "{line}"')

    bottle = SodaBottle.deserialize(line)

    print(f"Looks like {bottle.volume} litre {bottle.brand} bottle.")

    print("Program ending.")


if __name__ == "__main__":
    main()