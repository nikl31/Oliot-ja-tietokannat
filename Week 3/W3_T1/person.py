class Person:
    def __init__(self, fname: str, lname: str, age: int) -> None:
        self.first_name = fname
        self.last_name = lname
        self.__age = age

    def getAge(self) -> int:
        return self.__age

    def ageUp(self) -> None:
        self.__age += 1

    def getFullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def printFullname(self) -> None:
        print(f"{self.first_name} {self.last_name}")