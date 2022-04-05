from .utils import *

def dollar_cost_averaging(
    df, start_date, end_date, fixed_buys
):
    df = df['Close']
    trades = grep_valid_trades_monthly(df, start_date, end_date, fixed_buys)
    return execute_trades(df, trades)

def fubon_dollar_cost_averaging(
    df, money_date06, money_date16, money_date26
):
# if it's not the trading date, then postponded for 1 day.
# buy at the afternoon, not sure the actual buying point (might be close to Close)
# each time buy the stock, handling fee = 1
# options: 06, 16, 26. You're allowed to bonus 1 times.
# need to support dividends in the future (bought before X date you can get it)
    #df_dividends = df[df['Dividends'] > 0]
    #print(df_dividends)

    start_date = df.index[0]
    end_date = df.index[-1]

    fixed_buys = []
    if money_date06 > 0: fixed_buys.append(FixedBuy(6, money_date06))
    if money_date16 > 0: fixed_buys.append(FixedBuy(16, money_date16))
    if money_date26 > 0: fixed_buys.append(FixedBuy(26, money_date26))
    return dollar_cost_averaging(df, start_date, end_date, fixed_buys)
