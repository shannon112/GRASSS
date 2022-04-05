import pandas as pd
import math
from .mystock import MyStock

def buy_fixed_money_on_dates(
    df, dates, money
):
    my_stock = MyStock()
    for buy_date in dates:
        current_price = df.loc[buy_date]
        current_quantity = math.floor(money/current_price)
        current_cost = current_price*current_quantity
        current_stock = MyStock("", current_price, current_quantity, current_cost)
        my_stock.combine(current_stock)
    return my_stock

def combine_bought_stocks(
    mystocks
):
    my_stock = MyStock()
    for mystock in mystocks:
        my_stock.combine(mystock)
    return my_stock

def grep_monthly_valid_tradedate(df, start_date, end_date, the_date_day):
    dates = []
    current_date = pd.Timestamp(start_date.year, start_date.month, the_date_day)
    assert start_date<current_date
    while(1):
        if current_date > end_date: break
        if current_date in df.index: 
            dates.append(current_date)
            current_date = current_date + pd.DateOffset(months=1)
            current_date = pd.Timestamp(current_date.year, current_date.month, the_date_day)
        else:
            current_date = current_date + pd.Timedelta("1 day")
    return dates

def grep_valid_tradedate(df, the_date):
    while(1):
        if the_date in df.index: 
            return the_date
        else:
            the_date = the_date + pd.Timedelta("1 day")
