import math
from collections import deque

import pandas as pd

from .mystock import MyStock
from .mytrade import FixedBuy, MyDividends, MyTrade


def execute_trades(stock_id, df, dividends, trades):
    my_stock = MyStock(stock_id)
    for trade in trades:
        if trade.money == 0:
            continue
        if len(dividends) and (dividends[0].date < trade.date):
            my_stock.dividends += dividends[0].dividends * my_stock.quantity
            print(f"{dividends[0].date} dividends {my_stock.dividends}")
            dividends.popleft()
        current_price = df.loc[trade.date]["Close"]
        current_quantity = math.floor(trade.money / current_price)
        current_cost = current_price * current_quantity
        current_stock = MyStock(stock_id, current_price, current_quantity, current_cost)
        print(f"{trade.date} buying {current_stock.str_info()}")
        my_stock.combine(current_stock)
    return my_stock


def grep_valid_trades_monthly(df, fixed_trades):
    df = df["Close"]
    start_date = df.index[0]
    end_date = df.index[-1]
    my_trades = []
    current = pd.Timestamp(start_date.year, start_date.month, 1)
    while current < end_date:
        for fixed_trade in fixed_trades:
            current_date = pd.Timestamp(current.year, current.month, fixed_trade.day)
            if current_date > end_date:
                break
            my_trades.append(grep_valid_trade(df, current_date, fixed_trade.money))
        current = current + pd.DateOffset(months=1)
    return my_trades


def grep_valid_trade(df, the_date, money):
    valid_dates = df.index[df.index >= the_date]
    if len(valid_dates) > 0:
        the_date = valid_dates[0]
        return MyTrade(the_date, money)
    return MyTrade(the_date, 0)


def grep_valid_dividends(df):
    my_dividends = deque()
    df_dividends = df[df["Dividends"] > 0]
    for date in df_dividends.index:
        my_dividends.append(MyDividends(date, df_dividends["Dividends"].loc[date]))
    return my_dividends
