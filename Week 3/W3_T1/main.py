from person import Person

class main:
    def __init__(self) -> None:
        print("Program starting.")
        print("Creating person...")
        
        person = Person("John", "Doe", 30)
        
        print("Person created.")
        
        print(f"Name: {person.getFullname()}")
        print(f"Age: {person.getAge()}")
        
        print("Person has now birthday...")
        
        person.ageUp()
        age = person.getAge()
        
        print(f"New age: {age}")
        
        print("Program ending.")

        return None


if __name__ == "__main__":
    app = main()    