class SodaBottle:
    def __init__(self, brand: str, volume: float):
        self.brand = brand
        self.volume = volume

    def serialize(self) -> str:
        return f"{self.brand};{self.volume}"

    @staticmethod
    def deserialize(data: str):
        parts = data.strip().split(";")
        brand = parts[0]
        volume = float(parts[1])
        return SodaBottle(brand, volume)