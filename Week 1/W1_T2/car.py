class Car:
    def __init__(self, color: str):
        self.color = color
        self.engine_on = False

    def start(self) -> None:
        if not self.engine_on:
            print(f"{self.color} car started.")
            self.engine_on = True
        else:
            print(f"{self.color} is already running.")
        return None
