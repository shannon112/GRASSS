import pandas as pd
import math
from .mystock import MyStock
from .mytrade import MyTrade, FixedBuy

def execute_trades(df, trades):
    my_stock = MyStock()
    for trade in trades:
        if trade.money == 0: continue
        current_price = df.loc[trade.date]
        current_quantity = math.floor(trade.money/current_price)
        current_cost = current_price*current_quantity
        current_stock = MyStock("", current_price, current_quantity, current_cost)
        my_stock.combine(current_stock)
    return my_stock

def grep_valid_trades_monthly(df, start_date, end_date, fixed_trades):
    my_trades = []
    current = pd.Timestamp(start_date.year, start_date.month, 1)
    while(current < end_date):
        for fixed_trade in fixed_trades:
            current_date = pd.Timestamp(current.year, current.month, fixed_trade.day)
            if current_date > end_date: break
            my_trades.append(grep_valid_trade(df, current_date, fixed_trade.money))
        current = current + pd.DateOffset(months=1)
    return my_trades

def grep_valid_trade(df, the_date, money):
    valid_dates = df.index[df.index>=the_date]
    if len(valid_dates) > 0:
        the_date = valid_dates[0]
        return MyTrade(the_date, money)
    return MyTrade(the_date, 0)
