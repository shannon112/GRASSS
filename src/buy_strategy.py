from .utils import *

def fubon_dollar_cost_averaging(
    df, money_date06, money_date16, money_date26
):
# if it's not the trading date, then postponded for 1 day.
# buy at the afternoon, not sure the actual buying point (might be close to Close)
# each time buy the stock, handling fee = 1
# options: 06, 16, 26. You're allowed to bonus 1 times.
# need to support dividends in the future (bought before X date you can get it)
    start_date = df.index[0]
    end_date = df.index[-1]

    #df_dividends = df[df['Dividends'] > 0]
    #print(df_dividends)

    df = df['Close']
    my_stocks = []

    if money_date06 > 0:
        dates = grep_monthly_valid_tradedate(df, start_date, end_date, 6)
        my_stocks.append(buy_fixed_money_on_dates(df, dates, money_date06))
    if money_date16 > 0:
        dates = grep_monthly_valid_tradedate(df, start_date, end_date, 16)
        my_stocks.append(buy_fixed_money_on_dates(df, dates, money_date06))
    if money_date26 > 0:
        dates = grep_monthly_valid_tradedate(df, start_date, end_date, 26)
        my_stocks.append(buy_fixed_money_on_dates(df, dates, money_date06))
    total = combine_bought_stocks(my_stocks)
    return total
