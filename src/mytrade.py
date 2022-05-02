class MyTrade:
    def __init__(self, date=None, money=0.0):
        self.date = date
        self.money = money


class FixedBuy:
    def __init__(self, day=1, money=0.0):
        self.day = day
        self.money = money


class MyDividends:
    def __init__(self, date=None, dividends=0.0):
        self.date = date
        self.dividends = dividends
