class CoinAcceptor:
    def __init__(self):
        self.__amount = 0
        self.__value = 0.0

    def insertCoin(self) -> None:
        self.__amount += 1
        self.__value += 1.0

    def getAmount(self) -> int:
        return self.__amount

    def returnCoins(self) -> int:
        coins = self.__amount
        self.__amount = 0
        self.__value = 0.0
        return coins