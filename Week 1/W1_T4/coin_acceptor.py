class CoinAcceptor:
    def __init__(self):
        self.__amount = 0
        self.__value = 0.0

    def insertCoin(self):
        self.__amount += 1
        self.__value += 1.0  # oletetaan 1 coin = 1.0 arvo

    def getAmount(self) -> int:
        return self.__amount

    def returnCoins(self) -> int:
        coins = self.__amount
        self.__amount = 0
        self.__value = 0.0
        return coins