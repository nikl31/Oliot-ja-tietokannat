class CoinAcceptor:
    def __init__(self):
        self.__amount = 0
        self.__value = 0

    def insertCoin(self, value: float) -> None:
        self.__amount += 1
        self.__value += value

    def getAmount(self) -> int:
        return self.__amount

    def getValue(self) -> float:
        return self.__value

    def returnCoins(self):
        coins = self.__amount
        value = self.__value

        self.__amount = 0
        self.__value = 0

        return coins, value