class Person:
    def __init__(self, fname: str, lname: str):
        self.first_name = fname
        self.last_name = lname

    def fullname(self) -> None:
        print(f"{self.first_name} {self.last_name}")
        return None
