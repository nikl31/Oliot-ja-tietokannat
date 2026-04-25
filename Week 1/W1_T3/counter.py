class Counter:
    def __init__(self):
        self.__count = 0

    def add_count(self) -> None:
        self.__count += 1

    @property
    def count(self) -> int:
        return self.__count

    def reset(self) -> None:
        self.__count = 0
