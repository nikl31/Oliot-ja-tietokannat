class SodaBottle:
    def __init__(self, brand: str, volume: float):
        self.brand = brand
        self.volume = volume

    def serialize(self) -> str:
        return f"{self.brand};{self.volume}"
